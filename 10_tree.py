"""
Pythonでの木構造（Tree Structure）チュートリアル

1. ノード（Node）クラスの定義
2. 木の作成例
3. 深さ優先探索（DFS）
4. 幅優先探索（BFS）
"""

# 1. ノードクラスの定義
class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

	def add_child(self, child_node):
		self.children.append(child_node)

# 2. 木の作成例
root = Node("A")    # value = "A"
child1 = Node("B")
child2 = Node("C")
child3 = Node("D")

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)

# 3. 深さ優先探索（DFS）
def dfs(node):
	# ノードの値を表示
	print(node.value)
	for child in node.children:
    		dfs(child)

print("DFS traversal:")
dfs(root)

# 4. 幅優先探索（BFS）
from collections import deque

def bfs(node):
	queue = deque([node])   # キューを初期化し、最初のノードを追加
	while queue:
		current = queue.popleft()
		print(current.value)
		for child in current.children:
			queue.append(child)

print("\nBFS traversal:")
bfs(root)
