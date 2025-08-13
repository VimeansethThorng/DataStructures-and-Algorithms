# Pythonでのグラフ構造チュートリアル
#
# 1. グラフの表現（隣接リスト）
# 2. 幅優先探索（BFS）
# 3. 深さ優先探索（DFS）

# 1. グラフの表現（隣接リスト）
graph = {
	'A': ['B', 'C'],
	'B': ['A', 'D', 'E'],
	'C': ['A', 'F'],
	'D': ['B'],
	'E': ['B', 'F'],
	'F': ['C', 'E']
}

# 2. 幅優先探索（BFS）
from collections import deque

def bfs(graph, start):
	visited = set()
	queue = deque([start])
	visited.add(start)
	while queue:
		node = queue.popleft()
		print(node)
		for neighbor in graph[node]:
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append(neighbor)

print("BFS traversal:")
bfs(graph, 'A')

# 3. 深さ優先探索（DFS）
def dfs(graph, node, visited=None):
	if visited is None:
		visited = set()
	visited.add(node)
	print(node)
	for neighbor in graph[node]:
		if neighbor not in visited:
			dfs(graph, neighbor, visited)

print("\nDFS traversal:")
dfs(graph, 'A')
