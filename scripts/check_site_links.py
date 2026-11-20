#!/usr/bin/env python3
"""生成サイトの内部リンク、フラグメント、ローカルアセットを検証する。"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, source: str):
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        attribute = "href" if tag in {"a", "link"} else "src" if tag in {"script", "img"} else None
        if attribute and attributes.get(attribute):
            self.links.append(attributes[attribute])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, required=True)
    parser.add_argument("--baseurl", default="/dns-design-tradeoffs")
    args = parser.parse_args()
    root = args.site_dir.resolve()
    prefix = "/" + args.baseurl.strip("/") + "/"
    origin = "https://site.invalid"
    pages = {p.resolve(): Page(p.read_text(encoding="utf-8")) for p in root.rglob("*.html")}
    if not pages:
        parser.error("生成HTMLがありません")
    failures = []
    for path, page in pages.items():
        source_url = origin + prefix + path.relative_to(root).as_posix()
        for link in page.links:
            url = urlsplit(urljoin(source_url, link))
            if url.scheme not in {"http", "https"} or url.netloc != "site.invalid":
                continue
            decoded_path = unquote(url.path)
            if not decoded_path.startswith(prefix):
                failures.append(f"{path.relative_to(root)}: baseurl外へのリンク: {link}")
                continue
            target = (root / decoded_path[len(prefix):]).resolve()
            if not target.is_relative_to(root):
                failures.append(f"{path.relative_to(root)}: サイト外へのリンク: {link}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                failures.append(f"{path.relative_to(root)}: 参照先がありません: {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                failures.append(f"{path.relative_to(root)}: アンカーがありません: {link}")
    if failures:
        parser.error("\n".join(failures))
    print(f"内部リンクとアセットを検証しました: {len(pages)}ページ、リンク切れ0件")


if __name__ == "__main__":
    main()
