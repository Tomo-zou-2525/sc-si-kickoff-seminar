<!--
Slidevスライド1枚分のMarkdown断片。
第3章「生成AIとは何か」/ 3-2. なぜ「次の単語」を予測できるのか、に対応。
「同じ次単語予測というタスクを、文脈をどこまで見て解くか」の進化を3段で比較する図。
-->

---
layout: default
---

# なぜ「次の単語」を予測できるのか

<svg width="100%" viewBox="0 0 680 500" xmlns="http://www.w3.org/2000/svg" role="img">
<title>n-gram・RNN/LSTM・Transformerが次の単語を予測する際に、どこまで文脈を見ているかを比較する図</title>
<desc>同じ文「先月の来館者数は大きく＿＿」を例に、n-gramは直前の数語だけ、RNN/LSTMは全体を見るが古い情報ほど薄れる、Transformerは全単語を均等に直接参照することを示す3段の比較図</desc>

<defs>
<marker id="a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="#5F5E5A"/>
</marker>
</defs>

<text x="40" y="30" font-size="14" font-weight="500" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">① n-gram（統計的手法）：直前の数語しか見ていない</text>

<rect x="40" y="45" width="80" height="40" rx="6" fill="#F1EFE8" stroke="#D3D1C7" stroke-width="1.5"/>
<text x="80" y="70" text-anchor="middle" font-size="12" fill="#888780" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">先月</text>
<rect x="130" y="45" width="80" height="40" rx="6" fill="#F1EFE8" stroke="#D3D1C7" stroke-width="1.5"/>
<text x="170" y="70" text-anchor="middle" font-size="12" fill="#888780" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">の</text>
<rect x="220" y="45" width="80" height="40" rx="6" fill="#F1EFE8" stroke="#D3D1C7" stroke-width="1.5"/>
<text x="260" y="70" text-anchor="middle" font-size="12" fill="#888780" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">来館者数</text>
<rect x="310" y="45" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="350" y="70" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">は</text>
<rect x="400" y="45" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="440" y="70" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">大きく</text>
<rect x="490" y="45" width="70" height="40" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="525" y="70" text-anchor="middle" font-size="14" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">？</text>

<path d="M390,65 L488,65" fill="none" stroke="#185FA5" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M300,65 L308,65" fill="none" stroke="#D3D1C7" stroke-width="1.5" stroke-dasharray="3,3"/>
<text x="170" y="105" text-anchor="middle" font-size="11" fill="#888780" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">この範囲は見ていない</text>

<line x1="40" y1="130" x2="640" y2="130" stroke="#D3D1C7" stroke-width="1"/>

<text x="40" y="160" font-size="14" font-weight="500" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">② RNN・LSTM：全体を見るが、古い情報ほど記憶が薄れる</text>

<rect x="40" y="210" width="80" height="40" rx="6" fill="#E6F1FB" fill-opacity="0.25" stroke="#185FA5" stroke-opacity="0.4" stroke-width="1.5"/>
<text x="80" y="235" text-anchor="middle" font-size="12" fill="#185FA5" fill-opacity="0.6" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">先月</text>
<rect x="130" y="210" width="80" height="40" rx="6" fill="#E6F1FB" fill-opacity="0.4" stroke="#185FA5" stroke-opacity="0.55" stroke-width="1.5"/>
<text x="170" y="235" text-anchor="middle" font-size="12" fill="#185FA5" fill-opacity="0.75" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">の</text>
<rect x="220" y="210" width="80" height="40" rx="6" fill="#E6F1FB" fill-opacity="0.6" stroke="#185FA5" stroke-opacity="0.7" stroke-width="1.5"/>
<text x="260" y="235" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">来館者数</text>
<rect x="310" y="210" width="80" height="40" rx="6" fill="#E6F1FB" fill-opacity="0.8" stroke="#185FA5" stroke-width="1.5"/>
<text x="350" y="235" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">は</text>
<rect x="400" y="210" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="440" y="235" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">大きく</text>
<rect x="490" y="210" width="70" height="40" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="525" y="235" text-anchor="middle" font-size="14" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">？</text>

