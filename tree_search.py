from collections import deque
import time


# ============================================================
# 15-NODE SEARCH TREE
# ============================================================

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

        # Reverse order so the left child is explored first
        for child in reversed(tree[node]):
            stack.append(child)

    return nodes_expanded


# ============================================================
# TIMING FUNCTION
# ============================================================

def measure_time(search_function, start, goal,
                 repetitions=5000, runs=5):

    times = []
    nodes = 0

    for _ in range(runs):

        start_time = time.perf_counter()

        for _ in range(repetitions):
            nodes = search_function(tree, start, goal)

        end_time = time.perf_counter()

        elapsed_ms = (end_time - start_time) * 1000
        times.append(elapsed_ms)

    average_time = sum(times) / len(times)

    return average_time, times, nodes


# ============================================================
# MAIN EXPERIMENT
# ============================================================

if __name__ == "__main__":

    start_node = 'A'

    # Three experimental cases
    goals = {
        "Best Case": 'B',
        "Average Case": 'M',
        "Worst Case": 'O'
    }

    repetitions = 5000
    runs = 5

    print("=" * 60)
    print("       BFS vs DFS - TREE SEARCH PROFILING")
    print("=" * 60)

    print("\nTree Nodes:", len(tree))
    print("Start Node:", start_node)
    print("Repetitions per timing run:", repetitions)
    print("Timing runs per case:", runs)

    print("\nTree:")
    print("                    A")
    print("                 /     \\")
    print("                B       C")
    print("              /  \\     /  \\")
    print("             D    E   F    G")
    print("            / \\  / \\ / \\  / \\")
    print("           H  I J  K L  M N  O")

    results = []

    # --------------------------------------------------------
    # Run all three cases
    # --------------------------------------------------------

    for case_name, goal_node in goals.items():

        print("\n" + "-" * 60)
        print(case_name)
        print("Goal Node:", goal_node)
        print("-" * 60)

        # BFS
        bfs_average, bfs_times, bfs_nodes = measure_time(
            bfs,
            start_node,
            goal_node,
            repetitions,
            runs
        )

        # DFS
        dfs_average, dfs_times, dfs_nodes = measure_time(
            dfs,
            start_node,
            goal_node,
            repetitions,
            runs
        )

        # Store results
        results.append(
            (
                case_name,
                goal_node,
                bfs_average,
                dfs_average,
                bfs_nodes,
                dfs_nodes
            )
        )

        # Display BFS
        print("\nBFS")
        print("Nodes Expanded:", bfs_nodes)
        print(
            "Run Times (ms):",
            [round(t, 4) for t in bfs_times]
        )
        print(
            "Average Time (ms):",
            round(bfs_average, 4)
        )

        # Display DFS
        print("\nDFS")
        print("Nodes Expanded:", dfs_nodes)
        print(
            "Run Times (ms):",
            [round(t, 4) for t in dfs_times]
        )
        print(
            "Average Time (ms):",
            round(dfs_average, 4)
        )

    # ========================================================
    # FINAL SUMMARY TABLE
    # ========================================================

    print("\n\n")
    print("=" * 75)
    print("                     FINAL RESULTS")
    print("=" * 75)

    print(
        f"{'Case':<15}"
        f"{'Goal':<8}"
        f"{'BFS Time':<15}"
        f"{'DFS Time':<15}"
        f"{'BFS Nodes':<12}"
        f"{'DFS Nodes':<12}"
    )

    print("-" * 75)

    for result in results:

        case_name, goal, bfs_time, dfs_time, bfs_nodes, dfs_nodes = result

        print(
            f"{case_name:<15}"
            f"{goal:<8}"
            f"{bfs_time:<15.4f}"
            f"{dfs_time:<15.4f}"
            f"{bfs_nodes:<12}"
            f"{dfs_nodes:<12}"
        )

    print("=" * 75)

    print("\nProfiling experiment completed successfully.")
