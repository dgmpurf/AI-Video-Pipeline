from __future__ import annotations

from dataclasses import asdict, dataclass, fields
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Mapping, Sequence
import hashlib
import json
import math
import re
import struct


IMPLEMENTATION_VERSION = "CAL003_BLIND_TECHNICAL_VALIDATION_V0_2"
MAX_SAFE_STRING_LENGTH = 160
MAX_SAFE_LIST_LENGTH = 16
MAX_DURATION_TEXT_LENGTH = 64
TARGET_SIZE_BYTES = 4_194_304
EXPECTED_DURATION = Decimal("5.085011")
DURATION_TOLERANCE = Decimal("0.000001")
DURATION_EXPECTED_EVIDENCE = "5.085011\u00b10.000001"

EXECUTION_PHASES = (
    "PREFLIGHT",
    "REMUX",
    "PADDING",
    "FILE_CONTRACT",
    "FFPROBE_PROCESS",
    "FFPROBE_PARSE",
    "STREAM_CONTRACT",
    "VIDEO_CONTRACT",
    "METADATA_CONTRACT",
    "FULL_DECODE",
    "VIDEO_EQUIVALENCE",
    "AUDIO_EQUIVALENCE",
    "GLOBAL_HASH_CHECKS",
    "COMPLETE",
)


class SafeTechnicalValueError(Exception):
    """Signals an unsafe structured value without retaining its payload."""


@dataclass(frozen=True)
class CheckSpec:
    ordinal: int
    check_code: str
    execution_phase: str
    expected: object


CHECK_CATALOG = (
    CheckSpec(1, "FILE_PRESENT", "FILE_CONTRACT", True),
    CheckSpec(2, "FILE_REGULAR", "FILE_CONTRACT", True),
    CheckSpec(3, "FILE_NONEMPTY", "FILE_CONTRACT", True),
    CheckSpec(4, "TARGET_SIZE_EXACT", "FILE_CONTRACT", TARGET_SIZE_BYTES),
    CheckSpec(5, "TOP_LEVEL_FREE_BOX_VALID", "FILE_CONTRACT", True),
    CheckSpec(6, "FFPROBE_JSON_PARSE", "FFPROBE_PARSE", True),
    CheckSpec(7, "CONTAINER_MP4", "STREAM_CONTRACT", True),
    CheckSpec(8, "VIDEO_STREAM_COUNT", "STREAM_CONTRACT", 1),
    CheckSpec(9, "AUDIO_STREAM_COUNT", "STREAM_CONTRACT", 1),
    CheckSpec(10, "OTHER_STREAM_COUNT", "STREAM_CONTRACT", 0),
    CheckSpec(11, "CODEC_H264", "VIDEO_CONTRACT", "h264"),
    CheckSpec(12, "PIXEL_FORMAT_YUV420P", "VIDEO_CONTRACT", "yuv420p"),
    CheckSpec(13, "WIDTH_1280", "VIDEO_CONTRACT", 1280),
    CheckSpec(14, "HEIGHT_720", "VIDEO_CONTRACT", 720),
    CheckSpec(
        15,
        "DURATION_5_085011",
        "VIDEO_CONTRACT",
        DURATION_EXPECTED_EVIDENCE,
    ),
    CheckSpec(16, "ROTATION_ZERO", "VIDEO_CONTRACT", 0),
    CheckSpec(17, "FRAME_EVIDENCE_121", "VIDEO_CONTRACT", 121),
    CheckSpec(18, "METADATA_SAFETY", "METADATA_CONTRACT", 0),
    CheckSpec(19, "FULL_DECODE_PASS", "FULL_DECODE", True),
    CheckSpec(20, "VIDEO_FRAMEMD5_EQUIVALENCE", "VIDEO_EQUIVALENCE", True),
    CheckSpec(21, "AUDIO_FRAMEMD5_EQUIVALENCE", "AUDIO_EQUIVALENCE", True),
    CheckSpec(22, "HASH_UNIQUE_AMONG_DIAGNOSTIC_OUTPUTS", "GLOBAL_HASH_CHECKS", True),
    CheckSpec(23, "HASH_DIFFERS_FROM_ALL_CANONICAL_MEDIA", "GLOBAL_HASH_CHECKS", True),
)
CHECK_CODES = tuple(spec.check_code for spec in CHECK_CATALOG)
CHECK_BY_CODE = {spec.check_code: spec for spec in CHECK_CATALOG}

