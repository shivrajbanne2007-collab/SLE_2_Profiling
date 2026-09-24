
---

# `Contribution_Log.md`

```markdown
# Contribution Log

## SLE-2: BFS vs DFS Tree Search Profiling

### Student
**Name:** Shivraj Pravin Banne

### Experiment
**SLE-2 – BFS vs DFS Tree Search Profiling**

### Project Topic
**Performance Comparison of Breadth-First Search (BFS) and Depth-First Search (DFS)**

---

# 1. Contribution Overview

This project implements Breadth-First Search (BFS) and Depth-First Search (DFS) on a 15-node binary tree and compares their search performance.

The work includes:

- Designing the search tree.
- Implementing BFS.
- Implementing DFS.
- Counting nodes expanded.
- Implementing execution-time measurement.
- Designing best-case, average-case, and worst-case experiments.
- Running repeated timing experiments.
- Generating a final comparison table.
- Analysing the obtained results.
- Preparing project documentation.

---

# 2. Initial Problem Understanding

The first step was to understand the requirement of comparing two uninformed search algorithms:

1. Breadth-First Search
2. Depth-First Search

The experiment required more than simply implementing the algorithms.

The implementation also needed to measure:

- Search effort
- Number of nodes expanded
- Execution time
- Performance under different goal positions

The problem was therefore divided into separate components:

```text
Tree Creation
      ↓
BFS Implementation
      ↓
DFS Implementation
      ↓
Node Expansion Counting
      ↓
Timing Function
      ↓
Best/Average/Worst Cases
      ↓
Result Collection
      ↓
Final Comparison
      ↓
Documentation
