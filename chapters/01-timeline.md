# 第1章 見取り図――DNSは何を、いつ、なぜ足してきたか

DNSは一度に設計されたものではありません。1973年から今日までのあいだに、必要が生じるたびに何かが足されてきました。いま複雑に見えるのは、その積み上がりを平らに眺めているからです。

この章は積み上がりを一覧するための見取り図です。**仕組みがどう動くかは説明しません。** 名前と、それが必要になった理由までを示します。動作の説明と、要件から見た評価は第2章以降がそれぞれ担当します。地図であって解説ではありません。

<svg viewBox="0 0 680 1092" width="100%" role="img" aria-label="DNSに何がいつ足されたかを時代ごとに縦方向に並べた年表">
  <line x1="104" y1="72" x2="104" y2="1048" stroke="#d0d7de" stroke-width="2"/>
  <text x="0" y="46" font-size="13" font-weight="bold" fill="#0969da">集中管理の時代</text>
  <line x1="0" y1="54" x2="680" y2="54" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="78" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1973</text>
  <circle cx="104" cy="74" r="4" fill="#0969da"/>
  <text x="120" y="78" font-size="13" fill="#24292f">各サイトが自前のホスト表を維持していた（RFC 606）</text>
  <text x="86" y="110" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1974</text>
  <circle cx="104" cy="106" r="4" fill="#0969da"/>
  <text x="120" y="110" font-size="13" fill="#24292f">NICが機械可読の一覧を生成する体制へ（RFC 608）</text>
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
  <text x="0" y="386" font-size="13" font-weight="bold" fill="#0969da">隙間を埋める</text>
  <line x1="0" y1="394" x2="680" y2="394" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="418" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1996</text>
  <circle cx="104" cy="414" r="4" fill="#0969da"/>
  <text x="120" y="418" font-size="13" fill="#24292f">変更通知と差分転送（RFC 1996 / 1995）</text>
  <text x="86" y="450" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1997</text>
  <circle cx="104" cy="446" r="4" fill="#0969da"/>
  <text x="120" y="450" font-size="13" fill="#24292f">仕様の明確化（RFC 2181）</text>
  <text x="86" y="482" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1998</text>
  <circle cx="104" cy="478" r="4" fill="#0969da"/>
  <text x="120" y="482" font-size="13" fill="#24292f">不在応答の再利用（RFC 2308）</text>
  <text x="0" y="524" font-size="13" font-weight="bold" fill="#0969da">拡張の余地を作る</text>
  <line x1="0" y1="532" x2="680" y2="532" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="556" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">1999</text>
  <circle cx="104" cy="552" r="4" fill="#0969da"/>
  <text x="120" y="556" font-size="13" fill="#24292f">EDNSの導入（RFC 2671）</text>
  <text x="86" y="588" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2013</text>
  <circle cx="104" cy="584" r="4" fill="#0969da"/>
  <text x="120" y="588" font-size="13" fill="#24292f">EDNS(0)、STD 75（RFC 6891）</text>
  <text x="0" y="630" font-size="13" font-weight="bold" fill="#0969da">応答を信用する</text>
  <line x1="0" y1="638" x2="680" y2="638" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="662" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2005</text>
  <circle cx="104" cy="658" r="4" fill="#0969da"/>
  <text x="120" y="662" font-size="13" fill="#24292f">出所認証と完全性（RFC 4033 / 4034 / 4035）</text>
  <text x="0" y="704" font-size="13" font-weight="bold" fill="#0969da">悪用への耐性</text>
  <line x1="0" y1="712" x2="680" y2="712" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="736" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2008</text>
  <circle cx="104" cy="732" r="4" fill="#0969da"/>
  <text x="120" y="736" font-size="13" fill="#24292f">反射攻撃の防止、BCP 140（RFC 5358）</text>
  <text x="86" y="768" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2009</text>
  <circle cx="104" cy="764" r="4" fill="#0969da"/>
  <text x="120" y="768" font-size="13" fill="#24292f">偽造応答への耐性（RFC 5452）</text>
  <text x="86" y="800" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2010</text>
  <circle cx="104" cy="796" r="4" fill="#0969da"/>
  <text x="120" y="800" font-size="13" fill="#24292f">ゾーン転送の明確化（RFC 5936）</text>
  <text x="0" y="842" font-size="13" font-weight="bold" fill="#0969da">見られていることへの対処</text>
  <line x1="0" y1="850" x2="680" y2="850" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="874" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2016</text>
  <circle cx="104" cy="870" r="4" fill="#0969da"/>
  <text x="120" y="874" font-size="13" fill="#24292f">TLS暗号化、TCP要件、Client Subnet（RFC 7858 / 7766 / 7871）</text>
  <text x="86" y="906" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2018</text>
  <circle cx="104" cy="902" r="4" fill="#0969da"/>
  <text x="120" y="906" font-size="13" fill="#24292f">HTTPS暗号化（RFC 8484）</text>
  <text x="86" y="938" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2021</text>
  <circle cx="104" cy="934" r="4" fill="#0969da"/>
  <text x="120" y="938" font-size="13" fill="#24292f">問い合わせ名の最小化（RFC 9156）</text>
  <text x="86" y="970" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2022</text>
  <circle cx="104" cy="966" r="4" fill="#0969da"/>
  <text x="120" y="970" font-size="13" fill="#24292f">QUIC暗号化（RFC 9250）</text>
  <text x="0" y="1012" font-size="13" font-weight="bold" fill="#0969da">壊れても答え続ける</text>
  <line x1="0" y1="1020" x2="680" y2="1020" stroke="#0969da" stroke-width="1" opacity="0.25"/>
  <text x="86" y="1044" font-size="13" font-weight="bold" fill="#57606a" text-anchor="end">2020</text>
  <circle cx="104" cy="1040" r="4" fill="#0969da"/>
  <text x="120" y="1044" font-size="13" fill="#24292f">期限切れデータによる応答継続（RFC 8767）</text>
