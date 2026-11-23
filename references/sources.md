# 出典と裏付け対象

一次資料を中心に、「どの要件について、どの問題・設計・制約を確認する資料か」を記録する。RFCの状態、更新関係、参照箇所は本文執筆時にも再確認する。同じ資料は複数の要件に関係し得るが、未確認の対応は推測で追加しない。

## 設計判断と根拠の再照合（2026-11-23）

全12編の主張を、仕様・歴史資料、実装の説明、観測記録、本書の分析に分けて見直しました。以下は今回の修正に直接関わる照合箇所です。設計比較の数値と部門・移行の例は仮定であり、RFCの推奨値や新しい実測として扱いません。

| 対象 | 照合した根拠 | 本文へ反映した境界 |
| --- | --- | --- |
| 初期目的と用途の時代差 | RFC 882 INTRODUCTION、RFC 1738 3.1節、RFC 1794 1・2節 | 初期の問題認識を直接確認する。URLのRFC公表年を発明年、負荷分散の回顧文書の公表年を用途開始年にしない |
| 集中と分散、配布負荷 | RFC 606・608、RFC 810 ASSUMPTIONS 6・7、RFC 1034 2.1・2.2・4.2節 | 集中管理の利点を維持する。全体配布を避けられることから、総通信量が無条件に減るとは導かない |
| キャッシュと復旧 | RFC 1035 3.2.1節、RFC 2181 8節、RFC 9520 3.2節 | TTL比だけで実負荷を予測しない。失敗の再利用は復旧を遅らせ得る。RFC 9520による失敗キャッシュの必須化を維持 |
| 応答継続の期限 | RFC 1034 4.3.5節、RFC 8767 4〜6・10節 | Secondaryの失効期限、通常のキャッシュ期限、署名有効期間を区別する。Serve Staleだけで検証成功は保証しない |
| 更新の範囲 | RFC 2136 概要・2.3節 | 一つのゾーンへの更新を、複数ゾーンや全キャッシュの同時変更に広げない |
| 検証と利用側の方針 | RFC 4033 5節、RFC 4035 4.3・5.3.3・5.5節、RFC 6840 4.4・5.7・5.8節 | 通常の検証とSecure必須の方針を分離。検証済みデータのTTLにも署名の残り有効時間の制約がある |
| 秘匿と代替経路 | RFC 8310 5・5.1・6.6節、RFC 7871 2節 | StrictからOpportunisticへの同一問い合わせ中の降格は禁止。同じ保護の代替先と平文継続を別の案にする。ECSは明確な利益がある場合に明示的に有効化するよう文書自身が推奨 |
| 運用と原因情報 | RFC 9499 6節、RFC 8914 3・6節 | Viewは製品の構成、EDEは補助情報。変更主体の分割や監視時間の配分は本書の提案として区別する |
| 拡張の受け入れ | RFC 3597 3・4節、RFC 6891 6.1.2・6.1.3・6.2.2節、RFC 8906 3節 | 未知のオプションを無視する動作と未対応の版への応答を区別。応答成功だけでは拡張の利用成功を証明しない |
| 総括の移行目標 | 第3・4・5・6・8章の条件を再利用 | 権威側更新後の5分と操作開始からの全時間を分離。再取得・接続・観測の時間と、案が成立しなくなる条件を明示 |

RFC 4035の更新一覧とRFC 9824の概要・対象を再確認しました。今回の署名期限と検証方針の説明に、NSECによる不在応答の実装規則は持ち込みません。Errata 8037（RFC 4035、検証時の鍵候補の扱い）と8348（RFC 6891、OPTのCLASS欄）は今回もHeld for Document Updateであり、確定訂正として採用していません。今回追加したTTL最小値と未知オプションの規定は、それぞれの訂正対象とは別です。以前の全件検索記録は下部に日付を付けて残し、今回全件を再監査したという記録にはしません。

BIND 9.20.16のPrefetch、Cloudflareのゾーン転送・JSON API・2020年7月17日の障害報告も、本文が使う範囲で再確認しました。実装資料から他製品の挙動を推定せず、障害報告から全拠点停止とは結論しません。過去の観測値や実験条件は変更していません。

## 年表の仕様年と追加された役割

