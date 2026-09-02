# Markdown テンプレート集

本ファイルは、動画**『【パワポ】技術不要！誰でも「見やすい」「伝わる資料」がつくれる7つのコツ』**で提唱されているスライド作成の原則とやってはいけない禁忌（NG）を徹底的に反映し、Markdown（Marp等のスライド作成ツールや構成案作成）でそのまま、あるいはコピペで応用できるように体系化した実用フォーマット集です。

---

## 🎨 デザインシステム前提ルール（共通スタイル定義）

動画の「フォント・色・図形」の原則をCSS/Markdownに落とし込んだ基本設定です。スライドツール（Marp等）を使う場合は、以下のフロントマター（設定）を先頭に記述することを推奨します。

```yaml
---
marp: true
theme: default
size: 16:9
style: |
  /* 1. フォント：明朝体は一生使わない。ゴシック体一択 */
  section {
    font-family: "Yu Gothic", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    background-color: #ffffff; /* 2. 背景は基本「白」 */
    color: #333333;           /* 3. 真っ黒(#000000)は絶対使わない。目が疲れない#333333を指定 */
    font-size: 28px;
    padding: 60px;            /* 4. 余白の概念：ギリギリに配置しない */
  }
  
  /* 2行以上の文章は左揃えにする（中央揃え禁止） */
  p, ul, ol {
    text-align: left;
    line-height: 1.6;        /* 行間は少しあける */
  }

  /* 強調スタイル：デフォルトの下線（uタグ等）はリンクに見えるため使用禁止。太字のみ */
  strong {
    color: #0b2f64;          /* 文字の黒以外に使うのは「メインカラー1色」のみ。例として濃い紺色 */
    font-weight: bold;
  }

  /* 数字フォント：どのパソコンにも入っている「Helvetica」を使用 */
  .large-number {
    font-family: "Helvetica", sans-serif;
    font-weight: bold;
    color: #0b2f64;          /* メインカラー */
  }

  /* 図形：角丸にしない、塗りつぶさない（枠線だけ）、シャドウ（影）は使わない */
  .bordered-box {
    border: 3px solid #0b2f64;
    border-radius: 0px;      /* 角を丸めない（四角のまま） */
    padding: 20px;
    background: transparent;  /* 塗りつぶさない */
  }
---
```

---

## 🗂️ スライド4分類＆全パターン・テンプレート

すべてのスライド資料は**「表紙」「区切り」「タイトルあり」「タイトルなし」**の4つの組み合わせで完成します。

---

### パターン 1：表紙 (Cover)
> **動画の指摘：**
> 素人が表紙を凝るのは時間の無駄。極めてシンプルに作る。中央揃えは「表紙のみ、文字数が少ない場合」に限り許容。
> リッチ感を出したいなら「細い防線」と「意味のない（リッチ感用の）日付や名前」を小さく配置する。

```markdown
<!-- slide: 表紙 -->
<div align="center">

<br><br>

# バーサウナ会員権のご紹介
### 〜原点にしてパーフェクトなサウナ体験〜

<br>

<!-- リッチ感を出すための薄く細い水平線 -->
<hr style="border: 0; height: 1px; background: #cccccc; width: 60%; margin: 20px auto;">

<!-- 小さい文字で日付や名前を配置 -->
<span style="font-size: 0.7em; color: #666666;">
Presented by Gemini Notebook / 2026.08.30
</span>

</div>

<!-- 
💡 解説：
- 表紙なので中央揃え（align="center"）を使用しています。
- 余計な図形やグラデーション、極端にビビッドな色は排除しています。
-->
```

---

### パターン 2：区切り (Section Divider)
> **動画の指摘：**
> スライド枚数が多い場合は、途中で入れると圧倒的に見やすくなる。
> 目次として使う場合は「今話しているパートだけを強調し、それ以外は透過（薄く）させる」ことで、聞き手に現在地を伝える。

#### A. 目次型（現在地ハイライト）
```markdown
---
<!-- slide: 区切り（目次型） -->

# 目次

- <span style="opacity: 0.3;">Part 1. 既存のサウナにおける課題</span>
- **Part 2. バーサウナが提供する価値（本編）**
- <span style="opacity: 0.3;">Part 3. ご利用プランと会員特典</span>

<!-- 
💡 解説：
- 今話している「Part 2」だけを太字かつメインカラーで強調し、他を opacity: 0.3 で等化（透過）させています。
-->
```

