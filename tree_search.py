from collections import deque
import time


# --------------------------------------------------
# Search Tree
# --------------------------------------------------

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}


# --------------------------------------------------
# Breadth First Search (BFS)
# --------------------------------------------------

def bfs(tree, start, goal):
    queue = deque([start])
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for child in tree[node]:
            queue.append(child)

    return nodes_expanded


# --------------------------------------------------
# Depth First Search (DFS)
# --------------------------------------------------

def dfs(tree, start, goal):
    stack = [start]
    nodes_expanded = 0

    while stack:
        node = stack.pop()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for child in reversed(tree[node]):
            stack.append(child)

    return nodes_expanded


# --------------------------------------------------
# Main Program
# --------------------------------------------------

start_node = 'A'
goal_node = 'M'

runs = 5


# BFS timing
bfs_times = []

for i in range(runs):
    start_time = time.perf_counter()

    bfs_nodes = bfs(tree, start
