"""
Binary Tree
===========
A binary tree is a hierarchical data structure where each node has at most
two children: a left child and a right child.

This module implements:
  - BinaryTree with manual node linking
  - BinarySearchTree with automatic insert and search
  - Three DFS traversal orders (in-order, pre-order, post-order)
  - Tree inversion (mirror)
  - Sum of left leaves
  - Tree height

Traversal orders (for a tree rooted at N with left L and right R):
  In-order   (L → N → R): yields nodes in sorted order for a BST
  Pre-order  (N → L → R): useful for copying/serialising a tree
  Post-order (L → R → N): useful for deleting a tree (children before parent)
"""

from __future__ import annotations
from typing import Optional


class Node:
    """A single node in a binary tree."""

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


# ── Traversals ─────────────────────────────────────────────────────────────────

def inorder(node: Optional[Node]) -> list[int]:
    """
    In-order traversal: Left → Root → Right.
    For a BST this produces elements in ascending sorted order.

    Time:  O(n) — visits every node once
    Space: O(h) — h is the tree height (recursion stack)
    """
    if node is None:
        return []
    return inorder(node.left_child) + [node.data] + inorder(node.right_child)


def preorder(node: Optional[Node]) -> list[int]:
    """
    Pre-order traversal: Root → Left → Right.
    Visits the root before its subtrees — useful for tree serialisation.
    """
    if node is None:
        return []
    return [node.data] + preorder(node.left_child) + preorder(node.right_child)


def postorder(node: Optional[Node]) -> list[int]:
    """
    Post-order traversal: Left → Right → Root.
    Visits children before the parent — useful for safely deleting a tree.
    """
    if node is None:
        return []
    return postorder(node.left_child) + postorder(node.right_child) + [node.data]


# ── Tree operations ────────────────────────────────────────────────────────────

def tree_height(node: Optional[Node]) -> int:
    """
    Return the height of the tree (longest path from root to any leaf).
    An empty tree has height 0; a single node has height 1.

    Time:  O(n)
    Space: O(h)
    """
    if node is None:
        return 0
    return 1 + max(tree_height(node.left_child), tree_height(node.right_child))


def invert_tree(node: Optional[Node]) -> Optional[Node]:
    """
    Mirror the tree by swapping every node's left and right children.

    Example:
          4               4
         / \\    →       / \\
        2   7          7   2
       / \\ / \\       / \\ / \\
      1  3 6  9     9  6 3  1

    Time:  O(n)
    Space: O(h)
    """
    if node is None:
        return None
    node.left_child, node.right_child = node.right_child, node.left_child
    invert_tree(node.left_child)
    invert_tree(node.right_child)
    return node


def sum_of_left_leaves(node: Optional[Node]) -> int:
    """
    Return the sum of all left leaf nodes in the tree.
    A leaf node has no children.

    Example tree:
          3
         / \\
        9   20
           /  \\
          15    7
    Left leaves: 9 and 15 → sum = 24

    Time:  O(n)
    Space: O(h)
    """
    if node is None:
        return 0

    total = 0

    if node.left_child is not None:
        if node.left_child.left_child is None and node.left_child.right_child is None:
            total += node.left_child.data      # Left child is a leaf
        else:
            total += sum_of_left_leaves(node.left_child)

    total += sum_of_left_leaves(node.right_child)
    return total


# ── Binary Search Tree ─────────────────────────────────────────────────────────

class BinarySearchTree:
    """
    Binary Search Tree (BST) with automatic insertion and search.

    BST property: for every node N,
        all values in the LEFT subtree  < N.data
        all values in the RIGHT subtree > N.data

    This property means in-order traversal always yields sorted output,
    and average-case search/insert is O(log n).
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, data: int) -> None:
        """
        Insert a value into the BST, maintaining the BST property.

        Time:  O(log n) average, O(n) worst case (degenerate/skewed tree)
        Space: O(h) — recursion stack
        """
        self.root = self._insert(self.root, data)

    def _insert(self, node: Optional[Node], data: int) -> Node:
        if node is None:
            return Node(data)
        if data < node.data:
            node.left_child = self._insert(node.left_child, data)
        elif data > node.data:
            node.right_child = self._insert(node.right_child, data)
        # Duplicate values are ignored
        return node

    def search(self, data: int) -> bool:
        """
        Return True if `data` exists in the BST.

        Time:  O(log n) average
        Space: O(h)
        """
        return self._search(self.root, data)

    def _search(self, node: Optional[Node], data: int) -> bool:
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left_child, data)
        else:
            return self._search(node.right_child, data)

    def sorted_values(self) -> list[int]:
        """Return all values in ascending order via in-order traversal."""
        return inorder(self.root)

    def height(self) -> int:
        """Return the height of the BST."""
        return tree_height(self.root)


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Manual Binary Tree (from classwork exercises) ===")
    #
    #          4
    #         / \
    #        2   7
    #       / \ / \
    #      1  3 6  9
    #
    n1 = Node(4)
    n2 = Node(2)
    n3 = Node(7)
    n4 = Node(1)
    n5 = Node(3)
    n6 = Node(6)
    n7 = Node(9)

    n1.left_child = n2;  n1.right_child = n3
    n2.left_child = n4;  n2.right_child = n5
    n3.left_child = n6;  n3.right_child = n7

    print(f"  In-order   (sorted): {inorder(n1)}")     # [1, 2, 3, 4, 6, 7, 9]
    print(f"  Pre-order  (root first): {preorder(n1)}")  # [4, 2, 1, 3, 7, 6, 9]
    print(f"  Post-order (root last):  {postorder(n1)}") # [1, 3, 2, 6, 9, 7, 4]
    print(f"  Height: {tree_height(n1)}")               # 3

    print("\n=== Tree Inversion (Mirror) ===")
    print(f"  Before: {inorder(n1)}")   # [1, 2, 3, 4, 6, 7, 9]
    invert_tree(n1)
    print(f"  After:  {inorder(n1)}")   # [9, 7, 6, 4, 3, 2, 1]

    print("\n=== Sum of Left Leaves ===")
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15    7
    root = Node(3)
    root.left_child = Node(9)
    root.right_child = Node(20)
    root.right_child.left_child = Node(15)
    root.right_child.right_child = Node(7)
    print(f"  Left leaves sum: {sum_of_left_leaves(root)}")  # 9 + 15 = 24

    print("\n=== Binary Search Tree (auto-insert) ===")
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8, 2]
    for v in values:
        bst.insert(v)
    print(f"  Inserted: {values}")
    print(f"  Sorted (in-order): {bst.sorted_values()}")  # [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"  Height: {bst.height()}")
    print(f"  Search 4: {bst.search(4)}")   # True
    print(f"  Search 9: {bst.search(9)}")   # False
