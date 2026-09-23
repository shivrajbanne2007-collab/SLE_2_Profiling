from collections import deque
import time
import sys


# ============================================================
# CREATE A BINARY SEARCH TREE
# ============================================================

def create_tree(depth):
    tree = {}

    total_nodes = (2 ** (depth + 1)) - 1

    for i in range(1, total_nodes + 1):
        children = []

        left = 2 * i
        right = 2 * i + 1

        if left <= total_nodes:
            children.append(left)

        if right <= total_nodes:
            children.append(right)

        tree[i] = children

    return tree


# ============================================================
# BREADTH-FIRST SEARCH
# ============================================================

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


# ============================================================
# DEPTH-FIRST SEARCH
# ============================================================

def dfs(tree, start, goal):
    stack = [start]
    nodes_expanded = 0

    while stack:
        node = stack.pop()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        # Add right child first so left child is explored first
        for child in reversed(tree[node]):
            stack.append(child)

    return nodes_expanded


# ============================================================
# RUN ONE SEARCH MULTIPLE TIMES
# Used only to give py-spy enough execution time
# ============================================================

def profiling_workload(tree, algorithm, start, goal, repetitions):

    for _ in range(repetitions):

        if algorithm == "bfs":
            bfs(tree, start, goal)

        elif algorithm == "dfs":
            dfs(tree, start, goal)


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # Tree depth
    DEPTH = 13

    # Create tree
    tree = create_tree(DEPTH)

    start_node = 1

    # Left-most deepest node
    goal_node = 2 ** DEPTH

    print("==============================================")
    print("       BFS vs DFS TREE SEARCH")
    print("==============================================")

    print("Tree Depth:", DEPTH)
    print("Total Nodes:", len(tree))
    print("Start Node:", start_node)
    print("Goal Node:", goal_node)

    # --------------------------------------------------------
    # BFS measurement
    # --------------------------------------------------------

    bfs_times = []

    for _ in range(5):

        start_time = time.perf_counter()

        bfs_nodes = bfs(tree, start_node, goal_node)

        end_time = time.perf_counter()

        elapsed = (end_time - start_time) * 1000
        bfs_times.append(elapsed)

    bfs_average = sum(bfs_times) / len(bfs_times)

    # --------------------------------------------------------
    # DFS measurement
    # --------------------------------------------------------

    dfs_times = []

    for _ in range(5):

        start_time = time.perf_counter()

        dfs_nodes = dfs(tree, start_node, goal_node)

        end_time = time.perf_counter()

        elapsed = (end_time - start_time) * 1000
        dfs_times.append(elapsed)

    dfs_average = sum(dfs_times) / len(dfs_times)

    # --------------------------------------------------------
    # Display experimental results
    # --------------------------------------------------------

    print("\n--------------- BFS RESULTS ----------------")

    print("Nodes Expanded:", bfs_nodes)

    print(
        "Run Times (ms):",
        [round(t, 6) for t in bfs_times]
    )

    print(
        "Average Time (ms):",
        round(bfs_average, 6)
    )

    print("\n--------------- DFS RESULTS ----------------")

    print("Nodes Expanded:", dfs_nodes)

    print(
        "Run Times (ms):",
        [round(t, 6) for t in dfs_times]
    )

    print(
        "Average Time (ms):",
        round(dfs_average, 6)
    )

    # --------------------------------------------------------
    # Final comparison
    # --------------------------------------------------------

    print("\n--------------- COMPARISON -----------------")

    print(
        "BFS Average Time:",
        round(bfs_average, 6),
        "ms"
    )

    print(
        "DFS Average Time:",
        round(dfs_average, 6),
        "ms"
    )

    print("BFS Nodes Expanded:", bfs_nodes)
    print("DFS Nodes Expanded:", dfs_nodes)

    # --------------------------------------------------------
    # Py-spy mode
    # --------------------------------------------------------

    if len(sys.argv) == 3:

        algorithm = sys.argv[1].lower()
        repetitions = int(sys.argv[2])

        print("\n==============================================")
        print("             PY-SPY PROFILING MODE")
        print("==============================================")

        print("Algorithm:", algorithm.upper())
        print("Repetitions:", repetitions)

        print("\nRunning workload...")

        profiling_workload(
            tree,
            algorithm,
            start_node,
            goal_node,
            repetitions
        )

        print("Profiling workload completed.")