#### B. シンプル枠囲み型
```markdown
---
<!-- slide: 区切り（枠囲み型） -->
<div class="bordered-box" style="margin-top: 100px; text-align: center;">

# Part 2. バーサウナのコンセプト

</div>

<!-- 
💡 解説：
- 四角形の図形（枠線）を使っていますが、動画のルール通り「角は丸めない」「塗りつぶさない」「シャドウはつけない」を厳守しています。
-->
```

---

### パターン 3：タイトルあり (Standard with Title)
> **動画の指摘：**
> 一番よく使われるフォーマット。
> 「ワンスライド・ワンメッセージ（パッと見2秒で意味がわかること）」を徹底。
> H2見出し部分に「要は何か（最も言いたいこと）」を直接書く。

#### A. 箇条書きパターン
```markdown
---
<!-- slide: タイトルあり（箇条書き） -->

## 既存のサウナには「整う」を阻害する多くの原点（不満）がある
<!-- ↑ ここにスライドで一番言いたいワンメッセージ（解釈・結論）を直接書く -->

- 混雑していて自分のペースでサウナに入れない
- 水風呂がぬるく、温度管理が徹底されていない
- **サウナ室の温度にムラがあり、身体の芯まで温まらない**
  <!-- ↑ 並列する情報のなかで、最も見てほしい1箇所のみを太字で強調する -->

<!-- 
💡 解説：
- 「サウナにまつわる悩み」といった曖昧なタイトル（何について）ではなく、結論（何が言いたいか）をタイトルにしています。
- 長文は書かず、箇条書きでシンプルにまとめ、中央揃えにせず左揃えにしています。
-->
```

#### B. 文字と画像（横並び）パターン
```markdown
---
<!-- slide: タイトルあり（文字と画像） -->

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

<!-- 画像の比率は絶対に変えない。人の顔を入れない（または首から下をクロップ） -->
<img src="images/sauna-room.jpg" alt="プライベートサウナ室のイメージ" style="width: 100%; max-height: 300px; object-fit: cover; border-radius: 0;">

</td>
</tr>
</table>

<!-- 
💡 解説：
- 画像を1枚だけ使用し、テキストの横に並列配置しています。
- 画像は「比率を変えない（object-fit: cover）」「角を丸めない」を徹底。
- 人の顔が映っていない、空間そのものが伝わるビジュアル素材を選択する想定です。
-->
```

#### C. 数字強調パターン
```markdown
---
<!-- slide: タイトルあり（数字） -->

## 体験者のほぼ全員が「また利用したい」と回答

<div style="text-align: left; margin-top: 40px;">
  <!-- 数字は大きくHelveticaフォント、単位(%)は小さく表現 -->
  <span class="large-number" style="font-size: 5em;">98</span>
  <span style="font-size: 1.8em; font-weight: bold; margin-left: 5px;">%</span>
</div>

### 会員の満足度は驚異的な数値を記録
- 事後アンケートにおいて、従来のサウナで感じていた「不満」が100%解消されたと回答。

<!-- 
💡 解説：
- 数字を単に置くだけでなく、スライド上部にその数字が意味する「解釈（ワンメッセージ）」を明記しています。
- 数字のフォントは「Helvetica」を使い、単位を小さくしています。
-->
```

#### D. プロセス（流れ・ランキング）パターン
```markdown
---
<!-- slide: タイトルあり（プロセス） -->

## 3つのステップをシームレスに繋ぐことで、究極の「整い」へ

<table style="width: 100%; border: none; border-collapse: collapse; text-align: center;">
<tr style="border: none;">
<td style="width: 30%; border: 2px solid #0b2f64; padding: 20px; vertical-align: top;">

### STEP 1
**サウナ室**
最高峰の熱気で身体の芯から温まる
</td>
<!-- 矢印の代わりに「三角形」を使用する -->
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

<!-- 
💡 解説：
- 「普通の矢印」は目立ちすぎてダサくなるため、動画のアドバイス通り「三角形（▲）」を横向き等にして矢印代わりに使っています（ここでは文字としてレイアウト）。
- 枠線は角丸にせず、塗りつぶしもありません。
-->
```

---

### パターン 4：タイトルなし (No Title)
> **動画の指摘：**
> ハンバーガーのピクルスのように、要所で挟んで資料全体に心地よいリズムを作る。
> 白黒透過、半分画像、余白などのパターンがあり、文字数は最小限にする。

