---
layout: default
---

# 第1章 見取り図――DNSは何を、いつ、なぜ足してきたか

DNSは一度に設計されたものではありません。本章では前史にあたる1973年のホスト表から始め、必要に応じて設計が追加・改訂されてきた過程を眺めます。いま複雑に見える仕組みを、その積み上がりに沿って捉えるためです。

この章は積み上がりを一覧するための見取り図です。

はじめに、この年表が何の年表かを明示します。**並べているのは、仕様や運用上の知見を記したRFCが公表された年です。** 全てが標準仕様というわけではなく、実際に広く使われるようになった年でもありません。また、**本書が扱う要件の索引として作っているため、DNSの通史ではありません。** 国際化ドメイン名のように、本書で扱わない事項は載せていません。

初読では、仕組みの名前を覚える必要はありません。名前と登場した理由を眺め、[準備章](01-name-resolution.md)へ進んでください。動作と設計の評価を読んだ後に戻ると、それぞれの位置を確かめられます。

狭い画面では年表を横へスクロールできます。

<div class="timeline-figure" role="region" aria-label="DNSの年表。横にスクロールできます" tabindex="0">
<svg viewBox="0 0 680 1422" width="100%" role="img" aria-label="DNSの仕様に何がいつ足されたかを時代ごとに縦方向に並べた年表">
  <line x1="104" y1="72" x2="104" y2="1378" stroke="#d0d7de" stroke-width="2"/>
  <text x="0" y="46" font-size="13" font-weight="bold" fill="#0969da">集中管理が始まる</text>
  <line x1="0" y1="54" x2="680" y2="54" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="78" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1973</text>
  <circle cx="104" cy="74" r="4" fill="#0969da"/>
  <text x="120" y="78" font-size="13" fill="#24292f">各サイトが自前のホスト表を維持していた（RFC 606）</text>
  <text x="86" y="110" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1974</text>
  <circle cx="104" cy="106" r="4" fill="#0969da"/>
  <text x="120" y="110" font-size="13" fill="#24292f">NICによる一覧の生成・配布案（RFC 608）</text>
  <text x="86" y="142" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1982</text>
  <circle cx="104" cy="138" r="4" fill="#0969da"/>
  <text x="120" y="142" font-size="13" fill="#24292f">ホスト表と、その配布サービス（RFC 810 / 811）</text>
  <text x="86" y="174" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1985</text>
  <circle cx="104" cy="170" r="4" fill="#0969da"/>
  <text x="120" y="174" font-size="13" fill="#24292f">ホスト表仕様の改訂（RFC 952 / 953）</text>
  <text x="0" y="216" font-size="13" font-weight="bold" fill="#0969da">分散への転換</text>
  <line x1="0" y1="224" x2="680" y2="224" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="248" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1983</text>
  <circle cx="104" cy="244" r="4" fill="#0969da"/>
  <text x="120" y="248" font-size="13" fill="#24292f">ドメイン名の最初の仕様（RFC 882 / 883）</text>
  <text x="86" y="280" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1984</text>
  <circle cx="104" cy="276" r="4" fill="#0969da"/>
  <text x="120" y="280" font-size="13" fill="#24292f">ドメイン名への移行スケジュール（RFC 921）</text>
  <text x="86" y="312" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1987</text>
  <circle cx="104" cy="308" r="4" fill="#0969da"/>
  <text x="120" y="312" font-size="13" fill="#24292f">DNSの仕様、STD 13（RFC 1034 / 1035）</text>
  <text x="86" y="344" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1989</text>
  <circle cx="104" cy="340" r="4" fill="#0969da"/>
  <text x="120" y="344" font-size="13" fill="#24292f">Internet hostへの要求、STD 3（RFC 1123）</text>
  <text x="0" y="386" font-size="13" font-weight="bold" fill="#0969da">型を増やし、運用の知恵を溜める</text>
  <line x1="0" y1="394" x2="680" y2="394" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="418" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1990</text>
  <circle cx="104" cy="414" r="4" fill="#0969da"/>
  <text x="120" y="418" font-size="13" fill="#24292f">新しいレコード型の追加（RFC 1183）</text>
  <text x="86" y="450" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1995</text>
  <circle cx="104" cy="446" r="4" fill="#0969da"/>
  <text x="120" y="450" font-size="13" fill="#24292f">負荷分散のための工夫（RFC 1794）</text>
  <text x="86" y="482" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1996</text>
  <circle cx="104" cy="478" r="4" fill="#0969da"/>
  <text x="120" y="482" font-size="13" fill="#24292f">よくある設定誤りの整理（RFC 1912）</text>
  <text x="0" y="524" font-size="13" font-weight="bold" fill="#0969da">扱えるものを増やす</text>
  <line x1="0" y1="532" x2="680" y2="532" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="556" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1995</text>
  <circle cx="104" cy="552" r="4" fill="#0969da"/>
  <text x="120" y="556" font-size="13" fill="#24292f">DNSでのIPv6アドレス対応（RFC 1886）</text>
  <text x="86" y="588" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1999</text>
  <circle cx="104" cy="584" r="4" fill="#0969da"/>
  <text x="120" y="588" font-size="13" fill="#24292f">EDNSの導入（RFC 2671）</text>
  <text x="86" y="620" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2003</text>
  <circle cx="104" cy="616" r="4" fill="#0969da"/>
  <text x="120" y="620" font-size="13" fill="#24292f">IPv6対応の改訂（RFC 3596）</text>
  <text x="86" y="652" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2013</text>
  <circle cx="104" cy="648" r="4" fill="#0969da"/>
  <text x="120" y="652" font-size="13" fill="#24292f">EDNS(0)、STD 75（RFC 6891）</text>
  <text x="0" y="694" font-size="13" font-weight="bold" fill="#0969da">隙間を埋める</text>
  <line x1="0" y1="702" x2="680" y2="702" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="726" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1996</text>
  <circle cx="104" cy="722" r="4" fill="#0969da"/>
  <text x="120" y="726" font-size="13" fill="#24292f">変更通知と差分転送（RFC 1996 / 1995）</text>
  <text x="86" y="758" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1997</text>
  <circle cx="104" cy="754" r="4" fill="#0969da"/>
  <text x="120" y="758" font-size="13" fill="#24292f">仕様の明確化（RFC 2181）</text>
  <text x="86" y="790" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1998</text>
  <circle cx="104" cy="786" r="4" fill="#0969da"/>
  <text x="120" y="790" font-size="13" fill="#24292f">不在応答の再利用規定を改訂（RFC 2308）</text>
  <text x="0" y="832" font-size="13" font-weight="bold" fill="#0969da">応答を信用する</text>
  <line x1="0" y1="840" x2="680" y2="840" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="864" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1997</text>
  <circle cx="104" cy="860" r="4" fill="#0969da"/>
  <text x="120" y="864" font-size="13" fill="#24292f">DNSSECの最初の仕様（RFC 2065）</text>
  <text x="86" y="896" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2004</text>
  <circle cx="104" cy="892" r="4" fill="#0969da"/>
  <text x="120" y="896" font-size="13" fill="#24292f">脅威の体系的な分析（RFC 3833）</text>
  <text x="86" y="928" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2005</text>
  <circle cx="104" cy="924" r="4" fill="#0969da"/>
  <text x="120" y="928" font-size="13" fill="#24292f">出所認証と完全性（RFC 4033 / 4034 / 4035）</text>
  <text x="0" y="970" font-size="13" font-weight="bold" fill="#0969da">止まらないようにする</text>
  <line x1="0" y1="978" x2="680" y2="978" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="1002" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2002</text>
  <circle cx="104" cy="998" r="4" fill="#0969da"/>
  <text x="120" y="1002" font-size="13" fill="#24292f">権威サーバーを複数地点へ配置（RFC 3258）</text>
  <text x="86" y="1034" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2006</text>
  <circle cx="104" cy="1030" r="4" fill="#0969da"/>
  <text x="120" y="1034" font-size="13" fill="#24292f">Anycastの運用指針、BCP 126（RFC 4786）</text>
  <text x="86" y="1066" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2020</text>
  <circle cx="104" cy="1062" r="4" fill="#0969da"/>
  <text x="120" y="1066" font-size="13" fill="#24292f">期限切れデータによる応答継続（RFC 8767）</text>
  <text x="0" y="1108" font-size="13" font-weight="bold" fill="#0969da">悪用への耐性と既存仕様の明確化</text>
  <line x1="0" y1="1116" x2="680" y2="1116" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="1140" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2008</text>
  <circle cx="104" cy="1136" r="4" fill="#0969da"/>
  <text x="120" y="1140" font-size="13" fill="#24292f">反射攻撃の防止、BCP 140（RFC 5358）</text>
  <text x="86" y="1172" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2009</text>
  <circle cx="104" cy="1168" r="4" fill="#0969da"/>
  <text x="120" y="1172" font-size="13" fill="#24292f">偽造応答への耐性（RFC 5452）</text>
  <text x="86" y="1204" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2010</text>
  <circle cx="104" cy="1200" r="4" fill="#0969da"/>
  <text x="120" y="1204" font-size="13" fill="#24292f">ゾーン転送の明確化（RFC 5936）</text>
  <text x="0" y="1246" font-size="13" font-weight="bold" fill="#0969da">通信方式と情報開示の見直し</text>
  <line x1="0" y1="1254" x2="680" y2="1254" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="1278" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2016</text>
  <circle cx="104" cy="1274" r="4" fill="#0969da"/>
  <text x="120" y="1278" font-size="13" fill="#24292f">TLS暗号化、TCP要件、Client Subnet（RFC 7858 / 7766 / 7871）</text>
  <text x="86" y="1310" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2018</text>
  <circle cx="104" cy="1306" r="4" fill="#0969da"/>
  <text x="120" y="1310" font-size="13" fill="#24292f">HTTPS暗号化（RFC 8484）</text>
  <text x="86" y="1342" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2021</text>
  <circle cx="104" cy="1338" r="4" fill="#0969da"/>
  <text x="120" y="1342" font-size="13" fill="#24292f">問い合わせ名の最小化を改訂（RFC 9156）</text>
  <text x="86" y="1374" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2022</text>
  <circle cx="104" cy="1370" r="4" fill="#0969da"/>
  <text x="120" y="1374" font-size="13" fill="#24292f">QUIC暗号化（RFC 9250）</text>
