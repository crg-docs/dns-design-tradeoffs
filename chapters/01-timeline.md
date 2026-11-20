---
layout: default
---

# 第1章 見取り図――DNSは何を、いつ、なぜ足してきたか

> 構成の理由と扱う範囲は[この章の設計メモ](../docs/document-design/01-timeline.md)に記録します。

DNSは一度に設計されたものではありません。1973年から今日までのあいだに、必要が生じるたびに何かが足されてきました。いま複雑に見えるのは、その積み上がりを平らに眺めているからです。

この章は積み上がりを一覧するための見取り図です。

はじめに、この年表が何の年表かを明示します。**並べているのは、仕様や運用上の知見を記したRFCが公表された年です。** 全てが標準仕様というわけではなく、実際に広く使われるようになった年でもありません。また、**本書が扱う要件の索引として作っているため、DNSの通史ではありません。** 国際化ドメイン名のように、本書で扱わない事項は載せていません。

**仕組みがどう動くかは説明しません。** 名前と、それが必要になった理由までを示します。動作の説明と、要件から見た評価は第2章以降がそれぞれ担当します。地図であって解説ではありません。

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
  <text x="120" y="110" font-size="13" fill="#24292f">NICが一覧（HOSTS.TXT）を生成する体制へ（RFC 608）</text>
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
  <text x="0" y="1108" font-size="13" font-weight="bold" fill="#0969da">悪用への耐性</text>
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
  <text x="0" y="1246" font-size="13" font-weight="bold" fill="#0969da">見られていることへの対処</text>
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

## 何が足されてきたか

**集中管理が始まる（1973〜1985年）**――公式のホスト名一覧は存在しましたが、機械可読の形でネットワーク越しに取得できませんでした。各サイトが自前の表を手で維持し、どれも不完全で、互いに食い違っていました。1974年にNICが機械可読の一覧を定期生成する体制を引き受けます。この一覧は `HOSTS.TXT` という名前のファイルとして一箇所に置かれ、各ホストがそれを取得して使いました。1982年には仕様として定まります。集中管理は、より悪い分散状態への対処として始まりました。なお、このホスト表の仕様は取り下げられていません。1985年の改訂版がいまも有効で、そこに書かれたホスト名の書式規則は現在も参照されています。置き換わって消えたのではなく、役割を縮めて残っています。この時点で未解決だったのは、名前を使う前に中央と交渉して登録しなければならないことと、一意性の調整を中央が担っていたことです。

**分散への転換（1983〜1989年）**――更新の件数と更新する組織の数が増え、中央の調整が制約になります。名前空間を階層に分け、管理の責任を委譲する設計が導入されました。名前全体の一意性は保ちながら、各構成要素を親の直下で一意に割り当てる形へ変わります。1987年の仕様は後続RFCによる更新を受けながら標準の骨格として残っています。この段階で複製の定期確認と転送も定められましたが、確認間隔による待ち時間や転送量をどう減らすかは、その後の改善につながります。[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) 2.1節、4.3.5節

**型を増やし、運用の知恵を溜める（1990〜1996年）**――要件の枠組みが変わる転換はありませんが、空白の時期でもありません。運べる情報の種類が増え、負荷を分散させる工夫が試され、よくある設定誤りが文書として整理されます。設計を変えるのではなく、使いながら分かったことを溜めていた時期です。