FORBIDDEN_METADATA_MARKERS = (
    "r1_download",
    "push_01",
    "push-01",
    "push_02",
    "push-02",
    "push_03",
    "push-03",
    "impact_01",
    "impact-01",
    "impact_02",
    "impact-02",
    "impact_03",
    "impact-03",
    "action_ref",
    "submit_id",
    "reference_id",
    "experiments/cal-003/reference_control_repeatability_v1/r1_download",
)
WINDOWS_ABSOLUTE_PATH = re.compile(r"(?i)(?:^|[^a-z0-9])[a-z]:[\\/]")


def parse_finite_decimal_text(value: object) -> Decimal:
    if not isinstance(value, str) or not value or len(value) > MAX_DURATION_TEXT_LENGTH:
        raise SafeTechnicalValueError()
    try:
        parsed = Decimal(value)
    except InvalidOperation:
        raise SafeTechnicalValueError() from None
    if not parsed.is_finite():
        raise SafeTechnicalValueError()
    return parsed


def duration_difference_text(observed_text: object) -> str:
    observed = parse_finite_decimal_text(observed_text)
    return format(abs(observed - EXPECTED_DURATION), "f")


def duration_within_tolerance(observed_text: object) -> bool:
    observed = parse_finite_decimal_text(observed_text)
    difference = abs(observed - EXPECTED_DURATION)
    return difference <= DURATION_TOLERANCE


def _normalize_safe_scalar(value: object) -> object:
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise TypeError("unsafe scalar")
        return value
    if isinstance(value, str):
        if len(value) > MAX_SAFE_STRING_LENGTH:
            raise TypeError("unsafe scalar")
        return value
    if isinstance(value, (list, tuple)):
        if len(value) > MAX_SAFE_LIST_LENGTH:
            raise TypeError("unsafe scalar")
        normalized = []
        for item in value:
            if isinstance(item, (list, tuple, dict, bytes, bytearray, Path)):
                raise TypeError("unsafe scalar")
            normalized.append(_normalize_safe_scalar(item))
        return tuple(normalized)
    raise TypeError("unsafe scalar")


def is_safe_scalar(value: object) -> bool:
    try:
        _normalize_safe_scalar(value)
    except TypeError:
        return False
    return True


def safe_scalar_to_json(value: object) -> object:
    normalized = _normalize_safe_scalar(value)
    if isinstance(normalized, tuple):
        return list(normalized)
    return normalized


@dataclass(frozen=True)
class CheckResult:
    check_code: str
    result: bool
    expected: object
    observed: object
    execution_phase: str

    def __post_init__(self) -> None:
        if self.check_code not in CHECK_BY_CODE:
            raise ValueError("unknown check code")
        if not isinstance(self.result, bool):
            raise TypeError("result must be boolean")
        if self.execution_phase not in EXECUTION_PHASES:
            raise ValueError("unknown execution phase")
        object.__setattr__(self, "expected", _normalize_safe_scalar(self.expected))
        object.__setattr__(self, "observed", _normalize_safe_scalar(self.observed))

    def to_dict(self) -> dict[str, object]:
        return {
            "check_code": self.check_code,
            "execution_phase": self.execution_phase,
            "expected": safe_scalar_to_json(self.expected),
            "observed": safe_scalar_to_json(self.observed),
            "result": self.result,
        }