2026-11-20に以下のRFC本文の表題、発行年月、概要を確認しました。ここで裏付けるのは文書の公表と記述内容であり、普及時期ではありません。後続章で現在の規定を使う際は、更新RFCとErrataを節ごとに確認します。

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 1183: New DNS RR Definitions](https://www.rfc-editor.org/rfc/rfc1183.html) | 1990年にもレコード型の追加が検討されたこと | 1990年10月。実験目的の型の定義であり、全てが普及したとはしない |
| [RFC 1912: Common DNS Operational and Configuration Errors](https://www.rfc-editor.org/rfc/rfc1912.html) | よくある運用・設定誤りの文書化 | 1996年2月、Informational。仕様制定と運用上の助言を区別する |
| [RFC 1886: DNS Extensions to support IP version 6](https://www.rfc-editor.org/rfc/rfc1886.html) | 1995年のDNSにおけるIPv6アドレス対応 | 1995年12月。RFC 3596が廃止。IPv6自体の誕生年とはしない |
| [RFC 2671: Extension Mechanisms for DNS (EDNS0)](https://www.rfc-editor.org/rfc/rfc2671.html) | 1999年の拡張機構の定義 | 1999年8月。RFC 6891が廃止。運用への普及年は示さない |
| [RFC 3596: DNS Extensions to Support IP Version 6](https://www.rfc-editor.org/rfc/rfc3596.html) | 2003年のIPv6対応の改訂 | 2003年10月。RFC 1886/3152を廃止。改訂間隔を普及までの所要年数とみなさない |
| [RFC 6891: Extension Mechanisms for DNS (EDNS(0))](https://www.rfc-editor.org/rfc/rfc6891.html) | 2013年の拡張機構の改訂 | 2013年4月、STD 75。RFC 2671/2673を廃止。初期の固定長制約を拡張する設計として第9章へつなぐ |
| [RFC 1995: Incremental Zone Transfer in DNS](https://www.rfc-editor.org/rfc/rfc1995.html) | ゾーン全体ではなく変更部分を転送して配布量を減らす設計 | 1996年8月、1節。全量転送がそれ以前から存在したことも確認できる |
| [RFC 1996: A Mechanism for Prompt Notification of Zone Changes (DNS NOTIFY)](https://www.rfc-editor.org/rfc/rfc1996.html) | 定期確認の間隔による反映遅延を変更通知で短縮する設計 | 1996年8月、1節。通知自体とデータの転送を同一視しない |
| [RFC 2308: Negative Caching of DNS Queries (DNS NCACHE)](https://www.rfc-editor.org/rfc/rfc2308.html) | 不在応答のキャッシュ規定の改訂 | 1998年3月、概要。RFC 1034にも任意の仕組みがあったため、1998年を発明年とはしない |
| [RFC 2065: Domain Name System Security Extensions](https://www.rfc-editor.org/rfc/rfc2065.html) | DNSSECの最初の仕様が1997年に公表されたこと | 1997年1月。歴史資料として使い、現在のDNSSECの動作説明はRFC 4033〜4035等を使う |
| [RFC 3258: Distributing Authoritative Name Servers via Shared Unicast Addresses](https://www.rfc-editor.org/rfc/rfc3258.html) | 同じアドレスで権威サーバーを複数地点へ配置する設計の文書化 | 2002年4月、Informational。配置の効果と経路への依存を第4章で評価する |
| [RFC 4786: Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786.html) | Anycastの運用上の考慮事項の整理 | 2006年12月、BCP 126。DNS専用の規定でも普及率の資料でもない |
| [RFC 5452: Measures for Making DNS More Resilient against Forged Answers](https://www.rfc-editor.org/rfc/rfc5452.html) | 偽造応答を受け入れにくくする対策の標準化 | 2009年1月、概要。以前に標準化されていなかった挙動を規定する文書であり、対策が初めて実装された年とはしない |
| [RFC 5936: DNS Zone Transfer Protocol (AXFR)](https://www.rfc-editor.org/rfc/rfc5936.html) | 既存の全量ゾーン転送仕様の明確化 | 2010年6月、概要。AXFRはRFC 1034/1035に存在し、2010年に新設されたものではない |
| [RFC 7766: DNS Transport over TCP - Implementation Requirements](https://www.rfc-editor.org/rfc/rfc7766.html) | TCP対応と接続運用の要求の改訂 | 2016年3月。RFC 5966を廃止。TCP利用自体の登場年ではなく、暗号化の仕様でもない |
| [RFC 7871: Client Subnet in DNS Queries](https://www.rfc-editor.org/rfc/rfc7871.html) | 問い合わせ元ネットワークの情報を渡す拡張の文書化 | 2016年5月、Informational。性能と情報開示の衝突を第7章で評価する。暗号化・開示削減と区別する |
| [RFC 9156: DNS Query Name Minimisation to Improve Privacy](https://www.rfc-editor.org/rfc/rfc9156.html) | 上流へ送る問い合わせ名を必要な範囲に絞る手法の改訂 | 2021年11月。RFC 7816を廃止。2021年を最初の提案年とはしない |

## 整合性と変更反映

2026-11-20に第5章の使用箇所を確認しました。実験は仕様の証明ではなく、固定した実装・設定での観測です。

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 1982: Serial Number Arithmetic](https://www.rfc-editor.org/rfc/rfc1982.html) | SOA Serialの周回と比較規則 | 1996年8月、2〜4節。RFC 1034/1035を更新。時刻としての解釈や通常の大小比較へ置き換えない |
| [RFC 2136: Dynamic Updates in the Domain Name System (DNS UPDATE)](https://www.rfc-editor.org/rfc/rfc2136.html) | 前提条件付きの追加・削除と更新の原子性 | 1997年4月、概要・3節。RFC 1035を更新し、RFC 3007・4033〜4035で更新。原子性を全キャッシュの同時変更へ拡張しない。認証は第6章で別途扱う |
| [CoreDNS: file](https://coredns.io/plugins/file/) | ファイルとSOAの版に基づく再読み込み | `reload`の指定。今回の1秒は実験設定で、標準値ではない |
| [CoreDNS: cache](https://coredns.io/plugins/cache/) | キャッシュ期間の上限指定 | `cache 300`は全回答を300秒保存する指定ではない。実験ではTTL 20秒と5秒を使用 |
| [CoreDNS: forward](https://coredns.io/plugins/forward/) | 明示した上流への転送 | 今回はループバックの権威側だけを指定。インターネットの反復解決とは区別 |
| [CoreDNS v1.15.0](https://github.com/coredns/coredns/releases/tag/v1.15.0) | 実験に用いた配布物と版 | Windows amd64。公式チェックサムを照合して使用。観測JSONに実行時の版と全設定を保存 |

RFC 2308の3・5節は不在応答のTTLに使用します。後続のRFC 9499は用語、RFC 9520は解決失敗のキャッシュに関わり、本章の名前の不在とは区別します。

## 拡張性と分散管理

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) | HOSTS.TXT方式で顕在化した問題、DNSの設計目標、名前空間・委譲・ゾーンによる分散管理 | 特に2章。従来方式の制約と新方式の狙いを確認する。1987年11月、STD 13。RFC 882/883/973を廃止。19件のRFCが更新しており、1987年時点の規定を現在の規定として扱わない |
| [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) | 名前サーバーとリゾルバの実装、マスターファイルなど、分散したデータを提供・利用する仕組み | RFC 1034と一組で読む。1987年11月、STD 13。29件のRFCが更新しており、本書の論点に関わる更新（RFC 2181、2308、4033〜4035、5936、7766、8767）は該当章で個別に確認する |
| [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) | ドメイン、ゾーン、委譲などを現行用語で区別する基準 | 歴史資料中の語と現行語を区別する。2024年、BCP 219。RFC 8499を廃止。RFC 2308の更新対象はforwarderとQNAMEの定義の明確化であり、否定応答の保持期間の変更ではない |

## 名前解決を読むための前提

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 606: Host Names On-line](https://www.rfc-editor.org/rfc/rfc606.html) | DNS以前にもホスト名とアドレスの対応表が使われていたこと | 1973年12月。DNSが名前解決そのものを発明したとは書かない |
| [RFC 608: Host Names On-Line](https://www.rfc-editor.org/rfc/rfc608.html) | NICが機械可読な一覧を生成し、各サイトへ提供する案 | 1974年1月。集中管理が表の不一致への対処だったことを示す |
| [RFC 1738: Uniform Resource Locators (URL)](https://www.rfc-editor.org/rfc/rfc1738.html) | URLが方式やホストなどを含み、ホスト名そのものではないこと | 1994年12月。RFC 3986は本文書を更新し、RFC 4248とRFC 4266が本文書を廃止している。初期Webとの時代差を示す歴史資料としてのみ使う |
| [RFC 1794: DNS Support for Load Balancing](https://www.rfc-editor.org/rfc/rfc1794.html) | DNSを使った負荷分散が、初期DNS仕様より後に独立した運用上の問題として文書化されたこと | 1995年4月、Informational。現代の負荷分散方式全般の仕様として一般化しない |

## 性能、整合性、変更反映

第3章の追加資料は2026-11-20に本文の使用箇所を確認しました。RFC 2308の失敗キャッシュに関する記述はRFC 9520の更新を反映し、Prefetchは特定バージョンの実装例として扱います。

| 追加資料 | 本書で裏付ける記述 | 適用範囲 |
| --- | --- | --- |
| [RFC 9520: Negative Caching of DNS Resolution Failures](https://www.rfc-editor.org/rfc/rfc9520.html) | 不在の確認と解決失敗を区別し、失敗の反復による上流負荷を抑える設計 | 2023年12月。概要、3節。RFC 2308/4035/4697を更新。失敗を不在へ変えるものではない |
| [BIND 9.20.16 ARM: prefetch](https://bind9.readthedocs.io/en/v9.20.16/reference.html#namedconf-statement-prefetch) | 期限の近いキャッシュへの問い合わせを契機とした先取り更新 | 第3章の実装例。BIND 9.20.16に限定し、他実装の挙動や既定値へ一般化しない |
| [Microsoft Learn: Resolve-DnsName](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) | Server、DnsOnly、NoHostsFile等の観測コマンドの指定 | 第3章の再現条件。DNS仕様の根拠としては使わない |

| 資料 | 本書で裏付ける記述 | 問題・環境・トレードオフ |
| --- | --- | --- |
| [RFC 1034: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) | リゾルバ、再帰・反復、キャッシュの基本概念 | 問い合わせと再利用が負荷を抑える一方、キャッシュされたコピーを生む |
| [RFC 1035: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) | メッセージ形式、TTL、UDP/TCP利用、ゾーン転送 | 初期仕様として確認し、現在のトランスポート要件へ一般化しない |
| [RFC 1123: Requirements for Internet Hosts—Application and Support](https://www.rfc-editor.org/rfc/rfc1123.html) | Internet hostにおけるリゾルバ・トランスポート等の要求の補足 | 6.1節「DOMAIN NAME TRANSLATION」。1989年10月、STD 3。RFC 1034/1035制定後の要求であり初期仕様と混同しない。RFC 2181、5966、7766、9210が更新している |
| [RFC 2181: Clarifications to the DNS Specification](https://www.rfc-editor.org/rfc/rfc2181.html) | TTL、データ順位、ゾーン境界などDNS仕様の明確化 | 「明確化」が初期実装すべての挙動を記述するとは限らない |

## 可用性と障害耐性

非RFC資料は、運用主体・管理主体が自ら公表した構成説明、仕様、障害報告を一次資料として採用します。製品資料はそのサービスの確認日時点の挙動に限定し、広告的な可用性の評価や他製品との優劣の根拠にはしません。障害報告は発生日と公開日を区別します。URLが失効した場合は、同じ発行主体の移転先か当時の保存版を確認し、本文を確認できなければ根拠未確認へ戻します。数値比較には測定条件がある資料を必要とします。

2026-11-20、第4章で使う次の3本の非RFC資料とRFC 2182を確認しました。

| 追加資料 | 本書で裏付ける記述 | 適用範囲 |
| --- | --- | --- |
| [RFC 2182: Selection and Operation of Secondary DNS Servers](https://www.rfc-editor.org/rfc/rfc2182.html) | 複製の物理配置とネットワーク上の配置を共に評価すること | 1997年7月、BCP 16。3節、4節。台数だけで可用性を評価しない根拠 |
| [IANA: Root Name Servers](https://www.iana.org/domains/root/servers) | サーバー名の一覧と多数の物理的な設備を区別すること | 管理主体の公式一覧。台数・拠点数を固定的な値として本文へ持ち込まない |
| [Cloudflare DNS: Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/) | 異なる事業者間でPrimary/SecondaryとAXFR/IXFRによる同期を構成する実装例 | 当該サービスの構成例。すべての独自機能が相互運用するという根拠にはしない |
| [Cloudflare: Cloudflare outage on July 17, 2020](https://blog.cloudflare.com/cloudflare-outage-on-july-17-2020/) | 共通のバックボーン設定の誤りが複数拠点へ影響したこと | 2020-07-17発生、2020-07-18公開の当事者報告。全拠点障害やDNS全体の停止へ一般化しない |

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 8767: Serving Stale Data to Improve DNS Resiliency](https://www.rfc-editor.org/rfc/rfc8767.html) | 権威サーバーへ到達できないとき、期限切れのキャッシュデータを返して応答を継続する設計。第0章の「障害中に古い情報を返す判断」の裏付け | 2020年、Proposed Standard。RFC 1034/1035/2181を更新し、TTL満了後のデータ利用を例外的な状況に限って認める。可用性と最新性を交換する選択として扱い、常時の挙動と混同しない。滞留時間の上限値や推奨タイマーを本文へ引く場合は TODO: 要検証 |

## セキュリティ

第6章では2026-11-20に使用箇所を確認しました。RFC 4033〜4035の基本的な信頼モデルに範囲を絞り、具体的な署名アルゴリズム、鍵長、NSECの実装手順は推奨しません。BailiwickはRFC 9499の7節に従って歴史的用語として扱います。

| 追加資料 | 本書で裏付ける記述 | 注意 |
| --- | --- | --- |
| [RFC 6840: Clarifications and Implementation Notes for DNS Security (DNSSEC)](https://www.rfc-editor.org/rfc/rfc6840.html) | ADビットの問い合わせ・応答での意味 | 2013年2月。RFC 4033〜4035・5155を更新。5.7・5.8節 |
| [RFC 6781: DNSSEC Operational Practices, Version 2](https://www.rfc-editor.org/rfc/rfc6781.html) | 鍵交換とキャッシュの時間的依存 | 2012年12月、Informational、RFC 4641を廃止。4節。過去のアルゴリズム推奨を現在へ転用しない |
| [RFC 8945: Secret Key Transaction Authentication for DNS (TSIG)](https://www.rfc-editor.org/rfc/rfc8945.html) | 共有秘密による取引の認証と鍵配布の前提 | 2020年11月、STD 93。RFC 2845・4635を廃止。暗号化・認可範囲の決定とは区別 |
| [BIND 9.20.16: rate-limit](https://bind9.readthedocs.io/en/v9.20.16/reference.html#namedconf-statement-rate-limit) | UDP応答の制限による反射・増幅への対処例 | 製品固有のRRL。正当な問い合わせへの影響も評価対象 |

| 資料 | 本書で裏付ける記述 | 主な箇所・注意 |
| --- | --- | --- |
| [RFC 3833: Threat Analysis of the Domain Name System (DNS)](https://www.rfc-editor.org/rfc/rfc3833.html) | DNSに対する脅威を、名前空間、名前サーバー、リゾルバなどの構成要素ごとに整理した分析 | 2004年8月、Informational。対策の仕様ではなく脅威分析として扱う。個別の事件名や対策の普及時期の根拠には使わない |
| [RFC 4033: DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033.html) | DNSSECの目的、能力、制約、導入要件、TTLと署名期限の違い | 導入と脅威・非目標。2005年3月、RFC 6014と6840が更新。4節の非目標、5節の検証状態、8.1・8.2節の署名の有効期間と保守を使用。TTLを長くして署名期限を延ばせるとは書かない |
| [RFC 4034: Resource Records for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4034.html) | DNSKEY、RRSIG、NSEC、DSの形式と意味 | レコード形式の根拠。2005年3月。RFC 4470、6014、6840、6944、9077、9824、9905が更新しており、アルゴリズムとNSECの扱いは更新後を確認する |
| [RFC 4035: Protocol Modifications for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4035.html) | 署名生成、応答、検証、Authenticated Data等のプロトコル動作 | 検証状態と実装役割を一般化しすぎない。2005年3月。RFC 4470、6014、6840、8198、9077、9520、9824が更新している |
| [RFC 5358: Preventing Use of Recursive Nameservers in Reflector Attacks](https://www.rfc-editor.org/rfc/rfc5358.html) | オープンな再帰サーバーが反射攻撃に利用される問題と、再帰サービスを許可先へ限定する推奨 | BCP 140。権威サービスと再帰サービスを区別する |

## プライバシー

2026-11-20、第7章で保護区間と観測者を分けて参照しました。事業者のログ保持を外部から検証したとは扱いません。

| 追加資料 | 本書で裏付ける記述 | 注意 |
| --- | --- | --- |
| [RFC 9076: DNS Privacy Considerations](https://www.rfc-editor.org/rfc/rfc9076.html) | 公開データと問い合わせ履歴の区別、観測者と集中の問題 | 2021年7月、Informational、RFC 7626を廃止。1・4・6節。対策を規定する文書ではない |
| [RFC 8310: Usage Profiles for DNS over TLS and DNS over DTLS](https://www.rfc-editor.org/rfc/rfc8310.html) | 認証と保護を必須にする場合、可能な場合に使う場合の違い | 2018年3月、RFC 7858を更新。5・6・11.1節 |
| [Cloudflare: Using JSON](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/) | 実観測に使うHTTPS JSON API | JSONは標準のRFC 8484ワイヤー形式とは異なる。提供元自身が共通RFCの不在を明示 |

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
| [RFC 811: Hostnames Server](https://www.rfc-editor.org/rfc/rfc811.html) | HOSTS.TXTの登録・取得と、更新主体・配布工程 | 実読済み（2026-08-05）。1982年3月、RFC 953により廃止。第2章では登録工程の根拠にRFC 810を使い、取得プロトコルを扱う場合に参照する |
| [RFC 921: Domain Name System Implementation Schedule - Revised](https://www.rfc-editor.org/rfc/rfc921.html) | 移行期の具体的な互換措置。旧名に `.ARPA` を付けたものを新しい名前とする制約、DHOSTS.TXTによる新旧二重提供、平坦な名前空間から階層への一意性の移し替え | 実読済み（2026-08-05）。1984年10月、IABとDARPAの公式方針。RFC 897とRFC 881を更新。予定が機能しなかったという記録は第2章で使うが、その原因は特定しない。第9章は別の拡張例を扱う |
| [RFC 952: DoD Internet Host Table Specification](https://www.rfc-editor.org/rfc/rfc952.html) | HOSTS.TXT期後半のホスト表仕様。ホスト名の書式規則と、役割を名前に埋め込む規約（-GATEWAY、-GW） | 実読済み（2026-08-05）。1985年10月。RFC 608/810を廃止。廃止されておらずRFC 1123が更新しているため、「DNS以前の仕様」として過去形で扱わない |
| [RFC 953: Hostname Server](https://www.rfc-editor.org/rfc/rfc953.html) | ホスト表の配布・取得サービスの後期仕様 | 実読済み（2026-08-05）。1985年10月、RFC 811を廃止。現在はHistoric。RFC 952が配布手段として参照している |
| [RFC 882: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc882.html) | 従来方式の制約と、階層化・分散管理が解決しようとした問題 | 実読済み（2026-08-05）。1983年11月、RFC 973が更新し、RFC 1034/1035により廃止。表の大きさと更新頻度が管理可能な限界に近いという記述を第2章で参照する |
| [RFC 883: Domain Names—Implementation and Specification](https://www.rfc-editor.org/rfc/rfc883.html) | 初期DNSが導入した運用上の役割とトレードオフ | 実読済み（2026-08-05）。1983年11月、RFC 973が更新し、RFC 1034/1035により廃止。第2章の責任分割は概念を定めるRFC 882と後継のRFC 1034で裏付け、実装詳細を扱う場合に参照する |

## 運用性と拡張時の診断

| 第9章の追加資料 | 本書で裏付ける記述 | 注意 |
| --- | --- | --- |
| [RFC 3597: Handling of Unknown DNS Resource Record (RR) Types](https://www.rfc-editor.org/rfc/rfc3597.html) | 未知の型のデータを変更せずに保持・転送する設計 | 2003年9月、1・3・4節。意味を利用するアプリケーションの対応とは区別。DNSSEC正規化の後続変更は本章の対象外 |

第9章ではRFC 6891の6節（OPT・能力通知・フォールバック）、RFC 3596の1節（データと輸送のIP版の独立）、RFC 8906も確認しました。過去のUDPバッファ推奨値を現在の全環境へ転用せず、実機試験を行ったとは記載しません。

2026-11-20、第8章で使用する箇所を確認しました。運用フローの提案と規格の要求を分けて記述します。

| 資料 | 本書で裏付ける記述 | 注意 |
| --- | --- | --- |
| [RFC 8906: A Common Operational Problem in DNS Servers: Failure to Communicate](https://www.rfc-editor.org/rfc/rfc8906.html) | 不応答や不適切な応答が運用と拡張を妨げる問題 | 2020年9月、BCP 231。データ内容の正しさの検査とは区別 |
| [RFC 8914: Extended DNS Errors](https://www.rfc-editor.org/rfc/rfc8914.html) | 応答コードを変えず原因情報を補助する拡張 | 2020年10月。3・6節。全サーバーでの提供や情報の認証を保証しない |

RFC 1912は2.8節の委譲不整合の例を使い、古い製品の設定やタイマーを現在へ転用しません。Split DNSとViewはRFC 9499の6節を参照します。

## 全章初稿時のErrata確認（2026-11-20）

この台帳に本文URLを登録した54本のRFCについて、RFC EditorのErrata検索を再確認し、119件の状態・節番号を[確認記録](observations/errata-index-2026-11-20.json)に保存しました。検索結果の確認に加え、VerifiedのTechnical訂正と、使用箇所に関わる一部の保留・編集上の訂正を本文の主張と照合しています。全RFCの全実装規則を監査したという意味ではありません。Reported、Held for Document Update、RejectedをVerifiedと同じ確定訂正として適用しません。

| 関連箇所 | 照合した訂正 | 本文への判断 |
| --- | --- | --- |
| キャッシュ・TTL・SOA | RFC 1035の2130・6601・6463、RFC 1034の4943 | TTLの符号付きという古い記述や、ゾーンとキャッシュの時刻表現を混同しない。本文はTTLのビット実装を説明せず、SOAも一律TTL 0とはしていない |
| IXFRと動的更新 | RFC 1995の3197、RFC 2136の4469 | 差分転送をRRの途中のバイトだけを送る処理とは記述していない。CNAME競合時の更新疑似コードは扱っていない |
| DNSSEC | RFC 4033〜4035の3043〜3045、4034の1062・4552、4035の5226 | RFC 3007への誤った更新表記を主張しない。正規化・鍵タグ計算・DS問い合わせの特殊処理は今回の責務外 |
| 鍵交換 | RFC 6781の4844・5174・6692 | キャッシュ期限と親子の更新が関わるという範囲に限定。訂正前の鍵交換図や手順を転記しない |
| ADとEDNS | RFC 6840の4924・4927・4928、RFC 6891の3604、保留8348 | ADの明確化を本文に反映済み。EDNSは能力通知として説明し、応答側が要求側の値を単純コピーするという説明はしない |
| ECS・DoQ・未知の型 | RFC 7871の4735、RFC 9250の7883、RFC 3597の1063 | ECSの詳細なプレフィックス例、DoQのパディング要件、DNSSEC正規化の型一覧は転記していない |

これ以外の訂正についても、状態と該当節を記録しています。実装手順や具体的な数値を追加する改稿では、その節の訂正本文と後続RFCを改めて読みます。

## 出典管理上の未解決事項

- HOSTS.TXT以前の名前解決を説明する同時代資料は追加済み（RFC 606、2026-08-05）。抽出結果は [HOSTS.TXT期の一次資料からの抽出](hosts-txt-findings.md) にある。未読で残しているのは RFC 597（RFC 606が参照する公式ホスト名一覧）、RFC 881・897（RFC 921の前身のスケジュール）、RFC 920（新ドメインの登録要件）。
- HOSTS.TXTの規模、更新頻度、転送負荷の数値を使う場合は、測定時点と一次資料を特定する。RFC 1034の2.1節にある「新版の配布に要する総帯域はホスト数の二乗に比例する」は設計上の見積りであり、当時の実測値ではない。実測として引用しない。
- CDN、Anycast、クラウドDNSの章では、標準仕様だけでなく運用データの出典選定基準を定める。
- 各RFCの更新・訂正（Errata）を章の執筆開始時にRFC Editorで再確認する。
- 可用性、運用性、後方互換性の章に必要な一次資料は、各章の最初の執筆タスクで要件との対応を確認して追加する。
