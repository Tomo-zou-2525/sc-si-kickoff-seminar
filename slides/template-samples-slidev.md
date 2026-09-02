---
# presentation-templates.md の全パターンを Slidev スライド化したサンプル集です。
# 起動: npm run dev -- template-samples-slidev.md
#       （このプロジェクトは Slidev。既定は slides.md なのでファイル名を指定して起動します）
theme: default
title: テンプレート全パターン（Slidev版）
class: text-center
transition: slide-left
mdc: true
# デザインシステム（テンプレートの共通スタイルを Slidev 全体に適用）
# 明朝体は使わない／背景は白／文字は #333333／メインカラー1色 #0b2f64 のみ／角丸・影・下線は使わない
# 注意: style ブロック内では CSS コメント（/* */）を使わない（mdc パースが崩れるため）
style: |
  .slidev-layout {
    font-family: "Yu Gothic", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    background-color: #ffffff;
    color: #333333;
    line-height: 1.6;
  }
  .slidev-layout strong { color: #0b2f64; font-weight: bold; }
  .slidev-layout h1, .slidev-layout h2, .slidev-layout h3 { color: #0b2f64; }
  .large-number {
    font-family: "Helvetica", sans-serif;
    font-weight: bold;
    color: #0b2f64;
  }
  .bordered-box {
    border: 3px solid #0b2f64;
    border-radius: 0;
    padding: 20px;
    background: transparent;
  }
---

<!-- ===== パターン1：表紙 (Cover) ===== -->
<!-- 表紙のみ中央揃えを許容。余計な図形・グラデ・ビビッドな色は排除 -->

<div class="pt-20"></div>

# バーサウナ会員権のご紹介

### 〜原点にしてパーフェクトなサウナ体験〜

<hr class="border-0 h-px bg-gray-300 w-3/5 mx-auto my-6" />

<div class="text-sm text-gray-500">
Presented by Gemini Notebook / 2026.08.30
</div>

---
layout: default
---

<!-- ===== パターン2-A：区切り（目次型・現在地ハイライト） ===== -->

# 目次

<div class="text-left mt-6">

- <span class="opacity-30">Part 1. 既存のサウナにおける課題</span>
- **Part 2. バーサウナが提供する価値（本編）**
- <span class="opacity-30">Part 3. ご利用プランと会員特典</span>

</div>

---
layout: center
---

<!-- ===== パターン2-B：区切り（シンプル枠囲み型） ===== -->
<!-- 角丸なし・塗りつぶしなし・影なしを厳守 -->

<div class="bordered-box text-center">

# Part 2. バーサウナのコンセプト

</div>

---
layout: default
---

<!-- ===== パターン3-A：タイトルあり（箇条書き） ===== -->
<!-- タイトルに結論（ワンメッセージ）。最も見せたい1箇所だけ太字 -->

## 既存のサウナには「整う」を阻害する多くの不満がある

<div class="text-left mt-4">

- 混雑していて自分のペースでサウナに入れない
- 水風呂がぬるく、温度管理が徹底されていない
- **サウナ室の温度にムラがあり、身体の芯まで温まらない**

</div>

---
layout: default
---

<!-- ===== パターン3-B：タイトルあり（文字と画像・横並び） ===== -->

## プライベート空間が「100%の整い」を約束する

<div class="grid grid-cols-2 gap-8 items-center mt-4">

<div class="text-left">

### 完全個室サウナのこだわり

- 他人の目を一切気にせず、自分だけの世界に没入できる
- サウナ室の温度・湿度を自分好みに完全カスタマイズ可能
- **水風呂、ととのいスペースまでをシームレスに独占**

</div>

<div class="text-center">

<!-- 画像は比率維持（object-cover）・角丸なし -->
<img src="/sauna-room.jpg" alt="プライベートサウナ室のイメージ" class="w-full max-h-75 object-cover rounded-none" />

</div>

</div>

---
layout: default
---

<!-- ===== パターン3-C：タイトルあり（数字強調） ===== -->

## 体験者のほぼ全員が「また利用したい」と回答

<div class="text-left mt-8">
  <span class="large-number text-8xl">98</span>
  <span class="text-3xl font-bold ml-1">%</span>
</div>

### 会員の満足度は驚異的な数値を記録

<div class="text-left">

- 事後アンケートにおいて、従来のサウナで感じていた「不満」が100%解消されたと回答。

</div>

---
layout: default
---

<!-- ===== パターン3-D：タイトルあり（プロセス・流れ） ===== -->
<!-- 矢印の代わりに三角形（▲）を使用 -->

## 3つのステップをシームレスに繋ぐことで、究極の「整い」へ

<div class="grid grid-cols-[1fr_auto_1fr_auto_1fr] gap-2 items-center mt-8 text-center">

<div class="border-2 border-[#0b2f64] p-5">

### STEP 1

**サウナ室**
最高峰の熱気で身体の芯から温まる

</div>

<div class="text-2xl text-[#0b2f64]">▲</div>

<div class="border-2 border-[#0b2f64] p-5">

### STEP 2

**水風呂**
徹底管理された冷水で一気に引き締める

</div>

<div class="text-2xl text-[#0b2f64]">▲</div>

<div class="border-2 border-[#0b2f64] p-5">

### STEP 3

**ととのい席**
静寂に包まれた極上のチルタイム

</div>

</div>

---
layout: center
class: text-center
---

<!-- ===== パターン4-A：タイトルなし（文字だけ・ワンメッセージ） ===== -->
<!-- 話の転換点で使う。文字数は極限まで削る。使いすぎない -->

# **「あなたの整うは、本当に100点ですか？」**

---

<!-- ===== パターン4-B：タイトルなし（画像背景＋透過文字） ===== -->
<!-- 画像の上に黒の透過レイヤーを重ね、白文字で可読性を確保。この面のみ白文字を許可 -->

<div class="absolute inset-0 flex flex-col items-center justify-center text-center text-white px-12" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/sauna-bg.jpg'); background-size: cover; background-position: center;">
  <h1 class="!text-white">原点にしてパーフェクトなサウナ体験</h1>
  <h3 class="!text-white">「バーサウナ」</h3>
</div>

---
layout: default
---

<!-- ===== パターン4-C：タイトルなし（余白パターン・最高峰） ===== -->
<!-- 半分に余白のある画像、もう半分に極めて短いメッセージ -->

<div class="grid grid-cols-2 gap-8 items-center h-full">

<div class="text-left pl-6">

# 整う、語らう。
# プライベートサウナ。

</div>

<div class="text-right">

<img src="/sauna-chill.jpg" alt="チルスペースのイメージ" class="w-full h-auto rounded-none" />

</div>

</div>
