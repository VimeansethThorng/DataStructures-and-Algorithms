# Greedy Algorithm: 貪欲法
# URL: https://www.geeksforgeeks.org/dsa/greedy-algorithms/


# 貪欲法（Greedy Algorithm）は、各ステップで局所的に最適な選択を行い、最終的な最適解を目指すアルゴリズムです。
# 代表的な問題として「コイン問題」や「活動選択問題」などがあります。

# 例1: コイン問題
# 目標金額を最小枚数のコインで支払う
def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        count += num
        amount -= num * coin
    return count

coins = [1, 5, 10, 50, 100, 500]
amount = 620
print(f"最小コイン枚数: {min_coins(coins, amount)}")

# 例2: 活動選択問題
# 最大数の互いに重ならない活動を選ぶ
def activity_selection(activities):
    # activities: [(開始時刻, 終了時刻), ...]
    activities.sort(key=lambda x: x[1])
    selected = []
    last_end = 0
    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
result = activity_selection(activities)
print(f"選択された活動: {result}")