<!--
Slidevスライド1枚分のMarkdown断片。
セミナー目次案「第1章 AIとは何か / 1-1. AI・ML・DLという言葉の整理」に対応。
使い方: スライドデッキの.mdファイルに、`---`区切りのスライドとしてこのままコピペしてください。
-->

---
layout: default
---

# そもそもAIとは

<svg width="100%" viewBox="0 0 680 650" xmlns="http://www.w3.org/2000/svg" role="img">
<title>AIと生成AIの関係を示す入れ子図</title>
<desc>AIという大きな概念の中に機械学習があり、その中に深層学習、さらにその中に生成AIが位置づけられることを示す4層の同心円図</desc>

<circle cx="380" cy="320" r="250" fill="#E6F1FB" stroke="#185FA5" stroke-width="2"/>
<circle cx="380" cy="320" r="180" fill="#B5D4F4" stroke="#185FA5" stroke-width="2"/>
<circle cx="380" cy="320" r="110" fill="#85B7EB" stroke="#185FA5" stroke-width="2"/>
<circle cx="380" cy="320" r="50" fill="#D85A30" stroke="#993C1D" stroke-width="2"/>

<text x="380" y="105" text-anchor="middle" font-size="17" font-weight="500" fill="#042C53" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">AI（人工知能）</text>
<text x="380" y="126" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">知的な振る舞いを模倣する技術全般</text>

<text x="380" y="170" text-anchor="middle" font-size="16" font-weight="500" fill="#042C53" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">機械学習</text>
<text x="380" y="190" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">データから規則性を学習する</text>

<text x="380" y="238" text-anchor="middle" font-size="15" font-weight="500" fill="#042C53" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">深層学習</text>
<text x="380" y="256" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">多層ニューラルネットワークを使う</text>

<text x="380" y="316" text-anchor="middle" font-size="16" font-weight="500" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">生成AI</text>
<text x="380" y="335" text-anchor="middle" font-size="12" fill="#712B13" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">文章・画像などを新たに生成する</text>

<text x="380" y="615" text-anchor="middle" font-size="12" fill="#5F5E5A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">※生成AIの調整（RLHF）には強化学習の技術も一部使われますが、土台は深層学習です</text>
</svg>

<!--
補足（発表者ノート案）:
- 生成AIはAIという大きな概念の中の、深層学習を土台にした一部分であることを伝える
- 「深層強化学習」という言葉は生成AIの主要な分類ではない点に注意（RLHFという調整技術の一部で強化学習の考え方を使っているだけ）
-->
