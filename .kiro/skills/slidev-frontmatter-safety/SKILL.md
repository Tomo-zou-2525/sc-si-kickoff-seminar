---
name: slidev-frontmatter-safety
description: Slidev（.md スライド）で style フロントマターや HTML ブロックを書くときの落とし穴を回避する。ビルドが "Attribute name cannot start with '=='" や "Element is missing end tag" で失敗する、CSS を効かせたい、Marp から Slidev へ移行する、といった場面で使う。
metadata:
  author: tom
  version: 1.0.0
---

# Slidev フロントマター & HTML の安全ルール

Slidev（`mdc: true`）でスライドを書くとき、フロントマターの `style:` ブロックや本文中の HTML はそのまま Vue SFC としてコンパイルされる。Markdown として無害に見える記述がビルド時にパースエラーになることがある。以下を守ればほぼ回避できる。

開発サーバ（`npm run dev`）では通っても、静的ビルド（`slidev build`）で初めて落ちるケースがあるため、**変更後は必ずビルドで検証する**こと。

## 必ず守るルール

1. **`style:` ブロック内で CSS コメント `/* ... */` を使わない**
   - `mdc` のパースが崩れ、`Attribute name cannot start with '='` で落ちる。
   - 説明を残したいときは、フロントマターの外（`style:` の手前の YAML コメント行 `#`）に書く。

2. **YAML コメント（`#` 行）に `---` を含めない**
   - 例: `# --- デザインシステム ---` は NG。`---` がフロントマター区切りと誤検出され、以降が本文扱いになって崩れる。
   - `# デザインシステム` のようにハイフン区切りを使わない。

3. **HTML タグの中で Markdown 記法（`**太字**` など）を使わない**
   - 例: `<h3>**タイトル**</h3>` は NG。HTML ブロック内では Markdown は展開されず、ビルド時パーサも崩れる。
   - 強調が必要なら CSS 側（`font-weight: bold`）で表現するか、HTML ブロックの外で書く。

4. **HTML 要素の属性を複数行に分けない**
   - 開きタグと属性は 1 行にまとめる。複数行属性はビルド時に崩れやすい。
   - 例（NG）:
     ```html
     <div
       class="..."
       style="...">
     ```
   - 例（OK）: `<div class="..." style="...">`

5. **`<h1>` などの直後に `->` を置かない**
   - 例: `<h1>-> 続き</h1>` は `->` が属性開始と誤認される。全角矢印 `→` を使う。

6. **`<div>` の開閉を必ず揃える**
   - 閉じ忘れ・`</div>` を `<div>` と書き間違えると `Element is missing end tag` で落ちる。
   - グリッドや 2 カラムレイアウトでネストが深くなったら、スライド単位で開閉数を数えて確認する。

## ビルド検証の手順

1. 出力先はプロジェクト内に置く（`/tmp` などプロジェクト外はパス解決で別エラーになる）。
   ```bash
   npx slidev build <file>.md --out ./_out_check
   rm -rf ./_out_check
   ```
2. エラーが出たら、メッセージ末尾の `<file>.md__slidev_N.md:行:桁` を読む。
   - `__slidev_N` は N+1 枚目のスライド（0 始まり）。表紙が `__slidev_1` になることもあるので、切り詰めコピーで二分探索すると確実。
3. `Attribute name cannot start with '='` → 上記ルール 1〜5 のいずれか。
4. `Element is missing end tag` → 上記ルール 6。

## 既知の良い形（コピー用）

CSS コメントも `---` も含まない、安全なデザインシステム用フロントマター:

```yaml
---
theme: default
mdc: true
# デザインシステム（明朝体を使わない/背景は白/文字は #333333/メインカラー1色）
# 注意: style ブロック内では CSS コメント（/* */）を使わない
style: |
  .slidev-layout {
    font-family: "Yu Gothic", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    background-color: #ffffff;
    color: #333333;
    line-height: 1.6;
  }
  .slidev-layout strong { color: #0b2f64; font-weight: bold; }
  .slidev-layout h1, .slidev-layout h2, .slidev-layout h3 { color: #0b2f64; }
  .slidev-layout a { text-decoration: none; }
---
```
