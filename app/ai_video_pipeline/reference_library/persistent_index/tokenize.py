from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from .enums import TOKENIZER_CONTRACT_VERSION
from .errors import QueryError


NORMALIZATION_FORM = "NFKC"
UNICODE_RUNTIME_VERSION = unicodedata.unidata_version
MAX_QUERY_CHARACTERS = 512
MAX_QUERY_TERMS = 64
_FORBIDDEN_FTS_SYNTAX = frozenset('"*:^(){}[]~')
_RESERVED_OPERATORS = frozenset({"AND", "OR", "NOT", "NEAR"})


def _is_cjk(character: str) -> bool:
    value = ord(character)
    return (
        0x3400 <= value <= 0x4DBF
        or 0x4E00 <= value <= 0x9FFF
        or 0xF900 <= value <= 0xFAFF
        or 0x20000 <= value <= 0x2EBEF
        or 0x30000 <= value <= 0x323AF
    )


def _deduplicate(values: list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return tuple(result)


def prepared_token_sequence(text: str, *, index_unknown: bool = False) -> tuple[str, ...]:
    if not isinstance(text, str):
        raise TypeError("search text must be a string")
    normalized = unicodedata.normalize(NORMALIZATION_FORM, text).casefold()
    if normalized.strip().upper() == "UNKNOWN" and not index_unknown:
        return ()
    tokens: list[str] = []
    run: list[str] = []

    def flush_cjk() -> None:
        if not run:
            return
        if len(run) == 1:
            tokens.append(run[0])
        else:
            tokens.extend("".join(run[index : index + 2]) for index in range(len(run) - 1))
        run.clear()

    latin: list[str] = []

    def flush_latin() -> None:
        if latin:
            token = "".join(latin)
            if index_unknown or token != "unknown":
                tokens.append(token)
            latin.clear()

    for character in normalized:
        if _is_cjk(character):
            flush_latin()
            run.append(character)
        elif character.isalnum() or character == "_":
            flush_cjk()
            latin.append(character)
        else:
            flush_cjk()
            flush_latin()
    flush_cjk()
    flush_latin()
    return _deduplicate(tokens)


def prepare_document(text: str) -> str:
    return " ".join(prepared_token_sequence(text))


def _quoted(token: str) -> str:
    return '"' + token.replace('"', '""') + '"'


def prepare_match_query(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        raise QueryError("free-text query must be nonempty")
    if len(text) > MAX_QUERY_CHARACTERS:
        raise QueryError("free-text query is too long")
    if any(character in _FORBIDDEN_FTS_SYNTAX for character in text):
        raise QueryError("raw FTS syntax is forbidden")
    raw_words = re.findall(r"[A-Za-z]+", text)
    if any(word.upper() in _RESERVED_OPERATORS for word in raw_words):
        raise QueryError("FTS boolean operators are forbidden")
    tokens = prepared_token_sequence(text, index_unknown=True)
    if not tokens:
        raise QueryError("query contains no searchable token")
    if len(tokens) > MAX_QUERY_TERMS:
        raise QueryError("query contains too many terms")
    return " AND ".join(_quoted(token) for token in tokens)


@dataclass(frozen=True)
class TokenizerIdentity:
    contract_version: str = TOKENIZER_CONTRACT_VERSION
    normalization_form: str = NORMALIZATION_FORM
    unicode_runtime_version: str = UNICODE_RUNTIME_VERSION
    casefold: bool = True
    cjk_strategy: str = "OVERLAPPING_BIGRAM_WITH_SINGLETON_FALLBACK"

    def to_dict(self) -> dict[str, object]:
        return {
            "contract_version": self.contract_version,
            "normalization_form": self.normalization_form,
            "unicode_runtime_version": self.unicode_runtime_version,
            "casefold": self.casefold,
            "cjk_strategy": self.cjk_strategy,
        }


GOLDEN_TOKEN_FIXTURES = {
    "alpha beta": ("alpha", "beta"),
    "Alpha, BETA": ("alpha", "beta"),
    "\u539f\u795e\u52a8\u4f5c": ("\u539f\u795e", "\u795e\u52a8", "\u52a8\u4f5c"),
    "A\uff22\uff23 \u539f\u795e": ("abc", "\u539f\u795e"),
    "\u955c": ("\u955c",),
    "UNKNOWN": (),
}