#### A. 文字だけパターン（ワンメッセージ強調）
```markdown
---
<!-- slide: タイトルなし（文字だけ） -->

<div align="center" style="margin-top: 150px;">

# **「あなたの整うは、本当に100点ですか？」**

</div>

<!-- 
💡 解説：
- 逆説や、ここぞという話の転換点で聞き手の興味を引くために、文字数を極限まで削って中央に大きく配置します。
- 使いすぎるとくどくなるため、スライド全体のなかで最小限に留めます。
-->
```

#### B. 画像と文字（白黒透過重ね）パターン
```markdown
---
<!-- slide: タイトルなし（画像背景＋透過文字） -->

<!-- 
CSS等で背景画像を指定する、あるいは以下のように画像を背面に敷いて、
その上に半透明の白または黒のレイアウトを重ねる。
-->

<div style="
  background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('images/sauna-bg.jpg');
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100%;
  padding: 100px 50px;
  box-sizing: border-box;
  color: #ffffff; /* このパターンのみ、暗い背景に白文字を許可 */
  text-align: center;
">

# 原点にしてパーフェクトなサウナ体験

### **「バーサウナ」**

</div>

<!-- 
💡 解説：
- 画像の上に直接文字を乗せると読めなくなるため、黒い図形を透過させて重ね（rgba(0,0,0,0.6)）、その上に白文字を乗せて可読性を確保しています。
-->
```

#### C. 画像と文字（余白パターン・最高峰）
```markdown
---
<!-- slide: タイトルなし（余白パターン） -->

<table style="width: 100%; height: 100%; border: none; border-collapse: collapse;">
<tr style="border: none;">
<td style="width: 50%; border: none; padding: 40px; vertical-align: middle;">

# 整う、語らう。
# プライベートサウナ。

</td>
<td style="width: 50%; border: none; text-align: right; vertical-align: middle; padding: 0;">

<!-- 右側に余白（フォーカス）が綺麗に寄っている画像を配置する -->
<img src="images/sauna-chill.jpg" alt="チルスペースのイメージ" style="width: 100%; height: auto; border-radius: 0;">

</td>
</tr>
</table>

<!-- 
💡 解説：
- 動画で「最高峰」と称される、美しい余白のある画像を半分に配置し、もう半分の余白（スペース）に極めて短いメッセージを添える構成です。
-->
```

---

## 🚫 ダサくならないための「絶対禁忌」チェックリスト

マークダウンでスライド構成案を編集・作成する際、以下の「やってはいけないこと（NG）」に触れていないか、常に確認してください。

*   [ ] **民朝体（Mincho）を使っていないか？** $\rightarrow$ 一生使わない。ゴシック体一択（游ゴシック、ヒラギノ角ゴ）。
*   [ ] **ドロップシャドウ（影）を使っていないか？** $\rightarrow$ チープになるので文字や図形にシャドウは絶対に入れない。
*   [ ] **デフォルトの「下線」を使っていないか？** $\rightarrow$ リンクと誤認される。強調は「太字」か「文字サイズ変更」にする。
*   [ ] **2行以上の長文が中央揃えになっていないか？** $\rightarrow$ 人間の視線移動（Zの法則）に合わせて左揃えにする。
*   [ ] **行間がキツキツになっていないか？** $\rightarrow$ 行間は必ず少し空ける（CSSで `line-height: 1.6` 程度に設定）。
*   [ ] **原色（真っ赤・真っ青など）を使っていないか？** $\rightarrow$ チープでおもちゃのようになるため、暗めの色（紺色など）にする。
*   [ ] **複数の色（3色以上）を乱用していないか？** $\rightarrow$ 文字の黒（#333333）以外に使えるのは「メインカラー1色」のみ。アクセントの赤は基本封印する。
*   [ ] **背景を真っ黒にしていないか？** $\rightarrow$ 難易度が爆上がりして見づらくなるため、背景は基本「白」にする。
*   [ ] **四角形の角を丸めていないか？** $\rightarrow$ 丸みは悪目立ちする。四角形は角を丸めず四角のまま使う。
*   [ ] **普通の矢印（➔）を使っていないか？** $\rightarrow$ 目立ちすぎてダサくなるので、代わりにシンプルな「三角形（▲）」を配置する。
*   [ ] **画像の縦横比を歪めていないか？** $\rightarrow$ 比率は100%維持する。
*   [ ] **スライドの端ギリギリに要素を配置していないか？** $\rightarrow$ 常に四方に適切な「余白」を確保する。
