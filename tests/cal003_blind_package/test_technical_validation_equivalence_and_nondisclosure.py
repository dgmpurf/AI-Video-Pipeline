from dataclasses import FrozenInstanceError
from pathlib import Path
import inspect
import struct
import tempfile
import unittest

from tools.cal003_blind_package import technical_validation as tv


class EquivalenceAndNondisclosureTests(unittest.TestCase):
    def test_01_framemd5_header_removal(self) -> None:
        self.assertEqual(tv.normalize_framemd5(b"# header\n0, 0, hash\n"), b"0, 0, hash")

    def test_02_framemd5_data_line_preservation(self) -> None:
        self.assertEqual(tv.normalize_framemd5(b" 0,  1, abc \r\n"), b" 0,  1, abc ")

    def test_03_framemd5_record_order_preserved(self) -> None:
        self.assertEqual(tv.normalize_framemd5(b"# h\nsecond\nfirst\n"), b"second\nfirst")

    def test_04_equal_video_records(self) -> None:
        self.assertTrue(tv.compare_framemd5(b"# a\nx\n", b"# b\r\nx\r\n").equivalent)

    def test_05_unequal_video_records(self) -> None:
        self.assertFalse(tv.compare_framemd5(b"x\n", b"y\n").equivalent)

    def test_06_equal_audio_records(self) -> None:
        self.assertTrue(tv.compare_framemd5(b"a\nb\n", b"a\nb").equivalent)

    def test_07_unequal_audio_records(self) -> None:
        self.assertFalse(tv.compare_framemd5(b"a\n", b"a\nb\n").equivalent)

    def test_08_record_counts(self) -> None:
        result = tv.compare_framemd5(b"# h\na\nb\n", b"a\nb\n")
        self.assertEqual((result.source_record_count, result.diagnostic_record_count), (2, 2))

    def test_09_hash_uniqueness_true(self) -> None:
        self.assertTrue(tv.hashes_are_unique(["a", "b", "c"]))

    def test_10_hash_uniqueness_false(self) -> None:
        self.assertFalse(tv.hashes_are_unique(["a", "b", "a"]))

    def test_11_canonical_difference_true(self) -> None:
        self.assertTrue(tv.hashes_differ_from_canonical(["a"], ["b"]))

    def test_12_canonical_collision_false(self) -> None:
        self.assertFalse(tv.hashes_differ_from_canonical(["a"], ["a", "b"]))

    def test_13_free_box_structure_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x.mp4"
            path.write_bytes(struct.pack(">I4s", 8, b"free"))
            self.assertTrue(tv.top_level_free_box_valid(path, 8))

    def test_14_free_box_wrong_type(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x.mp4"
            path.write_bytes(struct.pack(">I4s", 8, b"skip"))
            self.assertFalse(tv.top_level_free_box_valid(path, 8))

    def test_15_free_box_wrong_size(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x.mp4"
            path.write_bytes(struct.pack(">I4s", 9, b"free"))
            self.assertFalse(tv.top_level_free_box_valid(path, 8))

    def test_16_target_size_exact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x.mp4"
            path.write_bytes(b"123")
            observed = tv.file_contract_observations(path, 3)
            self.assertEqual(observed["TARGET_SIZE_EXACT"], 3)

    def test_17_sanitized_error_omits_message(self) -> None:
        self.assertNotIn("message", tv.model_field_names(tv.TechnicalValidationError))

    def test_18_sanitized_error_omits_args(self) -> None:
        self.assertNotIn("args", tv.model_field_names(tv.TechnicalValidationError))

    def test_19_sanitized_error_omits_traceback(self) -> None:
        self.assertNotIn("traceback", tv.model_field_names(tv.TechnicalValidationError))

    def test_20_error_model_is_frozen(self) -> None:
        error = tv.TechnicalValidationError(
            "SAFE", "FFPROBE_PARSE", "FFPROBE_JSON_PARSE", True, False, True
        )
        with self.assertRaises(FrozenInstanceError):
            error.observed = True

    def test_21_module_contains_no_randomness_surface(self) -> None:
        source = inspect.getsource(tv)
        self.assertNotIn("import random", source)
        self.assertNotIn("import secrets", source)

    def test_22_module_has_no_mapping_or_salt_model(self) -> None:
        names = set(tv.model_field_names(tv.CheckResult))
        names.update(tv.model_field_names(tv.ProbeFacts))
        self.assertTrue(names.isdisjoint({"mapping", "salt", "source_to_alias"}))

    def test_23_probe_model_has_no_raw_payload(self) -> None:
        names = tv.model_field_names(tv.ProbeFacts)
        self.assertTrue(set(names).isdisjoint({"raw", "payload", "stdout", "stderr"}))

    def test_24_check_result_serializes_safe_list(self) -> None:
        result = tv.CheckResult("FILE_PRESENT", True, [True], [True], "FILE_CONTRACT")
        self.assertEqual(result.to_dict()["observed"], [True])

    def test_25_probe_facts_has_duration_text(self) -> None:
        self.assertIn("duration_text", tv.model_field_names(tv.ProbeFacts))

    def test_26_probe_facts_has_no_duration_float(self) -> None:
        self.assertNotIn("duration", tv.model_field_names(tv.ProbeFacts))

    def test_27_implementation_version_is_v0_2(self) -> None:
        self.assertEqual(tv.IMPLEMENTATION_VERSION, "CAL003_BLIND_TECHNICAL_VALIDATION_V0_2")


if __name__ == "__main__":
    unittest.main()
