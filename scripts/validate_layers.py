#!/usr/bin/env python3
"""文章レイヤーをJekyllビルド前に検証する。"""

from layer_data import LayerError, load_and_validate


try:
    types, documents = load_and_validate()
except LayerError as error:
    print(f"文章レイヤーの検証に失敗しました:\n{error}")
    raise SystemExit(1)

entry_count = sum(len(document["entries"]) for document in documents)
print(f"文章レイヤーを検証しました: {len(types)}種別、{len(documents)}文書、{entry_count}エントリ")