**扱えるものを増やす（1995〜2013年）**――新しい種類の住所や、長いメッセージを運ぶ必要が生じます。IPv6アドレスのための型が1995年に、メッセージの能力を拡張する仕組みが1999年に定義されました。**どちらも一度で終わっていません。** IPv6対応は2003年に、拡張機構は2013年に、それぞれ改訂されています。ただし、公表年の間隔だけから、普及に要した時間や改訂の理由までは判断できません。[RFC 3596](https://www.rfc-editor.org/rfc/rfc3596.html)、[RFC 6891](https://www.rfc-editor.org/rfc/rfc6891.html)

**隙間を埋める（1996〜1998年）**――複製を定期的に更新する仕組みに対して、待ち時間を短くする変更通知と、転送量を減らす差分転送が追加されます。存在しないという答えの再利用も、1987年の任意の仕組みから規定が改訂されました。以前の仕様に何もなかったのではなく、運用上の制約を改善した段階です。[RFC 1996](https://www.rfc-editor.org/rfc/rfc1996.html) 1節、[RFC 1995](https://www.rfc-editor.org/rfc/rfc1995.html) 1節、[RFC 2308](https://www.rfc-editor.org/rfc/rfc2308.html) 概要

**応答を信用する（1997〜2005年）**――返ってきた答えが本当にその名前の管理者に由来するかを確かめる手段がありませんでした。署名による出所の認証と改ざんの検出が追加されます。最初の仕様は1997年、いま使われている仕様は2005年で、**8年かかっています。** 途中の2004年には、DNSがどう攻撃されうるかを体系的に並べた文書が出ています。ただし署名は通信の内容を隠す仕組みではありません。

**止まらないようにする（2002〜2020年）**――台数を増やすだけでなく、同じアドレスを複数の地点で使う配置と、その運用上の考慮事項が文書化されます。2020年には、権威サーバーから情報を更新できないときに、期限切れのキャッシュを使って応答を継続する規定が追加されました。期限の扱いにも、障害時の応答継続という別の要件から例外が加わったのです。[RFC 3258](https://www.rfc-editor.org/rfc/rfc3258.html)、[RFC 4786](https://www.rfc-editor.org/rfc/rfc4786.html)、[RFC 8767](https://www.rfc-editor.org/rfc/rfc8767.html)

**悪用への耐性（2008〜2010年）**――偽の応答を受け入れる危険への対策と、他人への攻撃の踏み台にされることを防ぐ運用が文書化されます。**偽造の危険は2004年の脅威分析に既に書かれていました。** ここで比較できるのは脅威分析と対策文書の公表時期であり、対策が広く実装された時期ではありません。RFC 5452も、以前に標準化されていなかった挙動を規定すると説明しています。[RFC 3833](https://www.rfc-editor.org/rfc/rfc3833.html)、[RFC 5358](https://www.rfc-editor.org/rfc/rfc5358.html)、[RFC 5452](https://www.rfc-editor.org/rfc/rfc5452.html) 概要

**見られていることへの対処（2016〜2022年）**――問い合わせの内容が経路上で見えることが問題として扱われるようになります。通信の暗号化と、相手へ渡す名前を必要な範囲に絞る方法が追加されました。暗号化しても、問い合わせ先そのものには内容が見えます。

## この整理は後から行ったものです

時代の区切りと要件の名前は、本書が後から与えた整理です。当時の文書が同じ言葉で要件を掲げていたわけではありません。また標準化は並行して進むため、時代の期間は互いに重なります。署名の議論は1997年から2005年まで、拡張の議論は1999年から2013年まで続いており、順番に並んでいたわけではありません。

繰り返し現れる形が一つあります。**最初の仕様と、年表に挙げた改訂版の公表年には間隔があります。** IPv6の型は1995年から2003年、拡張機構は1999年から2013年、署名は1997年から2005年です。ただし、これは開発期間や普及期間の実測ではなく、途中の改訂も省略しています。既存実装との互換性がどのように設計へ影響したかは、第9章で個別の資料に基づいて評価します。

## どの章がどこを扱うか

この章は索引としても使えます。

| 時代 | 足されたもの | 詳しく扱う章 |
| --- | --- | --- |
| 集中管理が始まる | 中央の一覧、登録の受付 | [第2章 拡張性](02-scalability.md) |
| 分散への転換 | 階層と委譲、問い合わせとキャッシュ、複製 | [第2章 拡張性](02-scalability.md)、第3章 性能、第4章 可用性と障害耐性 |
| 型を増やし、運用の知恵を溜める | レコード型の追加、負荷分散の工夫、設定誤りの整理 | 第8章 運用性と保守性、第9章 後方互換性と発展性 |
| 扱えるものを増やす | 能力の通知、メッセージ長の拡張、IPv6の型 | 第9章 後方互換性と発展性 |
| 隙間を埋める | 変更通知、差分転送、不在応答の再利用 | 第3章 性能、第4章 可用性と障害耐性、第5章 整合性と変更反映 |
| 応答を信用する | 署名による出所認証、脅威の分析 | 第6章 セキュリティ、第8章 運用性と保守性、第9章 後方互換性と発展性 |
| 止まらないようにする | 複数地点への配置、期限切れデータの利用 | 第4章 可用性と障害耐性、第3章 性能、第5章 整合性と変更反映 |
| 悪用への耐性 | 受け入れ条件の厳格化、提供先の制限 | 第6章 セキュリティ、第4章 可用性と障害耐性 |
| 見られていることへの対処 | 通信の暗号化、開示する名前の最小化 | 第7章 プライバシー、第8章 運用性と保守性 |

第10章（総括）はどの時代にも対応しません。全章を通した結論を扱う章です。

## この章の言い換え

| 前 | 後 |
| --- | --- |
| 「DNSは複雑だ」 | 「40年かけて足され続けた結果であり、足された順に理由がある」 |
| 「DNSは最初からこう設計されていた」 | 「1987年に定まったのは骨格で、通知、拡張、署名、暗号化、応答継続は後から足された」 |
| 「HOSTS.TXTはDNSに置き換わって消えた」 | 「ホスト表の仕様は廃止されておらず、ホスト名の書式規則として残っている」 |

## 参照資料

年表に挙げた各資料は [出典と、それが裏付ける記述](../references/sources.md) に登録しています。この章の記述で中心となるものは次の通りです。

- [RFC 606: Host Names On-line](https://www.rfc-editor.org/rfc/rfc606.html) 集中管理以前に各サイトが自前の表を維持していたこと。1973年12月の同時代の記録。
- [RFC 882: Domain Names—Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc882.html) 表のサイズと更新頻度が管理の限界に近いという同時代の問題認識。1983年11月。
- [RFC 921: Domain Name System Implementation Schedule - Revised](https://www.rfc-editor.org/rfc/rfc921.html) 一意性を全体から親の下へ移し替えたこと。1984年10月。
- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) / [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html) 現在も標準として使われている1987年の仕様。STD 13。
- [RFC 3833: Threat Analysis of the Domain Name System (DNS)](https://www.rfc-editor.org/rfc/rfc3833.html) 偽造や汚染の危険が2004年に体系的に整理されていたこと。
- [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) 本書の用語の基準。

---

[← 前の章 第0章 DNSはなぜ複雑に見えるのか](00-introduction.md)｜[目次](../)｜[次の章 → 準備章 なぜ名前解決が必要なのか](01-name-resolution.md)
