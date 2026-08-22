#!/usr/bin/env python3
"""文章レイヤーのデータを読み込み、アンカーを解決する。"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAYERS_DIR = ROOT / "_data" / "layers"
TYPES_FILE = ROOT / "_data" / "layer_types.json"
REQUIRED_ENTRY_KEYS = {"type", "anchor", "content"}
ALLOWED_POSITIONS = {"before", "after"}


class LayerError(ValueError):
    """検証可能なレイヤーデータの誤り。"""


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise LayerError(f"{path.relative_to(ROOT)}: JSONを読み込めません: {error}") from error


def markdown_text(source: str) -> str:
    """表示時の照合用に、最小限のMarkdown装飾を取り除く。"""
    source = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", source)
    source = re.sub(r"[`*_]", "", source)
    return source


def contextual_match_count(source: str, entry: dict) -> int:
    anchor = markdown_text(entry["anchor"])
    prefix = markdown_text(entry.get("prefix", ""))
    suffix = markdown_text(entry.get("suffix", ""))
    plain = markdown_text(source)
    count = 0
    start = 0
    while (index := plain.find(anchor, start)) != -1:
        before = plain[:index]
        after = plain[index + len(anchor) :]
        if (not prefix or before.endswith(prefix)) and (not suffix or after.startswith(suffix)):
            count += 1
        start = index + 1
    return count


def load_and_validate() -> tuple[dict, list[dict]]:
    errors: list[str] = []
    types = load_json(TYPES_FILE)
    if not isinstance(types, dict) or not types:
        raise LayerError("_data/layer_types.json: 1件以上の種別をオブジェクトで定義してください")
    for name, definition in types.items():
        if (
            not isinstance(name, str)
            or not isinstance(definition, dict)
            or not isinstance(definition.get("label"), str)
            or not definition["label"]
            or not isinstance(definition.get("color"), str)
            or not definition["color"]
        ):
            errors.append(f"_data/layer_types.json: {name!r}には空でないlabelとcolorを定義してください")

    documents: list[dict] = []
    targets: set[str] = set()
    for path in sorted(LAYERS_DIR.glob("*.json")):
        try:
            document = load_json(path)
            if not isinstance(document, dict):
                raise LayerError(f"{path.relative_to(ROOT)}: ルートはオブジェクトにしてください")
            target = document.get("target")
            entries = document.get("entries")
            if not isinstance(target, str) or not target.startswith("chapters/") or not target.endswith(".md"):
                raise LayerError(f"{path.relative_to(ROOT)}: targetにはchapters/*.mdを指定してください")
            target_path = ROOT / target
            if not target_path.is_file():
                raise LayerError(f"{path.relative_to(ROOT)}: 対象Markdownが存在しません: {target}")
            if target in targets:
                raise LayerError(f"{path.relative_to(ROOT)}: targetが別のレイヤーファイルと重複しています: {target}")
            targets.add(target)
            if not isinstance(entries, list) or not entries:
                raise LayerError(f"{path.relative_to(ROOT)}: entriesは1件以上の配列にしてください")
            source = target_path.read_text(encoding="utf-8")
            for index, entry in enumerate(entries):
                label = f"{path.relative_to(ROOT)}: entries[{index}]"
                if not isinstance(entry, dict):
                    errors.append(f"{label}: オブジェクトにしてください")
                    continue
                missing = REQUIRED_ENTRY_KEYS - entry.keys()
                if missing:
                    errors.append(f"{label}: 必須項目がありません: {', '.join(sorted(missing))}")
                    continue
                if any(not isinstance(entry[key], str) or not entry[key] for key in REQUIRED_ENTRY_KEYS):
                    errors.append(f"{label}: type、anchor、contentは空でない文字列にしてください")
                    continue
                if entry["type"] not in types:
                    errors.append(f"{label}: 未定義のtypeです: {entry['type']}")
                if any(key in entry and not isinstance(entry[key], str) for key in ("prefix", "suffix")):
                    errors.append(f"{label}: prefixとsuffixは文字列にしてください")
                    continue
                position = entry.get("position", "after")
                if position not in ALLOWED_POSITIONS:
                    errors.append(f"{label}: positionはbeforeまたはafterにしてください")
                count = contextual_match_count(source, entry)
                if count != 1:
                    errors.append(f"{label}: anchorの一致数は1件でなければなりません（実際: {count}件）")
            documents.append({"path": path, "target": target, "entries": entries})
        except LayerError as error:
            errors.append(str(error))
    if errors:
        raise LayerError("\n".join(errors))
    return types, documents