</svg>

## 何が足されてきたか

**集中管理が始まる（1973〜1985年）**――公式のホスト名一覧は存在しましたが、機械可読の形でネットワーク越しに取得できませんでした。各サイトが自前の表を手で維持し、どれも不完全で、互いに食い違っていました。1974年にNICが機械可読の一覧を定期生成する体制を引き受け、1982年に仕様として定まります。集中管理は、より悪い分散状態への対処として始まりました。なお、このホスト表の仕様は取り下げられていません。1985年の改訂版がいまも有効で、そこに書かれたホスト名の書式規則は現在も参照されています。置き換わって消えたのではなく、役割を縮めて残っています。この時点で未解決だったのは、名前を使う前に中央と交渉して登録しなければならないことと、一意性の調整を中央が担っていたことです。

**分散への転換（1983〜1989年）**――更新の件数と更新する組織の数が増え、中央の調整が追いつかなくなります。名前空間を階層に分け、管理の責任を委譲する設計が導入されました。名前の一意性は、全体で唯一の文字列であることから、親の名前の下でだけ唯一であることへ移し替えられます。1987年の仕様が現在も標準として使われています。未解決だったのは、複製をいつどう同期するか、そして既に動いている名前をどう移すかでした。

**隙間を埋める（1996〜1998年）**――複製の存在は定められていましたが、変更をいつ知らせ、何を送るかは詰まっていませんでした。変更の通知と、差分だけを送る転送が追加されます。存在しないという答えを再利用する仕組みも入りました。

**拡張の余地を作る（1999〜2013年）**――メッセージの長さの上限が、新しい情報を運ぶ妨げになります。互いの能力を通知し合う拡張が導入されました。世界中の実装を一斉に更新できないため、この拡張自体が段階的に広まる必要がありました。

**応答を信用する（2005年）**――返ってきた答えが本当にその名前の管理者に由来するかを確かめる手段がありませんでした。署名による出所の認証と改ざんの検出が追加されます。ただし通信の内容を隠す仕組みではありません。

**悪用への耐性（2008〜2010年）**――偽の応答を受け入れてしまう余地と、他人への攻撃の踏み台にされる問題が顕在化します。応答の受け入れ条件を厳しくし、誰に対して問い合わせを受け付けるかを制限する運用が広まりました。

**見られていることへの対処（2016〜2022年）**――問い合わせの内容が経路上で見えることが問題として扱われるようになります。通信の暗号化と、相手へ渡す名前を必要な範囲に絞る方法が追加されました。暗号化しても、問い合わせ先そのものには内容が見えます。

**壊れても答え続ける（2020年）**――上流に到達できないとき、期限切れと分かっているデータを返して応答を続けることが認められました。1987年にTTLへ預けた「最新性をどこまで譲るか」という判断が、33年後に動かされたことになります。

## この整理は後から行ったものです

時代の区切りと要件の名前は、本書が後から与えた整理です。当時の文書が同じ言葉で要件を掲げていたわけではありません。また標準化は並行して進むため、時代の期間は互いに重なります。署名の議論は1997年から2005年まで、拡張の議論は1999年から2013年まで続いており、順番に並んでいたわけではありません。

## どの章がどこを扱うか

この章は索引としても使えます。

| 時代 | 足されたもの | 詳しく扱う章 |
| --- | --- | --- |
| 集中管理が始まる | 中央の一覧、登録の受付 | [第2章 拡張性](02-scalability.md) |
| 分散への転換 | 階層と委譲、問い合わせとキャッシュ、複製 | [第2章 拡張性](02-scalability.md)、第3章 性能、第4章 可用性と障害耐性 |
| 隙間を埋める | 変更通知、差分転送、不在応答の再利用 | 第3章 性能、第4章 可用性と障害耐性、第5章 整合性と変更反映 |
| 拡張の余地を作る | 能力の通知、メッセージ長の拡張 | 第9章 後方互換性と発展性 |
| 応答を信用する | 署名による出所認証 | 第6章 セキュリティ、第8章 運用性と保守性、第9章 後方互換性と発展性 |
| 悪用への耐性 | 受け入れ条件の厳格化、提供先の制限 | 第6章 セキュリティ、第4章 可用性と障害耐性 |
| 見られていることへの対処 | 通信の暗号化、開示する名前の最小化 | 第7章 プライバシー、第8章 運用性と保守性 |
| 壊れても答え続ける | 期限切れデータの利用 | 第4章 可用性と障害耐性、第3章 性能、第5章 整合性と変更反映 |

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
- [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) 本書の用語の基準。

---

[← 前の章 第0章 DNSはなぜ複雑に見えるのか](00-introduction.md)｜[目次](../)｜[次の章 → 第2章 拡張性](02-scalability.md)
