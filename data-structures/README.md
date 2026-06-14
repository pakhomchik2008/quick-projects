# Data Structures

Implementations of fundamental data structures used throughout computer science.
Each structure is chosen to solve a specific class of problem efficiently.

---

## Contents

| Folder | Structure | Abstraction | Key Operations |
|--------|-----------|-------------|----------------|
| [`stack/`](stack/) | Stack | LIFO | push O(1), pop O(1), peek O(1) |
| [`binary-tree/`](binary-tree/) | Binary Tree / BST | Hierarchical | insert O(log n), search O(log n) |
| [`graph/`](graph/) | Graph (adjacency list) | Network | BFS O(V+E), DFS O(V+E) |

---

## Stack

**Last-In, First-Out (LIFO)** — like a pile of plates.

Real-world uses: undo/redo, browser history, function call stack, bracket matching.

```
push(5)  → [5]
push(3)  → [5, 3]
pop()    → 3  (last in, first out)
peek()   → 5
```

Additional exercises: `move_top`, `reverse_stack`, `is_balanced` (bracket checker).

---

## Binary Tree

A hierarchical structure where each node has at most two children.

```
         4
        / \
       2   7
      / \ / \
     1  3 6  9
```

**Traversal orders:**
- **In-order** (L→Root→R): produces sorted output on a BST
- **Pre-order** (Root→L→R): useful for copying/serialising
- **Post-order** (L→R→Root): useful for deletion (children before parent)

Also includes: tree inversion, sum of left leaves, `BinarySearchTree` class.

---

## Graph (Adjacency List)

A network of nodes connected by edges, with optional weights and direction.

```
Gleb ─(5)─ John
 |           |
(7)         (8)
 |           |
Tiago ─────(9)─ Lamine
```

Algorithms included: **BFS** (shortest path), **DFS** (reachability), `shortest_path`, `mutual_connections`.

---

## How to Run

```bash
python data-structures/stack/stack.py
python data-structures/binary-tree/binary_tree.py
python data-structures/graph/graph.py
```