@dataclass(frozen=True)
class TechnicalValidationError:
    error_class: str
    execution_phase: str
    check_code: str
    expected: object
    observed: object
    local_safety_failure: bool

    def __post_init__(self) -> None:
        if len(self.error_class) > MAX_SAFE_STRING_LENGTH:
            raise ValueError("error class too long")
        if self.execution_phase not in EXECUTION_PHASES:
            raise ValueError("unknown execution phase")
        if self.check_code not in CHECK_BY_CODE:
            raise ValueError("unknown check code")
        if not isinstance(self.local_safety_failure, bool):
            raise TypeError("local safety flag must be boolean")
        object.__setattr__(self, "expected", _normalize_safe_scalar(self.expected))
        object.__setattr__(self, "observed", _normalize_safe_scalar(self.observed))

    def to_dict(self) -> dict[str, object]:
        return {
            "check_code": self.check_code,
            "error_class": self.error_class,
            "execution_phase": self.execution_phase,
            "expected": safe_scalar_to_json(self.expected),
            "local_safety_failure": self.local_safety_failure,
            "observed": safe_scalar_to_json(self.observed),
        }


@dataclass(frozen=True)
class ProbeFacts:
    format_is_mp4: bool
    video_stream_count: int
    audio_stream_count: int
    other_stream_count: int
    codec: str
    pixel_format: str
    width: int
    height: int
    duration_text: str
    rotation: int
    frame_evidence: int
    forbidden_metadata_marker_count: int
    safe_metadata_key_count: int

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class Framemd5Comparison:
    source_record_count: int
    diagnostic_record_count: int
    equivalent: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


class _StructuredParseFailure(Exception):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _StructuredParseFailure()
        result[key] = value
    return result


def _reject_nonfinite_constant(_: str) -> None:
    raise _StructuredParseFailure()


def parse_ffprobe_bytes(
    raw: bytes,
) -> tuple[ProbeFacts | None, TechnicalValidationError | None]:
    try:
        text = raw.decode("utf-8", errors="strict")
        payload = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, _StructuredParseFailure):
        return None, TechnicalValidationError(
            error_class="FFPROBE_JSON_PARSE_ERROR",
            execution_phase="FFPROBE_PARSE",
            check_code="FFPROBE_JSON_PARSE",
            expected=True,
            observed=False,
            local_safety_failure=True,
        )
    try:
        return probe_facts_from_object(payload), None
    except SafeTechnicalValueError:
        return None, TechnicalValidationError(
            error_class="DURATION_DECIMAL_TEXT_ERROR",
            execution_phase="VIDEO_CONTRACT",
            check_code="DURATION_5_085011",
            expected=DURATION_EXPECTED_EVIDENCE,
            observed="invalid_decimal_text",
            local_safety_failure=True,
        )
    except _StructuredParseFailure:
        return None, TechnicalValidationError(
            error_class="FFPROBE_STRUCTURE_ERROR",
            execution_phase="FFPROBE_PARSE",
            check_code="FFPROBE_JSON_PARSE",
            expected=True,
            observed=False,
            local_safety_failure=True,
        )


def _safe_short_string(value: object, *, missing: str = "missing") -> str:
    if value is None:
        return missing
    if not isinstance(value, str) or len(value) > MAX_SAFE_STRING_LENGTH:
        raise _StructuredParseFailure()
    return value


def _safe_int(value: object, *, missing: int = -1) -> int:
    if value is None:
        return missing
    if isinstance(value, bool):
        raise _StructuredParseFailure()
    if isinstance(value, int):
        return value
    if isinstance(value, str) and re.fullmatch(r"[+-]?\d+", value):
        return int(value)
    raise _StructuredParseFailure()


def _rotation_from_stream(stream: Mapping[str, object]) -> int:
    values: list[int] = []
    tags = stream.get("tags")
    if tags is not None:
        if not isinstance(tags, dict):
            raise _StructuredParseFailure()
        if "rotate" in tags:
            values.append(_safe_int(tags["rotate"]))
    side_data = stream.get("side_data_list")
    if side_data is not None:
        if not isinstance(side_data, list):
            raise _StructuredParseFailure()
        for item in side_data:
            if not isinstance(item, dict):
                raise _StructuredParseFailure()
            if "rotation" in item:
                values.append(_safe_int(item["rotation"]))
    if not values:
        return 0
    normalized = {0 if value == 0 else value for value in values}
    if len(normalized) != 1:
        raise _StructuredParseFailure()
    return values[0]


