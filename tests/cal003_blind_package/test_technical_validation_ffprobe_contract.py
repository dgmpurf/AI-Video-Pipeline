import json
import unittest

from tools.cal003_blind_package import technical_validation as tv


def payload() -> dict[str, object]:
    return {
        "format": {
            "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
            "duration": "5.085011",
            "tags": {
                "major_brand": "isom",
                "minor_version": "512",
                "compatible_brands": "isomiso2avc1mp41",
                "encoder": "Lavf",
            },
        },
        "streams": [
            {
                "codec_type": "video",
                "codec_name": "h264",
                "pix_fmt": "yuv420p",
                "width": 1280,
                "height": 720,
                "nb_read_frames": "121",
                "tags": {"language": "und", "handler_name": "VideoHandler"},
            },
            {
                "codec_type": "audio",
                "codec_name": "aac",
                "tags": {"language": "und", "handler_name": "SoundHandler"},
            },
        ],
    }


class FFprobeContractTests(unittest.TestCase):
    def facts(self, value: dict[str, object] | None = None) -> tv.ProbeFacts:
        facts, error = tv.parse_ffprobe_bytes(
            json.dumps(value or payload(), allow_nan=False).encode("utf-8")
        )
        self.assertIsNone(error)
        self.assertIsNotNone(facts)
        return facts

    def duration_error(self, value: object) -> tv.TechnicalValidationError:
        item = payload()
        item["format"]["duration"] = value
        raw = json.dumps(item, allow_nan=False).encode("utf-8")
        facts, error = tv.parse_ffprobe_bytes(raw)
        self.assertIsNone(facts)
        self.assertIsNotNone(error)
        return error

    def test_01_valid_mp4_payload(self) -> None:
        self.assertTrue(self.facts().format_is_mp4)

    def test_02_mp4_token_in_format_name(self) -> None:
        value = payload()
        value["format"]["format_name"] = "mov,mp4,m4a"
        self.assertTrue(self.facts(value).format_is_mp4)

    def test_03_one_video(self) -> None:
        self.assertEqual(self.facts().video_stream_count, 1)

    def test_04_one_audio(self) -> None:
        self.assertEqual(self.facts().audio_stream_count, 1)

    def test_05_zero_other(self) -> None:
        self.assertEqual(self.facts().other_stream_count, 0)

    def test_06_other_stream_is_counted(self) -> None:
        value = payload()
        value["streams"].append({"codec_type": "subtitle"})
        self.assertEqual(self.facts(value).other_stream_count, 1)

    def test_07_extra_video_is_counted_as_video(self) -> None:
        value = payload()
        value["streams"].append({"codec_type": "video"})
        self.assertEqual(self.facts(value).video_stream_count, 2)

    def test_08_h264(self) -> None:
        self.assertEqual(self.facts().codec, "h264")

    def test_09_yuv420p(self) -> None:
        self.assertEqual(self.facts().pixel_format, "yuv420p")

    def test_10_width(self) -> None:
        self.assertEqual(self.facts().width, 1280)

    def test_11_height(self) -> None:
        self.assertEqual(self.facts().height, 720)

    def test_12_duration_text_is_preserved(self) -> None:
        self.assertEqual(self.facts().duration_text, "5.085011")

    def test_13_duration_positive_boundary_is_ordinary_pass(self) -> None:
        value = payload()
        value["format"]["duration"] = "5.085012"
        facts = self.facts(value)
        self.assertTrue(tv.evaluate_check("DURATION_5_085011", facts.duration_text).result)

    def test_14_duration_beyond_boundary_is_ordinary_failure(self) -> None:
        value = payload()
        value["format"]["duration"] = "5.085013"
        facts = self.facts(value)
        self.assertFalse(tv.evaluate_check("DURATION_5_085011", facts.duration_text).result)

    def test_15_rotation_absent_means_zero(self) -> None:
        self.assertEqual(self.facts().rotation, 0)

    def test_16_explicit_nonzero_rotation(self) -> None:
        value = payload()
        value["streams"][0]["side_data_list"] = [{"rotation": -90}]
        self.assertEqual(self.facts(value).rotation, -90)

    def test_17_frame_evidence_121(self) -> None:
        self.assertEqual(self.facts().frame_evidence, 121)

    def test_18_wrong_frame_evidence_is_ordinary_failure(self) -> None:
        value = payload()
        value["streams"][0]["nb_read_frames"] = "120"
        facts = self.facts(value)
        self.assertFalse(tv.evaluate_check("FRAME_EVIDENCE_121", facts.frame_evidence).result)

    def test_19_generic_handler_metadata_accepted(self) -> None:
        self.assertEqual(self.facts().forbidden_metadata_marker_count, 0)

    def test_20_generic_encoder_metadata_accepted(self) -> None:
        value = payload()
        value["format"]["tags"]["encoder"] = "Lavf60"
        self.assertEqual(self.facts(value).forbidden_metadata_marker_count, 0)

    def test_21_forbidden_windows_path_detected(self) -> None:
        value = payload()
        value["format"]["tags"]["comment"] = r"C:\private\source.mp4"
        self.assertEqual(self.facts(value).forbidden_metadata_marker_count, 1)

    def test_22_forbidden_canonical_marker_detected(self) -> None:
        value = payload()
        value["streams"][0]["tags"]["title"] = "PUSH_01"
        self.assertEqual(self.facts(value).forbidden_metadata_marker_count, 1)

    def test_23_malformed_json_is_local_safety(self) -> None:
        facts, error = tv.parse_ffprobe_bytes(b"{")
        self.assertIsNone(facts)
        self.assertTrue(error.local_safety_failure)

    def test_24_duplicate_key_is_local_safety(self) -> None:
        facts, error = tv.parse_ffprobe_bytes(b'{"format":{},"format":{},"streams":[]}')
        self.assertIsNone(facts)
        self.assertTrue(error.local_safety_failure)

    def test_25_invalid_utf8_is_local_safety(self) -> None:
        facts, error = tv.parse_ffprobe_bytes(b"\xff")
        self.assertIsNone(facts)
        self.assertTrue(error.local_safety_failure)

    def test_26_valid_wrong_codec_is_ordinary_predicate(self) -> None:
        value = payload()
        value["streams"][0]["codec_name"] = "hevc"
        facts = self.facts(value)
        self.assertFalse(tv.evaluate_check("CODEC_H264", facts.codec).result)

    def test_27_nan_duration_fails_safely(self) -> None:
        error = self.duration_error("NaN")
        self.assertEqual(error.check_code, "DURATION_5_085011")

    def test_28_positive_infinity_duration_fails_safely(self) -> None:
        self.assertTrue(self.duration_error("Infinity").local_safety_failure)

    def test_29_negative_infinity_duration_fails_safely(self) -> None:
        self.assertTrue(self.duration_error("-Infinity").local_safety_failure)

    def test_30_empty_duration_fails_safely(self) -> None:
        self.assertEqual(self.duration_error("").observed, "invalid_decimal_text")

    def test_31_malformed_duration_fails_safely(self) -> None:
        self.assertEqual(self.duration_error("five").error_class, "DURATION_DECIMAL_TEXT_ERROR")

    def test_32_integer_duration_fails_safely(self) -> None:
        self.assertTrue(self.duration_error(5).local_safety_failure)

    def test_33_float_duration_fails_safely(self) -> None:
        self.assertTrue(self.duration_error(5.085011).local_safety_failure)

    def test_34_null_duration_fails_safely(self) -> None:
        self.assertTrue(self.duration_error(None).local_safety_failure)

    def test_35_overlong_duration_fails_safely(self) -> None:
        self.assertTrue(self.duration_error("1" * 65).local_safety_failure)

    def test_36_duration_error_has_no_raw_value(self) -> None:
        error = self.duration_error("private-duration-payload")
        self.assertNotIn("private-duration-payload", str(error.to_dict()))


if __name__ == "__main__":
    unittest.main()
