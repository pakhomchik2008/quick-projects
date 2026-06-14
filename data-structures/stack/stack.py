"""
Stack Data Structure
====================
A stack is a Last-In, First-Out (LIFO) collection.
The last item pushed is always the first item popped — like a pile of plates.

Real-world uses:
  - Undo/redo in text editors
  - Browser back-button history
  - Function call stack in every program
  - Syntax/bracket matching in compilers
  - DFS graph traversal

All core operations are O(1) time.
"""

import bisect
from typing import Optional, TypeVar

T = TypeVar("T")


class Stack:
    """
    Generic LIFO stack backed by a Python list.

    Operations:
        push(item)  — O(1) amortised
        pop()       — O(1)
        peek()      — O(1)
        is_empty()  — O(1)
        size()      — O(1)
    """

    def __init__(self) -> None:
        self._items: list = []

    def push(self, item) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack(top={self._items[-1] if self._items else 'empty'}, size={self.size()})"

    def __len__(self) -> int:
        return self.size()


# ── Stack exercises ────────────────────────────────────────────────────────────

def move_top(source: Stack, destination: Stack) -> None:
    """
    Move the top element of `source` onto the top of `destination`.

    Time:  O(1)
    Space: O(1)
    """
    if source.is_empty():
        raise IndexError("Cannot move from an empty stack.")
    destination.push(source.pop())


def reverse_stack(stack: Stack) -> Stack:
    """
    Reverse the order of all elements in a stack.

    Uses a temporary stack: pop everything onto it (reverses order),
    then pop everything back (reverses again — restoring order in source,
    but the temp stack now holds the reversed result).

    Time:  O(n)
    Space: O(n) — temporary stack
    """
    temp = Stack()
    while not stack.is_empty():
        temp.push(stack.pop())
    return temp


def is_balanced(expression: str) -> bool:
    """
    Check whether an expression has balanced brackets using a stack.

    Every opening bracket is pushed; every closing bracket must match
    the most recently pushed opening bracket (LIFO property).

    Examples:
        is_balanced("([]{})")  → True
        is_balanced("([)]")    → False
        is_balanced("((")      → False

    Time:  O(n)
    Space: O(n)
    """
    opening = set("([{")
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()   # True only if all brackets were matched


# ── Bisect module demo ─────────────────────────────────────────────────────────

def sorted_insert_position(sorted_list: list[int], value: int) -> tuple[int, int]:
    """
    Find the left and right positions to insert `value` into `sorted_list`
    while maintaining sorted order, using the bisect module.

    bisect_left  → leftmost position (before existing equal values)
    bisect_right → rightmost position (after existing equal values)

    Time:  O(log n)
    """
    left_pos = bisect.bisect_left(sorted_list, value)
    right_pos = bisect.bisect_right(sorted_list, value)
    return left_pos, right_pos


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Stack Basics ===")
    s = Stack()
    for value in [10, 20, 30, 40, 50]:
        s.push(value)
        print(f"  Pushed {value:>3} | {s}")

    print(f"\n  Peek:      {s.peek()}")
    print(f"  Pop:       {s.pop()}")
    print(f"  After pop: {s}")

    print("\n=== Move Top ===")
    a = Stack()
    b = Stack()
    for v in [1, 2, 3, 4, 5]:
        a.push(v)
    print(f"  Before → A: {a._items}  B: {b._items}")
    move_top(a, b)
    print(f"  After  → A: {a._items}  B: {b._items}")

    print("\n=== Reverse Stack ===")
    original = Stack()
    for v in [1, 2, 3, 4, 5]:
        original.push(v)
    print(f"  Original (top→bottom): {list(reversed(original._items))}")
    reversed_stack = reverse_stack(original)
    print(f"  Reversed (top→bottom): {list(reversed(reversed_stack._items))}")

    print("\n=== Balanced Brackets ===")
    test_cases = ["([]{})", "([)]", "((", "{[()]}", ""]
    for expr in test_cases:
        result = is_balanced(expr)
        print(f"  {expr!r:<12} → {'balanced' if result else 'NOT balanced'}")

    print("\n=== Bisect: Sorted Insert Position ===")
    data = [1, 2, 3, 4, 4, 4, 4, 5, 6, 8]
    value = 4
    left, right = sorted_insert_position(data, value)
    print(f"  List:  {data}")
    print(f"  Value: {value}")
    print(f"  Left position:  {left}  (insert before index {left})")
    print(f"  Right position: {right} (insert before index {right})")
    print(f"  There are {right - left} existing copies of {value} in the list.")