def _metadata_counts(
    format_object: Mapping[str, object],
    streams: Sequence[Mapping[str, object]],
) -> tuple[int, int]:
    values: list[str] = []
    key_count = 0
    for owner in (format_object, *streams):
        tags = owner.get("tags")
        if tags is None:
            continue
        if not isinstance(tags, dict):
            raise _StructuredParseFailure()
        for key, value in tags.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise _StructuredParseFailure()
            if len(key) > MAX_SAFE_STRING_LENGTH or len(value) > 4096:
                raise _StructuredParseFailure()
            key_count += 1
            values.append(value)
    forbidden_count = 0
    for value in values:
        lowered = value.replace("\\", "/").lower()
        if WINDOWS_ABSOLUTE_PATH.search(value) or any(
            marker in lowered for marker in FORBIDDEN_METADATA_MARKERS
        ):
            forbidden_count += 1
    return forbidden_count, key_count


def probe_facts_from_object(payload: object) -> ProbeFacts:
    if not isinstance(payload, dict):
        raise _StructuredParseFailure()
    format_object = payload.get("format")
    streams_object = payload.get("streams")
    if not isinstance(format_object, dict) or not isinstance(streams_object, list):
        raise _StructuredParseFailure()
    streams: list[Mapping[str, object]] = []
    for stream in streams_object:
        if not isinstance(stream, dict):
            raise _StructuredParseFailure()
        streams.append(stream)

    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    other_streams = [
        stream
        for stream in streams
        if stream.get("codec_type") not in ("video", "audio")
    ]
    video = video_streams[0] if video_streams else {}
    format_name = _safe_short_string(format_object.get("format_name"))
    format_tokens = {token.strip().lower() for token in format_name.split(",")}
    duration_text = format_object.get("duration")
    parse_finite_decimal_text(duration_text)
    codec = _safe_short_string(video.get("codec_name"))
    pixel_format = _safe_short_string(video.get("pix_fmt"))
    width = _safe_int(video.get("width"))
    height = _safe_int(video.get("height"))
    frame_evidence = _safe_int(
        video.get("nb_read_frames", video.get("nb_frames"))
    )
    rotation = _rotation_from_stream(video)
    forbidden_count, key_count = _metadata_counts(format_object, streams)
    return ProbeFacts(
        format_is_mp4="mp4" in format_tokens,
        video_stream_count=len(video_streams),
        audio_stream_count=len(audio_streams),
        other_stream_count=len(other_streams),
        codec=codec,
        pixel_format=pixel_format,
        width=width,
        height=height,
        duration_text=duration_text,
        rotation=rotation,
        frame_evidence=frame_evidence,
        forbidden_metadata_marker_count=forbidden_count,
        safe_metadata_key_count=key_count,
    )


def probe_observations(facts: ProbeFacts) -> dict[str, object]:
    return {
        "FFPROBE_JSON_PARSE": True,
        "CONTAINER_MP4": facts.format_is_mp4,
        "VIDEO_STREAM_COUNT": facts.video_stream_count,
        "AUDIO_STREAM_COUNT": facts.audio_stream_count,
        "OTHER_STREAM_COUNT": facts.other_stream_count,
        "CODEC_H264": facts.codec,
        "PIXEL_FORMAT_YUV420P": facts.pixel_format,
        "WIDTH_1280": facts.width,
        "HEIGHT_720": facts.height,
        "DURATION_5_085011": facts.duration_text,
        "ROTATION_ZERO": facts.rotation,
        "FRAME_EVIDENCE_121": facts.frame_evidence,
        "METADATA_SAFETY": facts.forbidden_metadata_marker_count,
    }


def _check_passes(check_code: str, expected: object, observed: object) -> bool:
    if check_code == "DURATION_5_085011":
        try:
            return duration_within_tolerance(observed)
        except SafeTechnicalValueError:
            return False
    return observed == expected


