# 出典と裏付け対象

一次資料を中心に、「どの要件について、どの問題・設計・制約を確認する資料か」を記録する。RFCの状態、更新関係、参照箇所は本文執筆時にも再確認する。同じ資料は複数の要件に関係し得るが、未確認の対応は推測で追加しない。

## 拡張性と分散管理

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) | HOSTS.TXT方式で顕在化した問題、DNSの設計目標、名前空間・委譲・ゾーンによる分散管理 | 特に2章。従来方式の制約と新方式の狙いを確認する。1987年11月、STD 13。RFC 882/883/973を廃止。19件のRFCが更新しており、1987年時点の規定を現在の規定として扱わない |
| [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) | 名前サーバーとリゾルバの実装、マスターファイルなど、分散したデータを提供・利用する仕組み | RFC 1034と一組で読む。1987年11月、STD 13。29件のRFCが更新しており、本書の論点に関わる更新（RFC 2181、2308、4033〜4035、5936、7766、8767）は該当章で個別に確認する |
| [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) | ドメイン、ゾーン、委譲などを現行用語で区別する基準 | 歴史資料中の語と現行語を区別する。2024年、BCP 219。RFC 8499を廃止し、RFC 2308を更新（Negative Cache関連の用語は本文書の定義を優先する） |

## 性能、整合性、変更反映

