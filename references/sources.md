# 出典と裏付け対象

一次資料を中心に、「どの要件について、どの問題・設計・制約を確認する資料か」を記録する。RFCの状態、更新関係、参照箇所は本文執筆時にも再確認する。同じ資料は複数の要件に関係し得るが、未確認の対応は推測で追加しない。

## 拡張性と分散管理

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) | HOSTS.TXT方式で顕在化した問題、DNSの設計目標、名前空間・委譲・ゾーンによる分散管理 | 特に2章。従来方式の制約と新方式の狙いを確認する。1987年時点の仕様であり現在の規定とは分ける |
| [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) | 名前サーバーとリゾルバの実装、マスターファイルなど、分散したデータを提供・利用する仕組み | RFC 1034と一組で読む。後続RFCによる更新を確認する |
| [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) | ドメイン、ゾーン、委譲などを現行用語で区別する基準 | 歴史資料中の語と現行語を区別する。RFC 8499を廃止 |

## 性能、整合性、変更反映

| 資料 | 本書で裏付ける記述 | 問題・環境・トレードオフ |
| --- | --- | --- |
| [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) | リゾルバ、再帰・反復、キャッシュの基本概念 | 問い合わせと再利用が負荷を抑える一方、キャッシュされたコピーを生む |
| [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) | メッセージ形式、TTL、UDP/TCP利用、ゾーン転送 | 初期仕様として確認し、現在のトランスポート要件へ一般化しない |
| [RFC 1123: Requirements for Internet Hosts—Application and Support](https://www.rfc-editor.org/rfc/rfc1123.html) | Internet hostにおけるリゾルバ・トランスポート等の要求の補足 | 6.1節。RFC 1034/1035制定後の要求であり初期仕様と混同しない |
| [RFC 2181: Clarifications to the DNS Specification](https://www.rfc-editor.org/rfc/rfc2181.html) | TTL、データ順位、ゾーン境界などDNS仕様の明確化 | 「明確化」が初期実装すべての挙動を記述するとは限らない |

## セキュリティ

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 4033: DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033.html) | DNSSECの目的、能力、制約、導入要件 | 導入と脅威・非目標。機密性を提供する仕組みとは書かない |
| [RFC 4034: Resource Records for DNSSEC](https://www.rfc-editor.org/rfc/rfc4034.html) | DNSKEY、RRSIG、NSEC、DSの形式と意味 | レコード形式の根拠。後続更新を確認する |
| [RFC 4035: Protocol Modifications for DNSSEC](https://www.rfc-editor.org/rfc/rfc4035.html) | 署名生成、応答、検証、Authenticated Data等のプロトコル動作 | 検証状態と実装役割を一般化しすぎない |
| [RFC 5358: Preventing Use of Recursive Nameservers in Reflector Attacks](https://www.rfc-editor.org/rfc/rfc5358.html) | オープンな再帰サーバーが反射攻撃に利用される問題と、再帰サービスを許可先へ限定する推奨 | BCP 140。権威サービスと再帰サービスを区別する |

## プライバシー

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 7858: Specification for DNS over Transport Layer Security (TLS)](https://www.rfc-editor.org/rfc/rfc7858.html) | DoTの接続、認証、プライバシーに関する設計 | 後続の運用・プロファイル文書も確認する |
| [RFC 8484: DNS Queries over HTTPS (DoH)](https://www.rfc-editor.org/rfc/rfc8484.html) | HTTPSを用いるDNS問い合わせ・応答の形式とHTTP上の動作 | Web一般のHTTPS利用とDoHを同一視しない |
| [RFC 9250: DNS over Dedicated QUIC Connections](https://www.rfc-editor.org/rfc/rfc9250.html) | 専用QUIC接続を用いるDoQのプロトコル、ストリーム利用、接続上の考慮事項 | DoQの性能優位を条件なしに断定しない |

## 拡張性の章で追加確認する歴史資料

| 資料 | 確認する記述 | 状態 |
| --- | --- | --- |
| [RFC 810: DoD Internet Host Table Specification](https://www.rfc-editor.org/rfc/rfc810.html) | 集中したホスト表の取得・名前サービス移行の運用環境と制約 | TODO: 要検証 |
| [RFC 811: Hostnames Server](https://www.rfc-editor.org/rfc/rfc811.html) | HOSTS.TXTの登録・取得と、更新主体・配布工程 | TODO: 要検証 |
| [RFC 882: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc882.html) | 従来方式の制約と、階層化・分散管理が解決しようとした問題 | TODO: 要検証（RFC 1034により廃止） |
| [RFC 883: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc883.html) | 初期DNSが導入した運用上の役割とトレードオフ | TODO: 要検証（RFC 1035により廃止） |

## 出典管理上の未解決事項

- HOSTS.TXT以前の名前解決を説明する同時代資料を追加する。
- HOSTS.TXTの規模、更新頻度、転送負荷の数値を使う場合は、測定時点と一次資料を特定する。
- CDN、Anycast、クラウドDNSの章では、標準仕様だけでなく運用データの出典選定基準を定める。
- 各RFCの更新・訂正（Errata）を章の執筆開始時にRFC Editorで再確認する。
- 可用性、運用性、後方互換性の章に必要な一次資料は、各章の最初の執筆タスクで要件との対応を確認して追加する。
