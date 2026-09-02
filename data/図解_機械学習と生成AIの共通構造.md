<!--
Slidevスライド1枚分のMarkdown断片。
第3章「生成AIとは何か」の導入に対応。
第1章で使った「従来のプログラミングと機械学習の違い」の図と同じビジュアル言語（箱＋矢印）を踏襲し、
「学習フェーズ／推論フェーズ」という骨格が機械学習と生成AIで共通であることを示す。
-->

---
layout: default
---

# 生成AIも実は同じ仕組み

<svg width="100%" viewBox="0 0 680 500" xmlns="http://www.w3.org/2000/svg" role="img">
<title>機械学習と生成AIが同じ学習・推論構造を持つことを示す図</title>
<desc>機械学習の一般化した構造(訓練データ・アルゴリズム・モデルによる学習フェーズと、新しい入力・モデル・出力による推論フェーズ)と、生成AIが同じ構造(テキストデータ・Transformer・LLMによる学習フェーズと、プロンプト・LLM・出力テキストによる推論フェーズ、オプションでベクターストアを介したRAG)を持つことを示す比較図</desc>

<defs>
<marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="#5F5E5A"/>
</marker>
<marker id="arrowDash" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="#888780"/>
</marker>
</defs>

<text x="40" y="35" font-size="14" font-weight="500" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">機械学習（一般化した構造）</text>

<rect x="40" y="55" width="130" height="44" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="105" y="82" text-anchor="middle" font-size="13" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">訓練データ</text>

<rect x="210" y="55" width="130" height="44" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="275" y="82" text-anchor="middle" font-size="13" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">アルゴリズム</text>

<rect x="380" y="55" width="150" height="44" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="455" y="82" text-anchor="middle" font-size="13" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">モデル（学習済み）</text>

<path d="M170,77 L210,77" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>
<path d="M340,77 L380,77" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>

<rect x="40" y="125" width="130" height="44" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="105" y="152" text-anchor="middle" font-size="13" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">新しい入力</text>

<rect x="210" y="125" width="130" height="44" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="275" y="152" text-anchor="middle" font-size="13" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">モデル</text>

<rect x="380" y="125" width="150" height="44" rx="6" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="1.5"/>
<text x="455" y="152" text-anchor="middle" font-size="13" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">出力</text>

<path d="M170,147 L210,147" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>
<path d="M340,147 L380,147" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>

<line x1="40" y1="195" x2="640" y2="195" stroke="#D3D1C7" stroke-width="1"/>

<text x="40" y="225" font-size="14" font-weight="500" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">生成AI（同じ構造に当てはめると）</text>

<rect x="40" y="245" width="130" height="44" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="105" y="268" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">大量の</text>
<text x="105" y="283" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">テキストデータ</text>

<rect x="210" y="245" width="130" height="44" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="275" y="272" text-anchor="middle" font-size="13" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">Transformer</text>

<rect x="380" y="245" width="150" height="44" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="455" y="268" text-anchor="middle" font-size="13" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">LLM</text>
<text x="455" y="283" text-anchor="middle" font-size="11" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">（事前学習済み）</text>

<path d="M170,267 L210,267" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>
<path d="M340,267 L380,267" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>

<rect x="40" y="315" width="130" height="44" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="105" y="342" text-anchor="middle" font-size="13" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">プロンプト</text>

<rect x="210" y="315" width="130" height="44" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="275" y="342" text-anchor="middle" font-size="13" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">LLM</text>

<rect x="380" y="315" width="150" height="44" rx="6" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="1.5"/>
<text x="455" y="342" text-anchor="middle" font-size="13" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">出力テキスト</text>

<path d="M170,337 L210,337" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>
<path d="M340,337 L380,337" fill="none" stroke="#5F5E5A" stroke-width="1.5" marker-end="url(#arrow2)"/>

<rect x="185" y="400" width="180" height="40" rx="6" fill="none" stroke="#888780" stroke-width="1.5" stroke-dasharray="4,3"/>
<text x="275" y="424" text-anchor="middle" font-size="12" fill="#5F5E5A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">検索・ベクターストア</text>

<path d="M255,359 L255,400" fill="none" stroke="#888780" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrowDash)"/>
<path d="M295,400 L295,359" fill="none" stroke="#888780" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrowDash)"/>

<text x="275" y="463" text-anchor="middle" font-size="11" fill="#5F5E5A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">※オプション：RAGなど、外部の最新情報が必要な場合のみ経由する（LLM本体の必須機能ではない）</text>

<text x="340" y="490" text-anchor="middle" font-size="12" fill="#5F5E5A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">学習フェーズ・推論フェーズという骨格は共通。生成AIは「言葉」を大量に学習した機械学習モデルの一種</text>
</svg>

<!--
補足（発表者ノート案）:
- 第1章で見せた「従来のプログラミング vs 機械学習」の図と同じ箱・矢印のレイアウトを意図的に踏襲している。
  「前に見た型に、もう1つ当てはまった」という見せ方で理解の負荷を下げる狙い
- ベクターストアは点線・オプション表記。「生成AIは常に検索している」という誤解を避けるための強調
- この後、tiktokenizer→bbycroft.net/llmの順でインタラクティブデモに繋げる想定
-->
