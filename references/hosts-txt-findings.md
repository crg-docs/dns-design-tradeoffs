# HOSTS.TXT期の一次資料からの抽出

第2章（拡張性）のTODO 5件について、一次資料を実読した結果を記録する（#4、2026-08-05）。原文はRFC Editorで配布されているテキストを直接読み、要約を経由していない。

引用は原文のまま示し、訳は本書の解釈として区別する。**該当記述なしも結論として扱う。**

判断待ちの項目は #5 で決める。

## 結論の一覧

| TODO | 結論 | 主な資料 |
| --- | --- | --- |
| :21 HOSTS.TXT以前の識別方法 | **一次資料あり。しかも同時代の一人称記録** | RFC 606（1973年12月） |
| :45 転送量・更新頻度・ホスト数の数値 | **該当記述なし。数値はどのRFCにも存在しない** | 606/608/810/952/882/921 を全文検索 |
| :51 当時の登録工程と負荷 | **一次資料あり** | RFC 810（1982年）、RFC 952（1985年） |
| :57 名前衝突と一意性 | **一次資料あり。ただし衝突の実例や頻度はなし** | RFC 921（1984年10月） |
| :74 移行期の仕組み | **一次資料あり。具体的な互換措置が明記されている** | RFC 921（1984年10月） |

## :21 HOSTS.TXT以前に、ホストはどう識別・参照されたか

RFC 606（L. P. Deutsch、1973年12月、Legacy Stream）は、集中した機械可読の表が**まだ無かった時点**の状況を一人称で書いている。回顧ではなく同時代の記録である。

> Now that we finally have an official list of host names, it seems about time to put an end to the absurd situation where each site on the network must maintain a different, generally out-of-date, host list for the use of its own operating system or user programs.

> For example, each of the TENEX sites to which I have access ( SRI-ARC, BBN-TENEX, USC-ISI, and PARC-MAXC) has a slightly different mapping between host names and host addresses: none is complete, and I believe each one differs in some way from the official List.

本書にとっての意味は大きい。**集中管理は、それ自体がより悪い分散状態への対処だった。** 公式の一覧は存在したが機械可読の形でネットワーク越しに取得できず、各サイトが自前の表を手で維持し、どれも不完全で互いに食い違っていた。

したがって第2章は「集中管理は悪い」という筋では書けない。集中→分散ではなく、**不統一な分散 → 集中 → 委譲による分散**という三段の話になる。RFC 606 が求めた「一つの正しい表」は実際に作られ、機能し、そして規模の増大で限界に達した。

RFC 608（M. D. Kudlick、SRI-ARC、1974年1月10日、RFC 810により廃止）がNIC側の応答で、実装を引き受けている。

> A program to generate an up to date version of the ASCII file needs to be written at the NIC, and run periodically (weekly, or as the situation warrants).

更新が**週次のバッチ生成**として想定されていたことが分かる。

## :45 転送量、更新頻度、ホスト数の具体値

**該当記述なし。** RFC 606、608、810、952、882、921 を全文検索したが、ホスト数、ファイルサイズ、転送量の数値はいずれにも存在しない。

RFC 882（1983年11月）は問題を規模の言葉で述べるが、数値を示さない。

> The size of this table, and especially the frequency of updates to the table are near the limit of manageability.

なおRFC 1034（1987年）2.1節の「配布に要する総帯域はホスト数の二乗に比例する」という記述は、**RFC 882には存在しない**。1983年の同時代文書にはなく、1987年の回顧で加わった定式化である。実測値としても、当時の文書の主張としても扱えない。

## :51 当時の登録工程と負荷

RFC 810（1982年3月、RFC 952により廃止）の ASSUMPTIONS 第7項。

> Names and Addresses for DoD networks, gateways, and hosts will be negotiated and registered with the Network Information Center (NIC@SRI-NIC or (415) 859-4775) before being used and before traffic is passed by a DoD host.

工程の性質がここに出ている。**名前を使う前にNICと交渉して登録する**必要があり、連絡手段として電子メールアドレスと並んで**電話番号**が書かれている。登録は自動化された手続きではなく、人を介した調整だった。

取得側の工程は同じ文書に書かれている。

> It can be obtained by connecting to host SRI-NIC (10.0.0.73) from your local FTP server, logging in as user=ANONYMOUS, password=GUEST, and doing a 'get' on <NETINFO>HOSTS.TXT.

さらに利用側の負担も明記されている（ASSUMPTIONS 第6項）。

> It is the responsibility of the user using this host table to translate it into whatever format is needed for his or her purposes.

RFC 952（1985年10月）では取得手段としてHostname Server（RFC 953）が併記され、そちらが速いとされている。

