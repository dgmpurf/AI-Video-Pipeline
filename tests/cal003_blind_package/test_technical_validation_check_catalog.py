from dataclasses import FrozenInstanceError
from decimal import Decimal
from pathlib import Path
import inspect
import math
import unittest

from tools.cal003_blind_package import technical_validation as tv


class CheckCatalogTests(unittest.TestCase):
    def test_01_exact_catalog_count(self) -> None:
        self.assertEqual(len(tv.CHECK_CATALOG), 23)

    def test_02_exact_catalog_order(self) -> None:
        self.assertEqual(
            tv.CHECK_CODES,
            (
                "FILE_PRESENT",
                "FILE_REGULAR",
                "FILE_NONEMPTY",
                "TARGET_SIZE_EXACT",
                "TOP_LEVEL_FREE_BOX_VALID",
                "FFPROBE_JSON_PARSE",
                "CONTAINER_MP4",
                "VIDEO_STREAM_COUNT",
                "AUDIO_STREAM_COUNT",
                "OTHER_STREAM_COUNT",
                "CODEC_H264",
                "PIXEL_FORMAT_YUV420P",
                "WIDTH_1280",
                "HEIGHT_720",
                "DURATION_5_085011",
                "ROTATION_ZERO",
                "FRAME_EVIDENCE_121",
                "METADATA_SAFETY",
                "FULL_DECODE_PASS",
                "VIDEO_FRAMEMD5_EQUIVALENCE",
                "AUDIO_FRAMEMD5_EQUIVALENCE",
                "HASH_UNIQUE_AMONG_DIAGNOSTIC_OUTPUTS",
                "HASH_DIFFERS_FROM_ALL_CANONICAL_MEDIA",
            ),
        )

    def test_03_ordinals_are_contiguous(self) -> None:
        self.assertEqual([item.ordinal for item in tv.CHECK_CATALOG], list(range(1, 24)))

    def test_04_phase_set(self) -> None:
        self.assertEqual(len(tv.EXECUTION_PHASES), 14)
        self.assertIn("COMPLETE", tv.EXECUTION_PHASES)

    def test_05_safe_null(self) -> None:
        self.assertTrue(tv.is_safe_scalar(None))

    def test_06_safe_boolean(self) -> None:
        self.assertTrue(tv.is_safe_scalar(True))

    def test_07_safe_integer(self) -> None:
        self.assertTrue(tv.is_safe_scalar(121))

    def test_08_safe_finite_float(self) -> None:
        self.assertTrue(tv.is_safe_scalar(1.5))

    def test_09_safe_decimal_string(self) -> None:
        self.assertTrue(tv.is_safe_scalar("5.085011"))

    def test_10_safe_short_scalar_list(self) -> None:
        self.assertTrue(tv.is_safe_scalar([True, 1, 2.0, "x", None]))

    def test_11_reject_dict(self) -> None:
        self.assertFalse(tv.is_safe_scalar({"raw": "payload"}))

    def test_12_reject_nested_list(self) -> None:
        self.assertFalse(tv.is_safe_scalar([[1]]))

    def test_13_reject_bytes(self) -> None:
        self.assertFalse(tv.is_safe_scalar(b"raw"))

    def test_14_reject_path(self) -> None:
        self.assertFalse(tv.is_safe_scalar(Path("private")))

    def test_15_reject_nan(self) -> None:
        self.assertFalse(tv.is_safe_scalar(math.nan))

    def test_16_reject_infinity(self) -> None:
        self.assertFalse(tv.is_safe_scalar(math.inf))

    def test_17_reject_overlong_string(self) -> None:
        self.assertFalse(tv.is_safe_scalar("x" * 161))

    def test_18_reject_overlong_list(self) -> None:
        self.assertFalse(tv.is_safe_scalar(list(range(17))))

    def test_19_check_result_is_frozen(self) -> None:
        result = tv.evaluate_check("WIDTH_1280", 1280)
        with self.assertRaises(FrozenInstanceError):
            result.observed = 1

    def test_20_first_failure_stops_sequence(self) -> None:
        observations = {
            "FILE_PRESENT": True,
            "FILE_REGULAR": False,
            "FILE_NONEMPTY": True,
        }
        results = tv.evaluate_ordered_observations(observations)
        self.assertEqual([item.check_code for item in results], ["FILE_PRESENT", "FILE_REGULAR"])
        self.assertFalse(results[-1].result)

    def test_21_no_raw_payload_field(self) -> None:
        self.assertNotIn("raw_payload", tv.model_field_names(tv.CheckResult))

    def test_22_no_mapping_or_salt_fields(self) -> None:
        names = set(tv.model_field_names(tv.TechnicalValidationError))
        self.assertTrue(names.isdisjoint({"mapping", "salt", "source_to_alias"}))

    def test_23_expected_duration_is_decimal(self) -> None:
        self.assertEqual(tv.EXPECTED_DURATION, Decimal("5.085011"))

    def test_24_duration_tolerance_is_decimal(self) -> None:
        self.assertEqual(tv.DURATION_TOLERANCE, Decimal("0.000001"))

    def test_25_exact_duration_passes(self) -> None:
        self.assertTrue(tv.duration_within_tolerance("5.085011"))

    def test_26_positive_boundary_passes(self) -> None:
        self.assertTrue(tv.duration_within_tolerance("5.085012"))

    def test_27_negative_boundary_passes(self) -> None:
        self.assertTrue(tv.duration_within_tolerance("5.085010"))

    def test_28_positive_beyond_boundary_fails(self) -> None:
        self.assertFalse(tv.duration_within_tolerance("5.085013"))

    def test_29_negative_beyond_boundary_fails(self) -> None:
        self.assertFalse(tv.duration_within_tolerance("5.085009"))

    def test_30_positive_boundary_difference_is_exact(self) -> None:
        self.assertEqual(tv.duration_difference_text("5.085012"), "0.000001")

    def test_31_negative_boundary_difference_is_exact(self) -> None:
        self.assertEqual(tv.duration_difference_text("5.085010"), "0.000001")

    def test_32_duration_check_persists_bounded_string(self) -> None:
        result = tv.evaluate_check("DURATION_5_085011", "5.085012")
        self.assertEqual(result.observed, "5.085012")
        self.assertIsInstance(result.expected, str)

    def test_33_duration_gate_does_not_call_math_isclose(self) -> None:
        source = inspect.getsource(tv.duration_within_tolerance)
        self.assertNotIn("isclose", source)

    def test_34_module_has_no_math_isclose_call(self) -> None:
        source = inspect.getsource(tv)
        self.assertNotIn("math.isclose", source)

    def test_35_parse_duration_rejects_float(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text(5.085011)

    def test_36_parse_duration_rejects_integer(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text(5)

    def test_37_parse_duration_rejects_null(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text(None)

    def test_38_parse_duration_rejects_empty(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text("")

    def test_39_parse_duration_rejects_malformed(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text("five")

    def test_40_parse_duration_rejects_nan(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text("NaN")

    def test_41_parse_duration_rejects_positive_infinity(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text("Infinity")

    def test_42_parse_duration_rejects_negative_infinity(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text("-Infinity")

    def test_43_parse_duration_rejects_overlong_text(self) -> None:
        with self.assertRaises(tv.SafeTechnicalValueError):
            tv.parse_finite_decimal_text("1" * 65)


if __name__ == "__main__":
    unittest.main()
