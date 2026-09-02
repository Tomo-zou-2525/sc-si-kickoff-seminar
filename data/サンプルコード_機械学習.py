"""
機械学習による課題解決の例：クレジットカード承認システム
SC運営×AI実装 キックオフセミナー / 第1章 補足用サンプルコード

このコードは、以下5つのプロセスに沿って書かれている。
1. データ収集：大量のデータを集める
2. 特徴抽出とラベル付け：データから特徴を抽出し、必要に応じてラベルを付ける
3. モデルの訓練：機械学習アルゴリズムを使用してデータから学習し、モデルを作成
4. モデルの評価：モデルの性能を評価し、精度を測定
5. 予測と推論：訓練済みモデルを使用して新しいデータに対する予測を行う

「サンプルコード_従来のプログラミング.py」と同じ変数名
（income / credit_score / existing_debt）を使い、2つを見比べられるようにしている。

必要なライブラリ: scikit-learn, numpy
  pip install scikit-learn numpy

（アルゴリズムに決定木を使っている理由）
このサンプルの正解ラベルは「複数の条件をすべて満たすか」という
if文の組み合わせで作っているため、直線1本では区切れない領域になる。
決定木はif文の積み重ねでデータを分割していく手法なので、
このような「ルールっぽい」データと相性がよく、少ないデータでも高い精度が出る。
"""

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# --- ① データ収集：大量のデータを集める ---
def generate_sample_data(n_samples=500, seed=42):
    """
    本来は「過去の実際の取引データ」を使う。
    このサンプルでは説明のために、過去データをランダムに人工生成する。
    """
    rng = np.random.default_rng(seed)
    income = rng.integers(2_000_000, 10_000_000, n_samples)
    credit_score = rng.integers(400, 850, n_samples)
    existing_debt = rng.integers(0, 3_000_000, n_samples)

    # --- ② 特徴抽出とラベル付け：データから特徴を抽出し、必要に応じてラベルを付ける ---
    # income / credit_score / existing_debt が「特徴（データの着目点）」にあたる。
    # 「過去に承認されたか（1）／却下されたか（0）」が「ラベル（正解）」にあたる。
    # ここでは説明用に、「従来のプログラミング」で使ったのと同じ基準で
    # 過去の承認実績を仮に再現している（実際の現場ではこのラベルは
    # 人間のルールではなく、過去の審査結果そのものになる）
    approved = (
        (income >= 5_000_000)
        & (credit_score >= 650)
        & (existing_debt < income * 0.3)
    ).astype(int)  # 1 = 承認、0 = 却下

    features = np.column_stack([income, credit_score, existing_debt])
    return features, approved


features, labels = generate_sample_data()

# 学習用データと、性能確認用データに分割する
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# --- ③ モデルの訓練：機械学習アルゴリズムを使用してデータから学習し、モデルを作成 ---
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# --- ④ モデルの評価：モデルの性能を評価し、精度を測定 ---
predictions_on_test = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions_on_test)


# --- ⑤ 予測と推論：訓練済みモデルを使用して新しいデータに対する予測を行う ---
def predict_approval(income, credit_score, existing_debt):
    new_data = np.array([[income, credit_score, existing_debt]])
    prediction = model.predict(new_data)[0]
    return "承認" if prediction == 1 else "却下"


if __name__ == "__main__":
    print(f"モデルの精度（評価用データでの正解率）: {accuracy:.1%}")
    print()

    # 「従来のプログラミング」サンプルコードと同じ2件で結果を比較できる
    result1 = predict_approval(income=6_000_000, credit_score=700, existing_debt=1_000_000)
    print(f"申込者A（年収600万円・スコア700・借入100万円） → {result1}")

    result2 = predict_approval(income=3_000_000, credit_score=600, existing_debt=1_000_000)
    print(f"申込者B（年収300万円・スコア600・借入100万円） → {result2}")
