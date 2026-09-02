"""
従来のプログラミングによる課題解決の例：クレジットカード承認システム
SC運営×AI実装 キックオフセミナー / 第1章 補足用サンプルコード

このコードは、以下4つのプロセスに沿って書かれている。
1. ルールの定義：開発者が明確なルールを定義
2. 入力の受け取り：プログラムがユーザーからの入力を受け取る
3. 処理の実行：定義されたルールに基づいて入力を処理
4. 出力の生成：処理結果を出力
"""


# --- ① ルールの定義：開発者が明確なルールを定義 ---
def approve_credit_card(income, credit_score, existing_debt):
    """
    与信ルール（人間があらかじめ決めた条件）
      ・年収が500万円以上
      ・信用スコアが650以上
      ・既存の借入が年収の30%未満
    上記をすべて満たせば「承認」、1つでも満たさなければ「却下」とする。
    """

    # --- ② 入力の受け取り ---
    # このサンプルでは、関数の引数 income / credit_score / existing_debt が
    # 「プログラムが受け取る入力」にあたる

    # --- ③ 処理の実行：定義されたルールに基づいて入力を処理 ---
    rule_income = income >= 5_000_000
    rule_credit_score = credit_score >= 650
    rule_debt = existing_debt < income * 0.3

    # --- ④ 出力の生成：処理結果を出力 ---
    if rule_income and rule_credit_score and rule_debt:
        return "承認"
    else:
        return "却下"


if __name__ == "__main__":
    # 実行例1：条件をすべて満たすケース
    result1 = approve_credit_card(income=6_000_000, credit_score=700, existing_debt=1_000_000)
    print(f"申込者A（年収600万円・スコア700・借入100万円） → {result1}")

    # 実行例2：条件を満たさないケース
    result2 = approve_credit_card(income=3_000_000, credit_score=600, existing_debt=1_000_000)
    print(f"申込者B（年収300万円・スコア600・借入100万円） → {result2}")