</svg>
</div>

## 年表から読む設計の重なり

まず、集中管理と分散管理を単純な新旧の対立にしないことです。各サイトの表の食い違いに対して一つの基準を配り、その後、規模と更新主体の増加に対して管理責任を分けました。前の設計が解いた問題と、条件が変わって生じた問題を続けて読むと、第2章の評価につながります。[RFC 606](https://www.rfc-editor.org/rfc/rfc606.html)、[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) 2.1節

次に、一度加わった仕組みも改訂されることです。複製の更新や不在応答の再利用は1987年の仕様にもあり、その後に変更通知、差分転送、再利用規定の改訂が続きました。年表の後の項目が、すべて新しい機能の発明を表すわけではありません。[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) 4.3.5節、[RFC 1996](https://www.rfc-editor.org/rfc/rfc1996.html) 1節、[RFC 1995](https://www.rfc-editor.org/rfc/rfc1995.html) 1節、[RFC 2308](https://www.rfc-editor.org/rfc/rfc2308.html) 概要

最後に、異なる要件への対応が重なっていることです。署名による出所の認証と、通信内容の暗号化は、別の問題を扱います。応答を続けるために期限切れの情報を使う設計も、通常の再利用とは異なる判断です。それぞれを第6章、第7章、第4章で評価します。

時代の区切りと要件の名前は、本書による事後的な整理です。期間が重なるのは、関連する文書の公表年が重なっているためです。公表年の間隔を開発期間や普及期間とはみなしません。途中の改訂を省いたこの図だけから、実装や利用の進み方までは判断できません。

## どの章がどこを扱うか

気になる問題から本編へ進むときは、次の索引を使えます。負荷分散の工夫は年表上の位置を示すにとどめ、製品設定やアルゴリズムの解説は行いません。

| 時代 | 足されたもの | 詳しく扱う章 |
| --- | --- | --- |
| 集中管理が始まる | 中央の一覧、登録の受付 | [第2章 拡張性](02-scalability.md) |
| 分散への転換 | 階層と委譲、問い合わせとキャッシュ、複製 | [第2章 拡張性](02-scalability.md)、[第3章 性能](03-performance.md)、[第4章 可用性と障害耐性](04-availability.md) |
| 型を増やし、運用の知恵を溜める | レコード型の追加、負荷分散の工夫、設定誤りの整理 | [第8章 運用性と保守性](08-operations.md)、[第9章 後方互換性と発展性](09-compatibility.md) |
| 扱えるものを増やす | 能力の通知、メッセージ長の拡張、IPv6の型 | [第9章 後方互換性と発展性](09-compatibility.md) |
| 隙間を埋める | 変更通知、差分転送、不在応答の再利用 | [第3章 性能](03-performance.md)、[第4章 可用性と障害耐性](04-availability.md)、[第5章 整合性と変更反映](05-consistency.md) |
| 応答を信用する | 署名による出所認証、脅威の分析 | [第6章 セキュリティ](06-security.md)、[第8章 運用性と保守性](08-operations.md)、[第9章 後方互換性と発展性](09-compatibility.md) |
| 止まらないようにする | 複数地点への配置、期限切れデータの利用 | [第4章 可用性と障害耐性](04-availability.md)、[第3章 性能](03-performance.md)、[第5章 整合性と変更反映](05-consistency.md) |
| 悪用への耐性と既存仕様の明確化 | 受け入れ条件の厳格化、提供先の制限、転送仕様の明確化 | [第6章 セキュリティ](06-security.md)、[第4章 可用性と障害耐性](04-availability.md) |
| 通信方式と情報開示の見直し | 通信の暗号化、TCP要件、ネットワーク情報の追加、開示する名前の最小化 | [第3章 性能](03-performance.md)、[第7章 プライバシー](07-privacy.md)、[第8章 運用性と保守性](08-operations.md) |

第10章（総括）はどの時代にも対応しません。全章を通した結論を扱う章です。

## この章のポイント

- 現在の仕組みは、一度に完成したものではなく、既存の設計への追加や見直しを重ねたものです。
- 仕様の公表年は、実際に広く使われ始めた時期を示すものではありません。
- 拡張性、性能、障害耐性、保護といった課題は重なり合い、時代ごとに一つずつ解決されたわけではありません。

## 参照資料

年表に挙げた各資料は [出典と、それが裏付ける記述](../references/sources.md) に登録しています。この章の記述で中心となるものは次の通りです。

- [RFC 606: Host Names On-line](https://www.rfc-editor.org/rfc/rfc606.html) 集中管理以前に各サイトが自前の表を維持していたこと。1973年12月の同時代の記録。
- [RFC 608: Host Names On-Line](https://www.rfc-editor.org/rfc/rfc608.html) NICによる機械可読な一覧の生成・配布案。1974年1月。提供開始日は後で告知するとしているため、稼働開始日の記録とは区別します。
- [RFC 882: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc882.html) 表のサイズと更新頻度が管理の限界に近いという同時代の問題認識。1983年11月。
- [RFC 921: Domain Name System Implementation Schedule - Revised](https://www.rfc-editor.org/rfc/rfc921.html) 一意性を全体から親の下へ移し替えたこと。1984年10月。
- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) / [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html) 現在も標準として使われている1987年の仕様。STD 13。
- [RFC 3833: Threat Analysis of the Domain Name System (DNS)](https://www.rfc-editor.org/rfc/rfc3833.html) 偽造や汚染の危険が2004年に体系的に整理されていたこと。
- [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) 本書の用語の基準。

本文の構成と範囲: [文書設計メモ](../docs/document-design/01-timeline.md)

---

[← はじめに](00-introduction.md)｜[目次](../)｜[次の章 → 準備章 なぜ名前解決が必要なのか](01-name-resolution.md)
