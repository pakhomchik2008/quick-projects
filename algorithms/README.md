# Algorithms

Implementations of classic computer science algorithms, progressing from
brute-force linear approaches to efficient divide-and-conquer strategies.

---

## Contents

| Folder | Algorithms | Key Concept |
|--------|------------|-------------|
| [`searching/`](searching/) | Linear search, Binary search | Time vs space trade-offs |
| [`sorting/`](sorting/) | Bubble, Insertion, Selection, Merge, Quick | O(n²) vs O(n log n) |
| [`recursion/`](recursion/) | Factorial, Fibonacci, Power, Sum of digits | Base case + recursive case |

---

## Complexity Overview

### Searching

| Algorithm | Time (worst) | Space | Notes |
|-----------|-------------|-------|-------|
| Linear search | O(n) | O(1) | Works on unsorted data |
| Binary search | O(log n) | O(1) | Requires sorted input |

> Binary search on 1,000,000 elements: at most **20 comparisons**.
> Linear search on the same data: up to **1,000,000 comparisons**.

### Sorting

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

---

## How to Run

```bash
python algorithms/searching/searching.py
python algorithms/sorting/sorting.py
python algorithms/recursion/recursion.py
```
