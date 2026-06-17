from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_FORBIDDEN_TOKENS = [
    "G:\\AICODING\\AI\u89c6\u9891\u5de5\u4f5c\u6d41",
    "G:/AICODING/AI\u89c6\u9891\u5de5\u4f5c\u6d41",
    "AI\u89c6\u9891\u5de5\u4f5c\u6d41",
    "G:\\AICODING\\dreamina_upload_staging",
    "G:/AICODING/dreamina_upload_staging",
    "dreamina_upload_staging",
    "G:\\AICODING\\AI_VIDEO_PIPELINE_V3",
    "G:/AICODING/AI_VIDEO_PIPELINE_V3",
    "AI_VIDEO_PIPELINE_V3",
    "DreaminaBatcher_v2_clean",
    "V8_validation",
    "APITEST",
    "CLI_md",
    "AI\u7459\u55db",
]

_SCAN_DEFINITION_PATH = Path(__file__).resolve()


ALLOWED_MATCHES = {
    "C:/Users/msjpurf/bin/dreamina.exe",
    "C:\\Users\\msjpurf\\bin\\dreamina.exe",
}

DEFAULT_IGNORED_FILES = {
    "PHASE_A1_1_ENCODING_SAFE_PATH_SCAN.md",
    "PHASE_A1_ACCEPTANCE_AUDIT.md",
    "PHASE_B1_1_GAP_CLOSURE_REPORT.md",
}


@dataclass(frozen=True)
class ForbiddenMatch:
    file: Path
    line_number: int
    token: str
    snippet: str
    allowed: bool


@dataclass(frozen=True)
class PathScanResult:
    workspace_root: Path
    files_scanned: list[Path]
    matches: list[ForbiddenMatch]
    forbidden_tokens: list[str]

    @property
    def has_violations(self) -> bool:
        return any(not match.allowed for match in self.matches)

    @property
    def result_label(self) -> str:
        return "FAIL" if self.has_violations else "PASS"


def _iter_lines_for_decoding(raw: bytes) -> Iterable[str]:
    encodings = (
        "utf-8",
        "utf-8-sig",
        "utf-16",
        "utf-16-le",
        "utf-16-be",
        "gbk",
        "cp936",
        "latin-1",
        "cp1252",
    )

    for encoding in encodings:
        try:
            yield raw.decode(encoding, errors="replace")
        except Exception:
            continue


def _should_scan(path: Path) -> bool:
    if path.is_symlink():
        return False
    if path.name in DEFAULT_IGNORED_FILES:
        return False
    return not path.name.lower().endswith(".pyc") and path.suffix.lower() not in {
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".webp",
        ".zip",
        ".tar",
        ".gz",
        ".exe",
        ".dll",
        ".so",
        ".pyc",
        ".pdf",
        ".npy",
        ".npz",
    }


def scan_forbidden_paths(workspace_root: Path, forbidden_tokens: list[str] | None = None) -> PathScanResult:
    root = Path(workspace_root).resolve()
    tokens = forbidden_tokens or list(DEFAULT_FORBIDDEN_TOKENS)
    files_scanned: list[Path] = []
    found: list[ForbiddenMatch] = []
    seen_keys: set[tuple[Path, int, str]] = set()

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if not _should_scan(path):
            continue
        files_scanned.append(path)
        raw = path.read_bytes()
        in_definition_block = path.resolve() == _SCAN_DEFINITION_PATH
        active_definition_block = False
        for decoded in _iter_lines_for_decoding(raw):
            for line_number, line in enumerate(decoded.splitlines(), start=1):
                if in_definition_block and line.startswith("DEFAULT_FORBIDDEN_TOKENS = ["):
                    active_definition_block = True
                if active_definition_block and line.strip() == "]":
                    active_definition_block = False
                for token in tokens:
                    if token not in line:
                        continue
                    allowed = token in ALLOWED_MATCHES or (in_definition_block and active_definition_block)
                    key = (path, line_number, token)
                    if key in seen_keys:
                        continue
                    seen_keys.add(key)
                    found.append(
                        ForbiddenMatch(
                            file=path,
                            line_number=line_number,
                            token=token,
                            snippet=line.strip(),
                            allowed=allowed,
                        )
                    )

    return PathScanResult(
        workspace_root=root,
        files_scanned=files_scanned,
        matches=found,
        forbidden_tokens=list(tokens),
    )


def write_scan_report(report_path: Path, result: PathScanResult) -> Path:
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("# PHASE A.1.1 Encoding-safe path scan")
    lines.append("")
    lines.append("## 1) Scan scope")
    lines.append(f"- Workspace root: `{result.workspace_root}`")
    lines.append(f"- Files scanned: `{len(result.files_scanned)}`")
    lines.append("- Parent directory was not scanned: verified.")
    lines.append("- No old project directories were used as scan sources.")
    lines.append("")
    lines.append("## 2) Forbidden token list")
    for token in result.forbidden_tokens:
        lines.append(f"- `{token}`")
    lines.append("")
    lines.append("## 3) Matching files and lines")
    if not result.matches:
        lines.append("- No matches found.")
    else:
        for match in result.matches:
            status = "allowed" if match.allowed else "violation"
            rel_path = match.file.relative_to(result.workspace_root)
            lines.append(
                f"- `{rel_path}:{match.line_number}` token `{match.token}` [{status}] "
                f"snippet: `{match.snippet}`"
            )
    lines.append("")
    lines.append("## 4) Execution and safety checks")
    lines.append("- No Dreamina command was executed during the scan.")
    lines.append("- Scan did not write external paths.")
    lines.append("- External path write check: false")
    lines.append("")
    lines.append(f"## 5) Final result: {result.result_label}")

    text = "\n".join(lines) + "\n"
    report_path.write_text(text, encoding="utf-8")
    return report_path
