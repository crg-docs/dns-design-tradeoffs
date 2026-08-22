# 文章レイヤー

文章レイヤーは、完成本文を変更せず、本文の特定箇所に結び付く作業情報や補足をGitHub Pages上で表示する仕組みです。`chapters/*.md` は読者向けの完成本文、`docs/document-design/` は文書全体の設計意図、`_data/layers/` は局所的な補助情報を担当します。文章レイヤーは設計メモを置き換えません。

## 構成

- `_data/layer_types.json`: 利用できる種別、表示名、表示色の定義
- `_data/layers/<章名>.json`: 対象章とエントリ
- `scripts/validate_layers.py`: データとアンカーの検証
- `scripts/embed_layers.py`: Jekyllの生成済みHTMLへページ分のデータを埋め込む処理
- `assets/js/layers.js`、`assets/css/layers.css`: ブラウザ上の表示

Primerのlayoutは複製しません。PagesのJekyllビルド後、デプロイ対象のHTMLだけへ既存の本文を変更せずにCSS、JavaScript、そのページに必要なJSONを追加します。JavaScriptが無効な場合は、従来どおり本文だけが表示されます。

## レイヤーファイルの書き方

```json
{
  "target": "chapters/02-scalability.md",
  "entries": [
    {
      "type": "research",
      "anchor": "本文中で一度だけ現れる文字列",
      "content": "表示する補助情報",
      "prefix": "必要な場合だけ指定する直前の文字列",
      "suffix": "必要な場合だけ指定する直後の文字列",
      "position": "after"
    }
  ]
}
```

`type`、`anchor`、`content` は必須です。`prefix` と `suffix` は短いアンカーを文脈で一意にする場合に使います。`position` は `after`（既定）または `before` を指定できます。Markdownの装飾記号を除いた文字列でも照合できるため、ブラウザでは対応する段落などの前後へ補助情報を挿入します。

種別を増やす場合は `_data/layer_types.json` に定義を追加します。表示コードと検証コードへ種別名を追加する必要はありません。

## 執筆と表示

本文にレイヤー専用のIDやコメントは書きません。補助情報を追加したら、`python3 scripts/validate_layers.py` で対象ファイル、種別、アンカーの一意性を確認します。

レイヤーがあるPagesでは、右上の「Layer」パネルから種別ごとに表示を切り替えられます。初期状態は本文のみです。「本文」をオフにすると補助情報を確認しやすい表示になりますが、本文ノード自体は書き換えません。

## 制約

アンカーは本文の文字列に依存するため、本文の改稿時に追随が必要です。CIは不一致を検出しますが、意味的に別の箇所へ偶然一意に一致した場合までは判定できません。長すぎない特徴的な文を選び、必要なら `prefix` と `suffix` を併用します。

基盤の実装後に残る表示確認と試験運用は、[`progress.md` の #23](progress.md#23-文章レイヤーの試験運用を完了する)で追跡します。