> The same table may also be obtained via the NIC Hostname Server, as described in RFC-953. The latter method is faster and easier, but requires a user program to make the necessary connection to the Name Server.

**負荷そのものの定量的な記述はない。** 工程は書けるが、それがどれほど重かったかを数値で語ることはできない。

## :57 名前衝突と一意性

RFC 921（J. Postel、1984年10月、IABとDARPAの公式方針、RFC 897とRFC 881を更新）が、一意性の担保をどう変えるかを正面から書いている。

> The names are being changed from simple names, or globally unique strings, to structured names, where each component name is unique only with respect to the superior component name.

> Until recently, hosts in the DARPA research and DDN operational communities were assigned names in a flat or global name space of character strings.

これは第2章7節の主張（階層化によって一意性を部分木ごとの責任へ分解する）を、同時代の方針文書がそのまま述べているものである。本書の後付けの解釈ではない。

一方で、**衝突の実例や発生頻度を示す記述はない。** 平坦な名前空間で中央が一意性を調整していたことは書けるが、「実際にこういう衝突が起きた」とは一次資料からは書けない。

RFC 952（1985年）には命名規則があり、これは調整を規則で代替する試みとして読める。

> The first character must be an alpha character. The last character must not be a minus sign or period. (...) Single character names or nicknames are not allowed.

用途を名前に埋め込む規約もある。

> A host which serves as a GATEWAY should have "-GATEWAY" or "-GW" as part of its name.

平坦な名前空間では、名前の中に役割や所属を押し込む圧力がかかる。RFC 882 の設計目標「names should not contain addresses, routes, or similar information as part of the name」と対照して読める。

## :74 移行期の仕組み

RFC 921 に具体的な互換措置が書かれている。

> Actually, the situation is a bit more complicated, of course. Hosts are already using domain style names under the constraint that their domain style name is exactly their old style name with the string ".ARPA" appended. The first transition step is to ensure that all hosts do this, and then to eliminate the use of old style names.

**旧名に `.ARPA` を付けたものを新しい名前とする**という制約が、移行の第一段だった。名前空間を作り直すのではなく、既存の名前を新しい構造の中へ機械的に写し込んでいる。

ファイルの入れ替えも段階的である。

> At this point a version of the host table which includes the domain style names is made available (DHOSTS.TXT).

> At this point all hosts should start using their domain style names as their official and primary names. The standard table of host names contains domain style names as the official and primary name (DHOSTS.TXT becomes HOSTS.TXT).

新形式を別名のファイル（DHOSTS.TXT）で並行提供し、期日に本名（HOSTS.TXT）と入れ替える。旧版は OHOSTS.TXT として残された。**表の形式そのものを二重化して移行している。**

なお同文書は、旧来の実装が新形式に追従できないことを率直に書いている。

> It is likely that the NIC will enter these new domain style names in the centrally maintained table (i.e., HOSTS.TXT) during the transition period. It is unlikely that a backward host can hack this at all.

RFC 921 は自らの前身であるRFC 881の予定が守られなかったことも記録している。

> \<This was done, but the schedule did not work.\>

移行が計画通りに進まなかったことを、当事者の文書が明示している。第9章（後方互換性と発展性）で「段階的導入は予定通りに終わらない」を扱うときの一次資料になる。

## 本書の構成に対する影響

1. **第2章の筋が変わる。** 「集中管理の限界」から始めるのではなく、集中管理が何を解決したかから始める必要がある（:21の発見）。RFC 606 の「absurd situation」は、NICを待つ場面と並ぶもう一つの場面として使える。
2. **第1章の年表に1973年と1974年を加える。** RFC 606/608 が機械可読なホスト表の起点である。1984年のRFC 921（移行スケジュール）も年表に加える。
3. **数値は使えない。** :45 は「数値を出さず、二乗則はRFC 1034の見積りとして紹介する」で畳むほかない。
4. **RFC 921 は第9章でも使う。** 予定が守られなかったことを当事者が記録した資料として。

## 追加で登録が必要な資料

`sources.md` へ以下を追加する。

- RFC 606 Host Names On-line（1973年12月、Legacy Stream）
- RFC 608 Host Names On-Line（1974年1月、RFC 810により廃止）
- RFC 921 Domain Name System Implementation Schedule - Revised（1984年10月、RFC 897とRFC 881を更新）

未確認のまま残すもの。

- RFC 597（RFC 606が参照する「公式ホスト名一覧」）は未読。RFC 606 以前の一覧の形態を確認する場合に読む。
- RFC 881、RFC 897（RFC 921の前身のスケジュール）は未読。移行が守られなかった経緯を詳しく書く場合に読む。
- RFC 920（新ドメインの登録要件）は未読。トップレベルドメインの設計を扱う場合に読む。
