<!--
  presentation-templates.md の全パターンを Marp スライド化したサンプル集です。
  プレビュー: VS Code の Marp 拡張、または `npx @marp-team/marp-cli template-samples.md -o out.html`
  ※ このプロジェクトの slides.md は Slidev ですが、テンプレートは Marp 前提のため
    混在を避けてこのファイルは独立した Marp ファイルとして作成しています。
-->
---
marp: true
theme: default
size: 16:9
paginate: true
style: |
  /* 1. フォント：明朝体は使わない。ゴシック体一択 */
  section {
    font-family: "Yu Gothic", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    background-color: #ffffff;  /* 背景は白 */
    color: #333333;             /* 真っ黒は使わず #333333 */
    font-size: 28px;
    padding: 60px;              /* 余白を確保 */
  }
  /* 2行以上の文章は左揃え（中央揃え禁止） */
  p, ul, ol {
    text-align: left;
    line-height: 1.6;
  }
  /* 強調は太字＋メインカラー1色のみ。下線は使わない */
  strong {
    color: #0b2f64;
    font-weight: bold;
  }
  /* 数字は Helvetica */
  .large-number {
    font-family: "Helvetica", sans-serif;
    font-weight: bold;
    color: #0b2f64;
  }
  /* 図形：角丸にしない・塗りつぶさない・影なし */
  .bordered-box {
    border: 3px solid #0b2f64;
    border-radius: 0px;
    padding: 20px;
    background: transparent;
  }
---

<!-- _paginate: false -->
<!-- ===== パターン1：表紙 (Cover) ===== -->
<div align="center">

<br><br>

# バーサウナ会員権のご紹介
### 〜原点にしてパーフェクトなサウナ体験〜

<br>

<hr style="border: 0; height: 1px; background: #cccccc; width: 60%; margin: 20px auto;">

<span style="font-size: 0.7em; color: #666666;">
Presented by Gemini Notebook / 2026.08.30
</span>

</div>

---

<!-- ===== パターン2-A：区切り（目次型・現在地ハイライト） ===== -->

# 目次

- <span style="opacity: 0.3;">Part 1. 既存のサウナにおける課題</span>
- **Part 2. バーサウナが提供する価値（本編）**
- <span style="opacity: 0.3;">Part 3. ご利用プランと会員特典</span>

---

<!-- ===== パターン2-B：区切り（シンプル枠囲み型） ===== -->
<div class="bordered-box" style="margin-top: 100px; text-align: center;">

# Part 2. バーサウナのコンセプト

</div>

---

<!-- ===== パターン3-A：タイトルあり（箇条書き） ===== -->

## 既存のサウナには「整う」を阻害する多くの不満がある

- 混雑していて自分のペースでサウナに入れない
- 水風呂がぬるく、温度管理が徹底されていない
- **サウナ室の温度にムラがあり、身体の芯まで温まらない**

---

<!-- ===== パターン3-B：タイトルあり（文字と画像・横並び） ===== -->

## プライベート空間が「100%の整い」を約束する

<table style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none;">
<td style="width: 50%; border: none; padding-right: 20px; vertical-align: top;">

### 完全個室サウナのこだわり
- 他人の目を一切気にせず、自分だけの世界に没入できる
- サウナ室の温度・湿度を自分好みに完全カスタマイズ可能
- **水風呂、ととのいスペースまでをシームレスに独占**

</td>
<td style="width: 50%; border: none; text-align: center; vertical-align: middle;">

<img src="images/sauna-room.jpg" alt="プライベートサウナ室のイメージ" style="width: 100%; max-height: 300px; object-fit: cover; border-radius: 0;">

</td>
</tr>
</table>

---

<!-- ===== パターン3-C：タイトルあり（数字強調） ===== -->

## 体験者のほぼ全員が「また利用したい」と回答

<div style="text-align: left; margin-top: 40px;">
  <span class="large-number" style="font-size: 5em;">98</span>
  <span style="font-size: 1.8em; font-weight: bold; margin-left: 5px;">%</span>
</div>

### 会員の満足度は驚異的な数値を記録
- 事後アンケートにおいて、従来のサウナで感じていた「不満」が100%解消されたと回答。

---

<!-- ===== パターン3-D：タイトルあり（プロセス・流れ） ===== -->

## 3つのステップをシームレスに繋ぐことで、究極の「整い」へ

<table style="width: 100%; border: none; border-collapse: collapse; text-align: center;">
<tr style="border: none;">
<td style="width: 30%; border: 2px solid #0b2f64; padding: 20px; vertical-align: top;">

### STEP 1
**サウナ室**
最高峰の熱気で身体の芯から温まる
</td>
<td style="width: 5%; border: none; font-size: 1.5em; color: #0b2f64; vertical-align: middle;">▲</td>
<td style="width: 30%; border: 2px solid #0b2f64; padding: 20px; vertical-align: top;">

### STEP 2
**水風呂**
徹底管理された冷水で一気に引き締める
</td>
<td style="width: 5%; border: none; font-size: 1.5em; color: #0b2f64; vertical-align: middle;">▲</td>
<td style="width: 30%; border: 2px solid #0b2f64; padding: 20px; vertical-align: top;">

### STEP 3
**ととのい席**
静寂に包まれた極上のチルタイム
</td>
</tr>
</table>

---

<!-- ===== パターン4-A：タイトルなし（文字だけ・ワンメッセージ） ===== -->
<!-- _paginate: false -->

<div align="center" style="margin-top: 150px;">

# **「あなたの整うは、本当に100点ですか？」**

</div>

---

<!-- ===== パターン4-B：タイトルなし（画像背景＋透過文字） ===== -->
<!-- _paginate: false -->

<div style="
  background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('images/sauna-bg.jpg');
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100%;
  padding: 100px 50px;
  box-sizing: border-box;
  color: #ffffff;
  text-align: center;
">

# 原点にしてパーフェクトなサウナ体験

### **「バーサウナ」**

</div>

---

<!-- ===== パターン4-C：タイトルなし（余白パターン・最高峰） ===== -->
<!-- _paginate: false -->

<table style="width: 100%; height: 100%; border: none; border-collapse: collapse;">
<tr style="border: none;">
<td style="width: 50%; border: none; padding: 40px; vertical-align: middle;">

# 整う、語らう。
# プライベートサウナ。

</td>
<td style="width: 50%; border: none; text-align: right; vertical-align: middle; padding: 0;">

<img src="images/sauna-chill.jpg" alt="チルスペースのイメージ" style="width: 100%; height: auto; border-radius: 0;">

</td>
</tr>
</table>