def evaluate_check(check_code: str, observed: object) -> CheckResult:
    spec = CHECK_BY_CODE[check_code]
    safe_observed = observed
    if check_code == "DURATION_5_085011":
        try:
            parse_finite_decimal_text(observed)
        except SafeTechnicalValueError:
            safe_observed = "invalid_decimal_text"
    return CheckResult(
        check_code=check_code,
        result=_check_passes(check_code, spec.expected, observed),
        expected=spec.expected,
        observed=safe_observed,
        execution_phase=spec.execution_phase,
    )


def evaluate_ordered_observations(
    observations: Mapping[str, object],
    *,
    include_global: bool = False,
) -> tuple[CheckResult, ...]:
    results: list[CheckResult] = []
    for spec in CHECK_CATALOG:
        if spec.ordinal >= 22 and not include_global:
            continue
        if spec.check_code not in observations:
            break
        result = evaluate_check(spec.check_code, observations[spec.check_code])
        results.append(result)
        if not result.result:
            break
    return tuple(results)


def first_failed_check(results: Sequence[CheckResult]) -> CheckResult | None:
    return next((result for result in results if not result.result), None)


def unevaluated_check_codes(
    results: Sequence[CheckResult],
    *,
    include_global: bool = False,
) -> tuple[str, ...]:
    evaluated = {result.check_code for result in results}
    return tuple(
        spec.check_code
        for spec in CHECK_CATALOG
        if (include_global or spec.ordinal <= 21) and spec.check_code not in evaluated
    )


def file_contract_observations(
    path: Path,
    target_size: int = TARGET_SIZE_BYTES,
) -> dict[str, object]:
    exists = path.exists()
    regular = path.is_file()
    size = path.stat().st_size if regular else 0
    return {
        "FILE_PRESENT": exists,
        "FILE_REGULAR": regular,
        "FILE_NONEMPTY": size > 0,
        "TARGET_SIZE_EXACT": size,
        "TOP_LEVEL_FREE_BOX_VALID": (
            top_level_free_box_valid(path, target_size) if regular else False
        ),
    }


def top_level_free_box_valid(
    path: Path,
    target_size: int = TARGET_SIZE_BYTES,
) -> bool:
    try:
        total_size = path.stat().st_size
        if total_size != target_size:
            return False
        offset = 0
        last_type = b""
        last_size = 0
        with path.open("rb") as handle:
            while offset < total_size:
                handle.seek(offset)
                header = handle.read(8)
                if len(header) != 8:
                    return False
                size32, box_type = struct.unpack(">I4s", header)
                header_size = 8
                if size32 == 1:
                    extended = handle.read(8)
                    if len(extended) != 8:
                        return False
                    box_size = struct.unpack(">Q", extended)[0]
                    header_size = 16
                elif size32 == 0:
                    box_size = total_size - offset
                else:
                    box_size = size32
                if box_size < header_size or offset + box_size > total_size:
                    return False
                last_type = box_type
                last_size = box_size
                offset += box_size
        return offset == total_size and last_type == b"free" and last_size >= 8
    except (OSError, OverflowError, struct.error):
        return False


def normalize_framemd5(raw: bytes) -> bytes:
    text = raw.decode("utf-8", errors="strict").replace("\r\n", "\n")
    records = [
        line
        for line in text.split("\n")
        if line and not line.lstrip().startswith("#")
    ]
    return "\n".join(records).encode("utf-8")


def compare_framemd5(source_raw: bytes, diagnostic_raw: bytes) -> Framemd5Comparison:
    source = normalize_framemd5(source_raw)
    diagnostic = normalize_framemd5(diagnostic_raw)
    return Framemd5Comparison(
        source_record_count=0 if not source else source.count(b"\n") + 1,
        diagnostic_record_count=0 if not diagnostic else diagnostic.count(b"\n") + 1,
        equivalent=source == diagnostic,
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hashes_are_unique(hashes: Sequence[str]) -> bool:
    return len(hashes) == len(set(hashes))


def hashes_differ_from_canonical(
    diagnostic_hashes: Sequence[str],
    canonical_hashes: Sequence[str],
) -> bool:
    return set(diagnostic_hashes).isdisjoint(canonical_hashes)


def model_field_names(model: type[object]) -> tuple[str, ...]:
    return tuple(field.name for field in fields(model))
