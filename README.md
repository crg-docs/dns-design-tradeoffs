# DNSで学ぶ非機能要件――「DNS」と言わずに説明する

DNS（Domain Name System）という実在する大規模分散システムを題材に、非機能要件を設計判断へ変換する過程を学ぶ技術読み物です。DNSの歴史や仕様の網羅ではなく、要件を具体化し、設計がもたらす効果と代償を理解することを目指します。

**[GitHub Pagesで本書を読む](https://crg-docs.github.io/dns-design-tradeoffs/)**

## 目次

- [第0章 DNSはなぜ複雑に見えるのか](chapters/00-introduction.md)
- [第1章 見取り図――DNSは何を、いつ、なぜ足してきたか](chapters/01-timeline.md)
- [準備章 なぜ名前解決が必要なのか](chapters/01-name-resolution.md)（本文初稿、判定前）
- [第2章 拡張性――集中管理を分割する](chapters/02-scalability.md)（本文初稿、判定前）

現在は第0章と第1章が本文、準備章と第2章が本文初稿の判定前です。第3章以降の本文は、構成と出典を確認しながら小さな単位で追加します。

### 本書について

- [本書の狙いと、DNSを題材に選んだ理由](docs/concept.md)
- [全体構成案（第0〜10章）](docs/outline.md)
- [出典と、それが裏付ける記述](references/sources.md)

## 対象読者

- DNSの仕組みを、非機能要件と設計理由から理解したいエンジニア
- 可用性、性能、拡張性、整合性、セキュリティなどの要件を実例で学びたい人
- 分散システムの設計判断を、自分のシステムへ応用したい人

## 執筆方針

各テーマを「要件の定義 → 問題になる状況 → DNSの設計 → 歴史的背景 → 効果 → 制約と要件間の衝突 → 運用上の注意 → 他システムへの応用」の順で検討します。歴史は設計理由を理解するための補助線として扱います。歴史的事実と仕様は一次資料で裏付け、未確認事項は未確認であることを明記します。

## ディレクトリ構成

```text
README.md              プロジェクト案内
AGENTS.md              AIエージェント向け作業規約
docs/                  企画、構成、執筆規約、進行状況
chapters/              章の原稿と詳細構成案
references/sources.md  出典と、それが裏付ける記述の対応表
_data/layers/          本文の特定箇所に重ねる補助情報
```

### 制作用の資料

- [執筆スタイルガイド](docs/style-guide.md)
- [仕組みの分担表](docs/mechanism-map.md)
- [HOSTS.TXT期の一次資料からの抽出](references/hosts-txt-findings.md)
- [進行状況と各作業の終了条件](docs/progress.md)
- [文書ごとの構成意図と見送った案](docs/document-design/README.md)
- [AIエージェント向け執筆規約](AGENTS.md)
- [文章レイヤーのデータ形式と運用方法](docs/layers.md)
