#!/usr/bin/env python3
"""Jekyllの生成結果に文章レイヤーが埋め込まれたことを確認する。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--site-dir", type=Path, required=True)
args = parser.parse_args()

root = Path(__file__).resolve().parents[1]
site_dir = args.site_dir.resolve()

for layer_file in sorted((root / "_data/layers").glob("*.json")):
    document = json.loads(layer_file.read_text(encoding="utf-8"))
    output = site_dir / Path(document["target"]).with_suffix(".html")
    if not output.is_file():
        parser.error(f"Jekyllの生成ページが存在しません: {output}")

    page = output.read_text(encoding="utf-8")
    required_fragments = (
        '<script id="document-layer-data"',
        "../assets/js/layers.js",
        "../assets/css/layers.css",
    )
    for fragment in required_fragments:
        if fragment not in page:
            parser.error(f"{output}に {fragment} が存在しません")

    print(f"Jekyll生成後の文章レイヤーを確認しました: {output.relative_to(site_dir)}")
