# SLE-2: BFS vs DFS Tree Search Profiling

## 1. Title

**Performance Comparison of Breadth-First Search (BFS) and Depth-First Search (DFS) Using Tree Search Profiling**

---

## 2. Objective

The objective of this experiment is to implement and compare:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

on a 15-node search tree.

The experiment measures:

1. Number of nodes expanded by BFS and DFS.
2. Execution time of BFS and DFS.
3. Performance for different goal-node positions.
4. Best-case, average-case, and worst-case search behavior.
5. Difference between BFS and DFS in terms of search effort and execution time.

---

## 3. Problem Statement

Implement Breadth-First Search and Depth-First Search for searching a goal node in a tree.

The program should:

- Use a 15-node binary tree.
- Start the search from node `A`.
- Search for different goal nodes.
- Count the number of nodes expanded.
- Measure execution time.
- Perform multiple repetitions to obtain measurable timing values.
- Perform multiple timing runs.
- Compare BFS and DFS results.

The three experimental cases used are:

| Case | Goal Node | Purpose |
|---|---|---|
| Best Case | B | Goal is found very close to the root |
| Average Case | M | Goal is located at an intermediate/deeper position |
| Worst Case | O | Goal is the last node explored by both searches |

---

## 4. Tree Used in the Experiment

The experiment uses the following 15-node binary tree:

```text
                    A
                 /     \
                B       C
              /  \     /  \
             D    E   F    G
            / \  / \ / \  / \
           H  I J  K L  M N  O
