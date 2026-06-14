"""
Recursion
=========
Demonstrations of recursive problem-solving using classic CS examples.

Every recursive function must have:
  1. A BASE CASE  — the simplest input with a known answer (stops the recursion)
  2. A RECURSIVE CASE — reduces the problem toward the base case

Problems covered:
  - Factorial         n! = n * (n-1) * ... * 1
  - Fibonacci         F(n) = F(n-1) + F(n-2)
  - Power             x^n = x * x^(n-1)
  - Binary search     (recursive version — see also algorithms/searching/)
  - Sum of digits     sum_digits(123) = 1 + 2 + 3
"""

from functools import lru_cache


# ── Factorial ──────────────────────────────────────────────────────────────────

def factorial_recursive(n: int) -> int:
    """
    Compute n! recursively.

    Mathematical definition:
        0! = 1          (base case)
        n! = n * (n-1)! (recursive case)

    Time:  O(n) — n recursive calls
    Space: O(n) — n frames on the call stack

    Args:
        n: A non-negative integer.

    Returns:
        n factorial.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1                              # Base case
    return n * factorial_recursive(n - 1)    # Recursive case


def factorial_iterative(n: int) -> int:
    """
    Compute n! iteratively (no recursion).
    Included for comparison — same result, O(1) space.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ── Fibonacci ──────────────────────────────────────────────────────────────────

def fibonacci_naive(n: int) -> int:
    """
    Compute the nth Fibonacci number using naive recursion.

    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

    WARNING: This is O(2^n) time because it recomputes the same sub-problems
    repeatedly. Use fibonacci_memo() for any meaningful n.

    Time:  O(2^n) — exponential (demonstrates why memoisation matters)
    Space: O(n)   — maximum recursion depth
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """
    Compute the nth Fibonacci number with memoisation (top-down DP).

    @lru_cache stores results of previous calls so each sub-problem is
    solved only once, reducing time from O(2^n) to O(n).

    Time:  O(n)
    Space: O(n) — cache + call stack
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Compute the nth Fibonacci number iteratively (bottom-up DP).
    Most efficient: O(n) time, O(1) space.
    """
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


# ── Power ──────────────────────────────────────────────────────────────────────

def power(base: float, exp: int) -> float:
    """
    Compute base^exp recursively.

    Uses fast exponentiation (exponentiation by squaring):
      x^n = (x^(n//2))^2       if n is even
      x^n = x * (x^(n//2))^2  if n is odd

    Time:  O(log n)
    Space: O(log n)
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)

    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half


# ── Sum of digits ──────────────────────────────────────────────────────────────

def sum_of_digits(n: int) -> int:
    """
    Return the sum of digits of a non-negative integer.

    Example: sum_of_digits(1234) = 1 + 2 + 3 + 4 = 10

    Time:  O(d) where d = number of digits
    Space: O(d)
    """
    n = abs(n)
    if n < 10:
        return n                                  # Base case: single digit
    return (n % 10) + sum_of_digits(n // 10)     # Last digit + rest


# ── Binary search (recursive) ─────────────────────────────────────────────────

def binary_search(arr: list[int], target: int, left: int = 0, right: int = None):
    """
    Recursive binary search — see algorithms/searching/ for full analysis.

    Time:  O(log n)
    Space: O(log n)
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return None

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Factorial ===")
    for n in [0, 1, 5, 10]:
        r = factorial_recursive(n)
        i = factorial_iterative(n)
        print(f"  {n}! = {r}  (iterative matches: {r == i})")

    print("\n=== Fibonacci ===")
    sequence = [fibonacci_memo(i) for i in range(12)]
    print(f"  F(0..11) = {sequence}")
    print(f"  F(30) memo    = {fibonacci_memo(30)}")
    print(f"  F(30) iterative = {fibonacci_iterative(30)}")

    print("\n=== Power (fast exponentiation) ===")
    print(f"  2^10  = {power(2, 10)}")   # 1024
    print(f"  3^5   = {power(3, 5)}")    # 243
    print(f"  2^-3  = {power(2, -3)}")   # 0.125

    print("\n=== Sum of Digits ===")
    print(f"  sum_of_digits(1234) = {sum_of_digits(1234)}")   # 10
    print(f"  sum_of_digits(9999) = {sum_of_digits(9999)}")   # 36

    print("\n=== Recursive Binary Search ===")
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"  List: {sorted_list}")
    print(f"  Search 7  → index {binary_search(sorted_list, 7)}")   # 3
    print(f"  Search 10 → index {binary_search(sorted_list, 10)}")  # None

    print("\n=== Why Memoisation Matters ===")
    import time
    n = 35
    t0 = time.perf_counter()
    fibonacci_naive(n)
    naive_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    fibonacci_memo.cache_clear()
    fibonacci_memo(n)
    memo_time = time.perf_counter() - t0

    print(f"  fibonacci_naive({n}):  {naive_time:.4f}s")
    print(f"  fibonacci_memo({n}):   {memo_time:.6f}s")
    print(f"  Speedup: ~{naive_time / (memo_time + 1e-9):.0f}x")
