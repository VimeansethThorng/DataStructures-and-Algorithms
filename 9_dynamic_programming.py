# Dynamic Programming: 動的計画法
# URL: https://www.geeksforgeeks.org/competitive-programming/dynamic-programming/

# 動的計画法（Dynamic Programming, DP）は、複雑な問題をより小さな部分問題に分割し、それらを解いていくことで全体の問題を効率的に解決する手法です。
# 部分問題の解を再利用することで、計算量を大幅に削減できます。

# 例題: フィボナッチ数列
# フィボナッチ数列は、次のように定義されます:
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) (n >= 2)
# 例: n = 10 のときのフィボナッチ数列
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# 1. 再帰（メモ化なし）: 非効率
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 2. メモ化再帰（トップダウンDP）
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# ⭐️⭐️⭐️　3. 配列を使ったボトムアップDP
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 4. 定数メモリでのDP
def fib_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# 実行例
if __name__ == "__main__":
    n = 10
    print("fib_recursive:", fib_recursive(n))
    print("fib_memo:", fib_memo(n))
    print("fib_dp:", fib_dp(n))
    print("fib_optimized:", fib_optimized(n))

# 他のDP問題例:
# ・ナップサック問題
# ・最長増加部分列（LIS）
# ・コイン問題
# これらも部分問題の解を再利用することで効率的に解けます。