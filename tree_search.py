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


# --------------------------------------------------
# BFS Profiling
# --------------------------------------------------

bfs_times = []

for i in range(runs):

    start_time = time.perf_counter()

    bfs_nodes = bfs(tree, start_node, goal_node)

    end_time = time.perf_counter()

    bfs_times.append(end_time - start_time)


# --------------------------------------------------
# DFS Profiling
# --------------------------------------------------

dfs_times = []

for i in range(runs):

    start_time = time.perf_counter()

    dfs_nodes = dfs(tree, start_node, goal_node)

    end_time = time.perf_counter()

    dfs_times.append(end_time - start_time)


# --------------------------------------------------
# Calculate Average Time
# --------------------------------------------------

bfs_average = sum(bfs_times) / runs
dfs_average = sum(dfs_times) / runs


# --------------------------------------------------
# Display Results
# --------------------------------------------------

print("----------------------------------------")
print("        TREE SEARCH PROFILING")
print("----------------------------------------")

print("\nStart Node :", start_node)
print("Goal Node  :", goal_node)
print("Number of Runs :", runs)

print("\nBFS Results")
print("----------------------------------------")
print("Nodes Expanded :", bfs_nodes)
print("Execution Times:")

for i, t in enumerate(bfs_times, 1):
    print("Run", i, ":", t, "seconds")

print("Average Time :", bfs_average, "seconds")


print("\nDFS Results")
print("----------------------------------------")
print("Nodes Expanded :", dfs_nodes)
print("Execution Times:")

for i, t in enumerate(dfs_times, 1):
    print("Run", i, ":", t, "seconds")

print("Average Time :", dfs_average, "seconds")


print("\n----------------------------------------")
print("        PROFILING COMPLETED")
print("----------------------------------------")
