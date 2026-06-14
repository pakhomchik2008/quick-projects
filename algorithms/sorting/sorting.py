"""
Sorting Algorithms
==================
Five classic sorting algorithms progressing from O(n²) naive approaches
to O(n log n) divide-and-conquer strategies.

Complexity summary:
    Algorithm       | Best     | Average  | Worst    | Space  | Stable
    ----------------|----------|----------|----------|--------|-------
    Bubble sort     | O(n)     | O(n²)    | O(n²)    | O(1)   | Yes
    Insertion sort  | O(n)     | O(n²)    | O(n²)    | O(1)   | Yes
    Selection sort  | O(n²)    | O(n²)    | O(n²)    | O(1)   | No
    Merge sort      | O(n log n)| O(n log n)| O(n log n)| O(n) | Yes
    Quick sort      | O(n log n)| O(n log n)| O(n²)  | O(log n)| No

Stable = equal elements keep their original relative order.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Repeatedly swap adjacent elements that are out of order.
    After each full pass the largest unsorted element 'bubbles' to its
    correct position at the end of the unsorted region.

    The early-exit flag makes this O(n) on an already-sorted list.

    Time:  O(n²) average/worst, O(n) best (already sorted)
    Space: O(1) — sorts in place

    Args:
        arr: List of integers to sort (modified in place).

    Returns:
        The sorted list (same object).
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):         # Shrink window each pass
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break                           # Already sorted — exit early
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Build a sorted sub-list one element at a time.
    Each new element is inserted into its correct position within the
    already-sorted prefix by shifting larger elements one step right.

    Excellent for small or nearly-sorted lists.

    Time:  O(n²) average/worst, O(n) best (already sorted)
    Space: O(1) — sorts in place

    Args:
        arr: List of integers to sort (modified in place).

    Returns:
        The sorted list (same object).
    """
    for i in range(1, len(arr)):
        key = arr[i]            # Element to be inserted into the sorted prefix
        j = i - 1
        # Shift elements of the sorted prefix that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key        # Insert key into its correct position
    return arr


def selection_sort(arr: list[int]) -> list[int]:
    """
    Divide the list into a sorted prefix and unsorted suffix.
    On each pass, find the minimum of the unsorted suffix and swap it
    into the last position of the sorted prefix.

    Makes the minimum number of swaps (O(n)), but always O(n²) comparisons.

    Time:  O(n²) always
    Space: O(1) — sorts in place

    Args:
        arr: List of integers to sort (modified in place).

    Returns:
        The sorted list (same object).
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]    # Swap minimum into place
    return arr


def merge_sort(arr: list[int]) -> list[int]:
    """
    Divide-and-conquer sort.
    Recursively splits the list in half until sub-lists have 1 element
    (trivially sorted), then merges pairs of sorted sub-lists back together.

    Time:  O(n log n) always — log n splits, O(n) work per level
    Space: O(n) — merged copies require extra memory

    Args:
        arr: List of integers to sort.

    Returns:
        A new sorted list (does not modify the original).
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    return _merge(left_sorted, right_sorted)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into a single sorted list.

    Uses two pointers that advance through each list, always picking
    the smaller of the two current elements.
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements (at most one list will have leftovers)
    merged += left[i:]
    merged += right[j:]
    return merged


def quick_sort(arr: list[int], first: int = 0, last: int = None) -> list[int]:
    """
    Divide-and-conquer sort using a pivot element.
    Partitions the list so that all elements left of the pivot are smaller
    and all elements right are larger, then recursively sorts each half.

    Performance depends heavily on pivot choice; worst case (sorted input
    with first-element pivot) degrades to O(n²).

    Time:  O(n log n) average, O(n²) worst
    Space: O(log n) — recursion stack

    Args:
        arr:   List of integers to sort (modified in place).
        first: Start index of the region to sort.
        last:  End index (inclusive) of the region to sort.

    Returns:
        The sorted list (same object).
    """
    if last is None:
        last = len(arr) - 1

    if first >= last:
        return arr

    pivot_index = _partition(arr, first, last)
    quick_sort(arr, first, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, last)
    return arr


def _partition(arr: list[int], first: int, last: int) -> int:
    """
    Rearrange elements around a pivot (chosen as arr[first]).
    After partitioning:
      - Elements at indices < pivot_index are <= pivot
      - Elements at indices > pivot_index are >= pivot

    Returns:
        The final index of the pivot element.
    """
    pivot = arr[first]
    left = first + 1
    right = last

    while True:
        while left <= last and arr[left] < pivot:
            left += 1
        while right >= first and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    # Place pivot in its final sorted position
    arr[first], arr[right] = arr[right], arr[first]
    return right


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import copy

    original = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {original}\n")

    print(f"Bubble sort:    {bubble_sort(copy.copy(original))}")
    print(f"Insertion sort: {insertion_sort(copy.copy(original))}")
    print(f"Selection sort: {selection_sort(copy.copy(original))}")
    print(f"Merge sort:     {merge_sort(copy.copy(original))}")

    arr_qs = copy.copy(original)
    quick_sort(arr_qs)
    print(f"Quick sort:     {arr_qs}")

    print("\n=== Complexity Comparison ===")
    header = f"{'Algorithm':<16} {'Best':>12} {'Average':>12} {'Worst':>12} {'Space':>8} {'Stable':>7}"
    print(header)
    print("-" * len(header))
    rows = [
        ("Bubble sort",    "O(n)",      "O(n²)",      "O(n²)",      "O(1)",      "Yes"),
        ("Insertion sort", "O(n)",      "O(n²)",      "O(n²)",      "O(1)",      "Yes"),
        ("Selection sort", "O(n²)",     "O(n²)",      "O(n²)",      "O(1)",      "No"),
        ("Merge sort",     "O(n log n)","O(n log n)", "O(n log n)", "O(n)",      "Yes"),
        ("Quick sort",     "O(n log n)","O(n log n)", "O(n²)",      "O(log n)",  "No"),
    ]
    for name, best, avg, worst, space, stable in rows:
        print(f"{name:<16} {best:>12} {avg:>12} {worst:>12} {space:>8} {stable:>7}")
