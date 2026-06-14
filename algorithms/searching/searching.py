"""
Searching Algorithms
====================
Implementations of linear search and binary search with full complexity analysis.

Key insight: binary search is dramatically faster on sorted data.
For 1 million elements, linear search checks up to 1,000,000 items;
binary search checks at most 20.

Complexity summary:
    Algorithm                 | Best   | Average  | Worst    | Space
    --------------------------|--------|----------|----------|----------
    Linear search             | O(1)   | O(n)     | O(n)     | O(1)
    Linear search (ordered)   | O(1)   | O(n)     | O(n)     | O(1)
    Binary search (iterative) | O(1)   | O(log n) | O(log n) | O(1)
    Binary search (recursive) | O(1)   | O(log n) | O(log n) | O(log n)
"""

from typing import Optional


def linear_search(arr: list[int], target: int) -> Optional[int]:
    """
    Search every element of an unordered list until the target is found.

    Time:  O(n) — must check every element in the worst case
    Space: O(1) — no extra memory required

    Args:
        arr:    The list to search (any order).
        target: The value to find.

    Returns:
        Index of the target value, or None if not found.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return None


def linear_search_ordered(arr: list[int], target: int) -> Optional[int]:
    """
    Optimised linear search for a sorted list.
    Stops early when a value greater than the target is encountered,
    since the target cannot appear further along a sorted sequence.

    Time:  O(n) worst case, but exits early in practice
    Space: O(1)

    Args:
        arr:    A sorted (ascending) list.
        target: The value to find.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
        if value > target:
            return None   # Target cannot exist further along the sorted list
    return None


def binary_search(arr: list[int], target: int) -> Optional[int]:
    """
    Divide-and-conquer search on a sorted list.

    At each step, the middle element is compared to the target.
    - If equal, return the index.
    - If target > middle, discard the left half.
    - If target < middle, discard the right half.
    This halves the search space every iteration, giving O(log n) time.

    Requires: arr must be sorted in ascending order.

    Time:  O(log n)
    Space: O(1)

    Args:
        arr:    A sorted list.
        target: The value to find.

    Returns:
        Index of the target, or None if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1      # Target lies in the right half
        else:
            right = mid - 1     # Target lies in the left half

    return None


def binary_search_recursive(
    arr: list[int],
    target: int,
    left: int = 0,
    right: Optional[int] = None,
) -> Optional[int]:
    """
    Recursive binary search — same logic as the iterative version,
    expressed as a recursive divide-and-conquer function.

    The extra stack frames make this O(log n) space instead of O(1).

    Time:  O(log n)
    Space: O(log n) — depth of the recursion call stack
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return None

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    unsorted = [60, 1, 88, 34, 17, 99, 42]
    sorted_list = [1, 2, 4, 5, 6, 7, 8, 9, 11, 23]

    print("=== Linear Search (unordered list) ===")
    print(f"List:   {unsorted}")
    print(f"Search 88  → index {linear_search(unsorted, 88)}")    # 2
    print(f"Search 55  → index {linear_search(unsorted, 55)}")    # None

    print("\n=== Linear Search (sorted list, early exit) ===")
    print(f"List:   {sorted_list}")
    print(f"Search 6   → index {linear_search_ordered(sorted_list, 6)}")     # 4
    print(f"Search 10  → index {linear_search_ordered(sorted_list, 10)}")    # None

    print("\n=== Binary Search (iterative) ===")
    print(f"List:   {sorted_list}")
    print(f"Search 6   → index {binary_search(sorted_list, 6)}")    # 4
    print(f"Search 23  → index {binary_search(sorted_list, 23)}")   # 9
    print(f"Search 3   → index {binary_search(sorted_list, 3)}")    # None

    print("\n=== Binary Search (recursive) ===")
    print(f"Search 11  → index {binary_search_recursive(sorted_list, 11)}")  # 8
    print(f"Search 1   → index {binary_search_recursive(sorted_list, 1)}")   # 0
    print(f"Search 100 → index {binary_search_recursive(sorted_list, 100)}") # None

    print("\n=== Complexity Comparison ===")
    header = f"{'Algorithm':<30} {'Best':>6} {'Average':>10} {'Worst':>10} {'Space':>10}"
    print(header)
    print("-" * len(header))
    rows = [
        ("Linear search",           "O(1)", "O(n)",     "O(n)",     "O(1)"),
        ("Linear search (ordered)", "O(1)", "O(n)",     "O(n)",     "O(1)"),
        ("Binary search (iter.)",   "O(1)", "O(log n)", "O(log n)", "O(1)"),
        ("Binary search (recur.)",  "O(1)", "O(log n)", "O(log n)", "O(log n)"),
    ]
    for name, best, avg, worst, space in rows:
        print(f"{name:<30} {best:>6} {avg:>10} {worst:>10} {space:>10}")
