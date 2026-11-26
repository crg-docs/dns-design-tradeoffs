---
layout: default
---

# 第6章 セキュリティ――何を、誰から守るのか

応答が速く、止まらず、更新も行き渡る。それでも、その応答が攻撃者の指定した接続先なら、ここまでの改善は誤った情報を効率よく配る仕組みになってしまいます。

ただし「DNSを安全にする」という一つの設定はありません。偽の回答を受け入れないこと、管理者以外に書き換えさせないこと、通信内容を見せないこと、サービスを攻撃の踏み台にしないことは、異なる要件です。本章は最初の二つと資源の保護を扱い、通信内容の開示は第7章へつなぎます。

## 1. 守る対象と攻撃者の位置を決める

例えば、通信経路を見ることのできない攻撃者が、再帰リゾルバへ偽の応答を送り込む場合があります。一方で、管理用アカウントを奪って正規の更新経路からレコードを変える場合もあります。後者のデータに正規の署名が付けば、署名だけで管理者の意図との違いは見抜けません。RFC 3833は、応答の偽造、データの改変、サービス妨害などを異なる脅威として整理しています。[RFC 3833: Threat Analysis of the Domain Name System (DNS) 2節](https://www.rfc-editor.org/rfc/rfc3833.html)

本書では、保護対象を回答データ、更新権限、サービスの処理資源に分けます。さらに攻撃者が経路を観測できるのか、管理権限を持つのかを明示します。同じ「偽造を防ぐ」でも、推測を難しくする対策と暗号学的にデータを検証する対策では、前提が違います。

## 2. 名前を調べた結果を差し替えられたくない

名前解決の結果は、その後に接続する相手を左右します。しかもキャッシュへ偽の回答が入ると、同じ情報を使う後の利用者にも影響します。問い合わせに答えてもらうだけでなく、その答えを受け入れてよいかを確認する要件が必要になります。

DNSでは、まず応答が実際の問い合わせに対応するかを照合し、経路外の攻撃者が必要な値を推測しにくくする対策が採られています。これは偽の応答を紛れ込ませにくくする解決ですが、問い合わせを観測できる相手に対して、情報の出所まで証明するものではありません。[RFC 5452 9節](https://www.rfc-editor.org/rfc/rfc5452.html)

さらに出所と改変の有無を確かめるため、DNSSECは回答データに署名を付け、信頼の起点から検証できるようにしました。途中の通信相手を確認するだけでなく、手元へ届いたデータを検証する設計です。問い合わせ内容を隠す暗号化とは、守る対象が違います。DNSの複製や再利用を使いながら、取得経路だけに出所の判断を頼らないための解決として読めます。[RFC 4033 4節](https://www.rfc-editor.org/rfc/rfc4033.html)

応答を照合する項目と受け入れ規則は[準備章：回答の照合とキャッシュへの受け入れ](01-name-resolution.md#回答の照合とキャッシュへの受け入れ)、署名・鍵・親子関係の仕組みは[準備章：DNSSECの署名と信頼の連鎖](01-name-resolution.md#dnssecの署名と信頼の連鎖)にまとめています。

## 3. 検証できないときも答えてよいのか

正しい出所を確認したいなら、確認できない答えをどうするかも決めなければなりません。返せる答えを増やすことと、求める保護を満たすことは同じではありません。

特に、通常のDNSSEC検証と「対象の回答は必ずSecureでなければ使わない」という利用側の方針は異なります。署名の保護がないと判断できた情報を返す場合と、保護されるはずなのに検証に失敗した場合を区別します。検証結果を一つの「成功・失敗」に潰すと、どの保証を必要としているかが見えなくなります。状態の定義と応答の扱いは[準備章：DNSSECの検証結果](01-name-resolution.md#dnssecの検証結果)で確認できます。

また、署名を使うと、鍵や署名の保守が失敗した場合にも情報を利用できなくなり得ます。攻撃がなくても、期限切れや親子の情報の不整合で要件を満たせなくなるためです。DNSSECを有効にした時点で終わりではなく、保護を維持できることが運用上の条件になります。[RFC 6781 4節](https://www.rfc-editor.org/rfc/rfc6781.html)

失敗したら検証を外して応答を得る、という方法では、もとの要求を取り下げたことになります。必要な保護を残して復旧するには、署名や鍵の状態を確認できることが必要です。期限と更新の詳細は[準備章：署名の期限と保守](01-name-resolution.md#署名の期限と保守)へ置いています。

## 4. 正規の仕組みで誤った情報を登録されたらどうするか

署名で出所を確かめても、管理者のアカウントを奪って登録された値や、誤操作で登録された値まで見抜けるわけではありません。名前を利用する側の検証とは別に、情報を変更できる人と範囲を制限する要件があります。

DNSの動的更新や転送では、相手とメッセージを認証する仕組みとしてTSIGが使えます。ただし、誰から来たかを確かめることと、その人に何を許すかは別です。必要な範囲だけを更新できる権限、秘密を管理する担当、失効・交換の方法を合わせて用意します。TSIGの仕組みと保護範囲は[準備章：更新の認証とTSIG](01-name-resolution.md#更新の認証とtsig)にまとめています。

このように、受け取る答えの改変を防ぐことと、正規の更新経路を守ることでは、解決する場所が違います。「安全なDNS」という一つの設定へまとめず、どこで要求が破られ得るかを考える必要があります。

## 5. 必要な利用者へ提供しながら悪用を抑えたい

公開された名前の情報を返すことと、誰の依頼でも代わりに探索を引き受けることは違います。DNSの再帰処理を意図した利用者へ限定する対策は、後者の仕事を悪用されにくくする解決です。応答量を制限する方法もありますが、強すぎる制限は正当な利用を妨げ得ます。[RFC 5358 3・4節](https://www.rfc-editor.org/rfc/rfc5358.html)

可用性を求めて処理能力を増やすだけでは、誰にその能力を使わせるかは決まりません。偽造された回答、権限外の変更、資源の悪用を分け、それぞれに対策と評価対象を対応させることが、この章で学ぶ設計です。公開範囲と応答量の具体策は[準備章：再帰サービスの制限と応答量](01-name-resolution.md#再帰サービスの制限と応答量)で確認できます。本書では攻撃・負荷試験は行っておらず、特定の構成で防御が成功したという実測結果は示しません。

## この章のポイント

- DNSSECはデータの出所と完全性を検証する仕組みで、問い合わせ内容を秘匿するものではありません。
- 署名を検証できても、登録値が管理者の意図どおりかは別の確認が必要です。
- 相手の認証、変更を許す範囲、再帰処理を提供する範囲は、それぞれ分けて設計します。

## 参照資料

- [RFC 3833: Threat Analysis of the Domain Name System (DNS)](https://www.rfc-editor.org/rfc/rfc3833.html) 2節
- [RFC 5452: Measures for Making DNS More Resilient against Forged Answers](https://www.rfc-editor.org/rfc/rfc5452.html) 9節
- [RFC 9499: DNS Terminology](https://www.rfc-editor.org/rfc/rfc9499.html) Bailiwick
- [RFC 2181: Clarifications to the DNS Specification](https://www.rfc-editor.org/rfc/rfc2181.html) 5.4.1節
- [RFC 4033: DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033.html) 4・5・8節
- [RFC 4034: Resource Records for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4034.html) 2・3・5節
- [RFC 4035: Protocol Modifications for the DNS Security Extensions](https://www.rfc-editor.org/rfc/rfc4035.html) 4.3・4.9.3・5.3.3・5.5節
- [RFC 6840: Clarifications and Implementation Notes for DNS Security (DNSSEC)](https://www.rfc-editor.org/rfc/rfc6840.html) 5.7・5.8節
- [RFC 6781: DNSSEC Operational Practices, Version 2](https://www.rfc-editor.org/rfc/rfc6781.html) 4節
- [RFC 8945: Secret Key Transaction Authentication for DNS (TSIG)](https://www.rfc-editor.org/rfc/rfc8945.html)
- [RFC 5358: Preventing Use of Recursive Nameservers in Reflector Attacks](https://www.rfc-editor.org/rfc/rfc5358.html) 3・4節
- [BIND 9.20.16: rate-limit](https://bind9.readthedocs.io/en/v9.20.16/reference.html#namedconf-statement-rate-limit)

本文の構成と範囲: [文書設計メモ](../docs/document-design/06-security.md)

---

[← 第5章 整合性と変更反映](05-consistency.md)｜[目次](../)｜[第7章 プライバシー →](07-privacy.md)

{% include mermaid.html %}
