"""
Divide and Conquer: 分割統治法
URL: https://www.geeksforgeeks.org/dsa/divide-and-conquer/

---

分割統治法（Divide and Conquer）は、問題をより小さな部分問題に分割し、それぞれを再帰的に解決し、最後にそれらの解を統合して元の問題の解とするアルゴリズム手法です。

【基本ステップ】
1. Divide（分割）: 問題を複数の部分問題に分割する
2. Conquer（統治）: 各部分問題を再帰的に解く
3. Combine（統合）: 部分問題の解を統合して全体の解とする

【代表例】
- マージソート（Merge Sort）
- クイックソート（Quick Sort）
- 二分探索（Binary Search）

---
"""

# Pythonでの二分探索（Binary Search）例
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 見つかった場合はインデックスを返す
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 見つからなかった場合

# 使用例
if __name__ == "__main__":
    arr = [3, 9, 10, 27, 38, 43, 82]
    print("Array:", arr)
    target = 27
    result = binary_search(arr, target)
    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found in array")