<path d="M120,230 L128,230" fill="none" stroke="#185FA5" stroke-opacity="0.3" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M210,230 L218,230" fill="none" stroke="#185FA5" stroke-opacity="0.45" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M300,230 L308,230" fill="none" stroke="#185FA5" stroke-opacity="0.6" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M390,230 L398,230" fill="none" stroke="#185FA5" stroke-opacity="0.8" stroke-width="1.5" marker-end="url(#a1)"/>
<path d="M480,230 L488,230" fill="none" stroke="#185FA5" stroke-width="1.5" marker-end="url(#a1)"/>
<text x="170" y="270" text-anchor="middle" font-size="11" fill="#888780" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">1語ずつ順番に読み、古い記憶ほど薄くなる</text>

<line x1="40" y1="295" x2="640" y2="295" stroke="#D3D1C7" stroke-width="1"/>

<text x="40" y="325" font-size="14" font-weight="500" fill="#2C2C2A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">③ Transformer（Attention）：全単語を均等に、直接見る</text>

<rect x="40" y="375" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="80" y="400" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">先月</text>
<rect x="130" y="375" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="170" y="400" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">の</text>
<rect x="220" y="375" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="260" y="400" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">来館者数</text>
<rect x="310" y="375" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="350" y="400" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">は</text>
<rect x="400" y="375" width="80" height="40" rx="6" fill="#E6F1FB" stroke="#185FA5" stroke-width="1.5"/>
<text x="440" y="400" text-anchor="middle" font-size="12" fill="#0C447C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">大きく</text>
<rect x="490" y="375" width="70" height="40" rx="6" fill="#F0997B" stroke="#993C1D" stroke-width="1.5"/>
<text x="525" y="400" text-anchor="middle" font-size="14" fill="#4A1B0C" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">？</text>

<path d="M80,415 C80,450 500,460 515,417" fill="none" stroke="#185FA5" stroke-width="1.3" stroke-opacity="0.75" marker-end="url(#a1)"/>
<path d="M170,415 C170,445 500,455 518,417" fill="none" stroke="#185FA5" stroke-width="1.3" stroke-opacity="0.75" marker-end="url(#a1)"/>
<path d="M260,415 C260,435 490,445 522,417" fill="none" stroke="#185FA5" stroke-width="1.3" stroke-opacity="0.75" marker-end="url(#a1)"/>
<path d="M350,415 L470,417" fill="none" stroke="#185FA5" stroke-width="1.3" stroke-opacity="0.75" marker-end="url(#a1)"/>
<path d="M440,415 L488,416" fill="none" stroke="#185FA5" stroke-width="1.3" stroke-opacity="0.75" marker-end="url(#a1)"/>

<text x="340" y="480" text-anchor="middle" font-size="12" fill="#5F5E5A" font-family="'Hiragino Kaku Gothic ProN','Yu Gothic','Noto Sans JP',sans-serif">「先月」も「大きく」も、距離に関係なく同じ強さで直接つながっている（＝Attention）</text>
</svg>

<!--
補足（発表者ノート案）:
- 「次の単語を当てる」というタスク自体は3つとも共通。変わったのは文脈をどこまで見て解くか
- ①n-gram: 直前の数語のみ（浅い文脈）
- ②RNN/LSTM: 全体を順番に読むが、古い情報ほど薄れる（やや浅い文脈、かつ1語ずつしか処理できず学習が遅い）
- ③Transformer: 全単語を同時に、距離に関係なく直接参照する（深い文脈）。しかも並列処理できるので大規模データで高速学習できる
- 「文脈が読めるようになったから精度が上がった」のが正しい因果関係（カンニングペーパー参照）
-->
