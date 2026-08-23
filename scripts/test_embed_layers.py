#!/usr/bin/env python3
"""文章レイヤーの生成後埋め込みを、最小のHTMLで確認する。"""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EmbedLayersTest(unittest.TestCase):
    def run_embed(self, site: Path, *, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", "scripts/embed_layers.py", "--site-dir", str(site)],
            cwd=ROOT,
            check=check,
            capture_output=True,
            text=True,
        )

    def test_all_documents_receive_assets_and_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            layer_files = sorted((ROOT / "_data/layers").glob("*.json"))
            documents = [json.loads(path.read_text(encoding="utf-8")) for path in layer_files]
            for document in documents:
                output = site / Path(document["target"]).with_suffix(".html")
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text("<html><body><main>本文</main></body></html>", encoding="utf-8")
                design = site / Path(document["documentDesign"]).with_suffix(".html")
                design.parent.mkdir(parents=True, exist_ok=True)
                design.write_text("<html><body>設計メモ</body></html>", encoding="utf-8")

            self.run_embed(site)

            for document in documents:
                output = site / Path(document["target"]).with_suffix(".html")
                page = output.read_text(encoding="utf-8")
                self.assertIn('../assets/css/layers.css', page)
                self.assertIn('../assets/js/layers.js', page)
                start = page.index(">", page.index('id="document-layer-data"')) + 1
                end = page.index("</script>", start)
                payload = json.loads(page[start:end])
                self.assertEqual(document["entries"], payload["entries"])
                expected_design = "../" + str(
                    Path(document["documentDesign"]).with_suffix(".html")
                )
                self.assertEqual(expected_design, payload["metadata"]["documentDesign"])
                for definition in payload["types"].values():
                    self.assertRegex(definition["color"], r"^#[0-9a-fA-F]{6}$")
                    self.assertRegex(definition["darkColor"], r"^#[0-9a-fA-F]{6}$")

            second_run = self.run_embed(site, check=False)
            self.assertNotEqual(0, second_run.returncode)
            self.assertIn("文章レイヤーは既に埋め込まれています", second_run.stderr)


if __name__ == "__main__":
    unittest.main()