| 資料 | 本書で裏付ける記述 | 問題・環境・トレードオフ |
| --- | --- | --- |
| [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) | リゾルバ、再帰・反復、キャッシュの基本概念 | 問い合わせと再利用が負荷を抑える一方、キャッシュされたコピーを生む |
| [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) | メッセージ形式、TTL、UDP/TCP利用、ゾーン転送 | 初期仕様として確認し、現在のトランスポート要件へ一般化しない |
| [RFC 1123: Requirements for Internet Hosts—Application and Support](https://www.rfc-editor.org/rfc/rfc1123.html) | Internet hostにおけるリゾルバ・トランスポート等の要求の補足 | 6.1節「DOMAIN NAME TRANSLATION」。1989年10月、STD 3。RFC 1034/1035制定後の要求であり初期仕様と混同しない。RFC 2181、5966、7766、9210が更新している |
| [RFC 2181: Clarifications to the DNS Specification](https://www.rfc-editor.org/rfc/rfc2181.html) | TTL、データ順位、ゾーン境界などDNS仕様の明確化 | 「明確化」が初期実装すべての挙動を記述するとは限らない |

## 可用性と障害耐性

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 8767: Serving Stale Data to Improve DNS Resiliency](https://www.rfc-editor.org/rfc/rfc8767.html) | 権威サーバーへ到達できないとき、期限切れのキャッシュデータを返して応答を継続する設計。第0章の「障害中に古い情報を返す判断」の裏付け | 2020年、Proposed Standard。RFC 1034/1035/2181を更新し、TTL満了後のデータ利用を例外的な状況に限って認める。可用性と最新性を交換する選択として扱い、常時の挙動と混同しない。滞留時間の上限値や推奨タイマーを本文へ引く場合は TODO: 要検証 |

## セキュリティ

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 4033: DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033.html) | DNSSECの目的、能力、制約、導入要件 | 導入と脅威・非目標。2005年3月、RFC 6014と6840が更新。4章に非目標が明示されており（機密性、アクセス制御、DoS耐性を提供しない）、機密性を提供する仕組みとは書かない |
| [RFC 4034: Resource Records for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4034.html) | DNSKEY、RRSIG、NSEC、DSの形式と意味 | レコード形式の根拠。2005年3月。RFC 4470、6014、6840、6944、9077、9824、9905が更新しており、アルゴリズムとNSECの扱いは更新後を確認する |
| [RFC 4035: Protocol Modifications for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4035.html) | 署名生成、応答、検証、Authenticated Data等のプロトコル動作 | 検証状態と実装役割を一般化しすぎない。2005年3月。RFC 4470、6014、6840、8198、9077、9520、9824が更新している |
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
| [RFC 606: Host Names On-line](https://www.rfc-editor.org/rfc/rfc606.html) | HOSTS.TXT以前の状態。公式の一覧はあったが機械可読でなく、各サイトが自前の表を手で維持し互いに食い違っていたこと | 実読済み（2026-08-05）。1973年12月、Legacy Stream。同時代の一人称記録であり回顧ではない。**集中管理がより悪い分散状態への対処だった**ことを示す中心資料 |
| [RFC 608: Host Names On-Line](https://www.rfc-editor.org/rfc/rfc608.html) | NICが機械可読の一覧を定期生成する体制を引き受けた経緯。更新が週次のバッチ生成として想定されていたこと | 実読済み（2026-08-05）。1974年1月、RFC 810により廃止 |
| [RFC 810: DoD Internet Host Table Specification](https://www.rfc-editor.org/rfc/rfc810.html) | 登録工程（名前を使う前にNICと交渉して登録する。連絡手段に電話番号が併記）、取得工程（FTPで匿名取得）、変換は利用者の責任 | 実読済み（2026-08-05）。ASSUMPTIONS 第6項・第7項。1982年3月。RFC 608を廃止し、RFC 952により廃止 |
| [RFC 811: Hostnames Server](https://www.rfc-editor.org/rfc/rfc811.html) | HOSTS.TXTの登録・取得と、更新主体・配布工程 | TODO: 要検証（1982年3月。RFC 953により廃止） |
| [RFC 921: Domain Name System Implementation Schedule - Revised](https://www.rfc-editor.org/rfc/rfc921.html) | 移行期の具体的な互換措置。旧名に `.ARPA` を付けたものを新しい名前とする制約、DHOSTS.TXTによる新旧二重提供、平坦な名前空間から階層への一意性の移し替え | 実読済み（2026-08-05）。1984年10月、IABとDARPAの公式方針。RFC 897とRFC 881を更新。**予定が守られなかったことを当事者が記録している**ため第9章でも使う |
| [RFC 952: DoD Internet Host Table Specification](https://www.rfc-editor.org/rfc/rfc952.html) | HOSTS.TXT期後半のホスト表仕様。ホスト名の書式規則と、役割を名前に埋め込む規約（-GATEWAY、-GW） | 実読済み（2026-08-05）。1985年10月。RFC 608/810を廃止。廃止されておらずRFC 1123が更新しているため、「DNS以前の仕様」として過去形で扱わない |
| [RFC 953: Hostname Server](https://www.rfc-editor.org/rfc/rfc953.html) | ホスト表の配布・取得サービスの後期仕様 | TODO: 要検証（1985年10月。RFC 811を廃止。現在はHistoric） |
| [RFC 882: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc882.html) | 従来方式の制約と、階層化・分散管理が解決しようとした問題 | TODO: 要検証（1983年11月。RFC 973が更新、RFC 1034/1035により廃止） |
| [RFC 883: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc883.html) | 初期DNSが導入した運用上の役割とトレードオフ | TODO: 要検証（1983年11月。RFC 973が更新、RFC 1034/1035により廃止） |

## 出典管理上の未解決事項

- HOSTS.TXT以前の名前解決を説明する同時代資料は追加済み（RFC 606、2026-08-05）。抽出結果は [HOSTS.TXT期の一次資料からの抽出](hosts-txt-findings.md) にある。未読で残しているのは RFC 597（RFC 606が参照する公式ホスト名一覧）、RFC 881・897（RFC 921の前身のスケジュール）、RFC 920（新ドメインの登録要件）。
- HOSTS.TXTの規模、更新頻度、転送負荷の数値を使う場合は、測定時点と一次資料を特定する。RFC 1034の2.1節にある「新版の配布に要する総帯域はホスト数の二乗に比例する」は設計上の見積りであり、当時の実測値ではない。実測として引用しない。
- CDN、Anycast、クラウドDNSの章では、標準仕様だけでなく運用データの出典選定基準を定める。
- 各RFCの更新・訂正（Errata）を章の執筆開始時にRFC Editorで再確認する。
- 可用性、運用性、後方互換性の章に必要な一次資料は、各章の最初の執筆タスクで要件との対応を確認して追加する。
