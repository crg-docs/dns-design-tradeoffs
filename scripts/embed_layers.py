#!/usr/bin/env python3
"""生成済みJekyllページへ、そのページの文章レイヤーを埋め込む。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from layer_data import LayerError, load_and_validate


parser = argparse.ArgumentParser()
parser.add_argument("--site-dir", type=Path, required=True)
args = parser.parse_args()

try:
    types, documents = load_and_validate()
except LayerError as error:
    parser.error(str(error))

site_dir = args.site_dir.resolve()
for document in documents:
    output = site_dir / Path(document["target"]).with_suffix(".html")
    if not output.is_file():
        parser.error(f"Jekyllの生成ページが存在しません: {output}")
    page = output.read_text(encoding="utf-8")
    if "document-layer-data" in page:
        parser.error(f"文章レイヤーは既に埋め込まれています: {output}")
    payload = json.dumps(
        {"types": types, "entries": document["entries"]},
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")
    injection = (
        '\n<link rel="stylesheet" href="../assets/css/layers.css">\n'
        f'<script id="document-layer-data" type="application/json">{payload}</script>\n'
        '<script src="../assets/js/layers.js" defer></script>\n'
    )
    if "</body>" not in page:
        parser.error(f"body終了タグが見つかりません: {output}")
    output.write_text(page.replace("</body>", injection + "</body>", 1), encoding="utf-8")
    print(f"文章レイヤーを埋め込みました: {output.relative_to(site_dir)}")
