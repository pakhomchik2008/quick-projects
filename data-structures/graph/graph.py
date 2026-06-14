"""
Graph Data Structure
====================
A graph represents relationships between entities (nodes/vertices)
using connections (edges).

This implementation uses an ADJACENCY LIST — a dictionary where each key
is a node and its value is a dictionary of neighbours with edge weights.

Adjacency list vs adjacency matrix:
  Adjacency list   — O(V + E) space, efficient for sparse graphs
  Adjacency matrix — O(V²)   space, faster lookup for dense graphs

Graph types:
  Undirected — edges have no direction (friendship is mutual)
  Directed   — edges have direction (A follows B does not mean B follows A)
  Weighted   — edges carry a numeric value (connection strength, distance)

Algorithms demonstrated:
  BFS (Breadth-First Search)  — shortest path in unweighted graphs
  DFS (Depth-First Search)    — reachability, connected components
"""

from collections import deque
from typing import Optional


class Graph:
    """
    Weighted, optionally directed graph using an adjacency list.

    Nodes are identified by any hashable value (here: strings for names).
    Edges carry a numeric weight (default 1).
    """

    def __init__(self, directed: bool = False) -> None:
        self._adjacency: dict[str, dict[str, float]] = {}
        self._node_data: dict[str, dict] = {}
        self.directed = directed

    # ── Node management ────────────────────────────────────────────────────────

    def add_node(self, name: str, **attributes) -> None:
        """
        Add a node with optional metadata attributes.

        Time:  O(1)
        """
        if name not in self._adjacency:
            self._adjacency[name] = {}
            self._node_data[name] = attributes

    def remove_node(self, name: str) -> None:
        """
        Remove a node and all edges that connect to it.

        Time:  O(V + E)
        """
        if name not in self._adjacency:
            raise KeyError(f"Node '{name}' does not exist.")

        # Remove every edge that points to this node
        for neighbour_edges in self._adjacency.values():
            neighbour_edges.pop(name, None)

        del self._adjacency[name]
        del self._node_data[name]

    # ── Edge management ────────────────────────────────────────────────────────

    def add_edge(self, u: str, v: str, weight: float = 1) -> None:
        """
        Add a weighted edge between nodes u and v.
        For an undirected graph, both directions are added.

        Time:  O(1)
        """
        if u not in self._adjacency or v not in self._adjacency:
            raise KeyError("Both nodes must exist before adding an edge.")
        self._adjacency[u][v] = weight
        if not self.directed:
            self._adjacency[v][u] = weight

    def remove_edge(self, u: str, v: str) -> None:
        """Remove the edge between u and v."""
        self._adjacency[u].pop(v, None)
        if not self.directed:
            self._adjacency[v].pop(u, None)

    # ── Query operations ───────────────────────────────────────────────────────

    def neighbours(self, node: str) -> list[str]:
        """Return all neighbours of a node."""
        return list(self._adjacency[node].keys())

    def edge_weight(self, u: str, v: str) -> Optional[float]:
        """Return the weight of edge (u, v), or None if no edge exists."""
        return self._adjacency[u].get(v)

    def mutual_connections(self, u: str, v: str) -> set[str]:
        """
        Return nodes connected to both u and v.
        Analogous to mutual friends on a social network.

        Time:  O(degree(u) + degree(v))
        """
        neighbours_u = set(self._adjacency[u])
        neighbours_v = set(self._adjacency[v])
        return neighbours_u.intersection(neighbours_v)

    # ── Graph traversal algorithms ─────────────────────────────────────────────

    def bfs(self, start: str) -> list[str]:
        """
        Breadth-First Search from `start`.
        Visits nodes level by level (closest nodes first).
        BFS gives the shortest path (fewest hops) in unweighted graphs.

        Time:  O(V + E)
        Space: O(V) — visited set and queue
        """
        if start not in self._adjacency:
            return []

        visited = []
        seen = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()
            visited.append(node)
            for neighbour in self._adjacency[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)

        return visited

    def dfs(self, start: str) -> list[str]:
        """
        Depth-First Search from `start`.
        Explores as far as possible along each branch before backtracking.
        DFS is used for reachability, cycle detection, and topological sort.

        Time:  O(V + E)
        Space: O(V)
        """
        if start not in self._adjacency:
            return []

        visited = []
        seen: set[str] = set()

        def _dfs(node: str) -> None:
            seen.add(node)
            visited.append(node)
            for neighbour in self._adjacency[node]:
                if neighbour not in seen:
                    _dfs(neighbour)

        _dfs(start)
        return visited

    def shortest_path(self, start: str, end: str) -> Optional[list[str]]:
        """
        Find the shortest path (fewest hops) between two nodes using BFS.

        Time:  O(V + E)
        Space: O(V)

        Returns:
            List of nodes forming the path, or None if no path exists.
        """
        if start == end:
            return [start]

        seen = {start}
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            for neighbour in self._adjacency.get(node, {}):
                if neighbour == end:
                    return path + [neighbour]
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(path + [neighbour])

        return None   # No path found

    # ── Display ────────────────────────────────────────────────────────────────

    def display(self) -> None:
        """Print the adjacency list and node metadata."""
        print("Nodes:")
        for name, attrs in self._node_data.items():
            print(f"  {name}: {attrs}")
        print("Edges:")
        seen_edges: set[frozenset] = set()
        for u, neighbours in self._adjacency.items():
            for v, w in neighbours.items():
                key = frozenset({u, v})
                if self.directed or key not in seen_edges:
                    print(f"  {u} {'→' if self.directed else '—'} {v}  (weight: {w})")
                    seen_edges.add(key)

    def __repr__(self) -> str:
        return (
            f"Graph(nodes={list(self._adjacency.keys())}, "
            f"directed={self.directed})"
        )


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Social Network Graph ===\n")
    network = Graph(directed=False)

    # Add members with metadata
    network.add_node("Gleb",   age=19, interests=["karate", "coding"])
    network.add_node("John",   age=20, interests=["football"])
    network.add_node("Tiago",  age=21, interests=["volleyball"])
    network.add_node("Lamine", age=22, interests=["volleyball"])

    # Add relationships with connection strength weights
    network.add_edge("Gleb",  "John",  weight=5)
    network.add_edge("Gleb",  "Tiago", weight=7)
    network.add_edge("Tiago", "John",  weight=8)
    network.add_edge("Tiago", "Lamine", weight=9)

    network.display()

    print("\n=== Mutual Connections ===")
    mutual = network.mutual_connections("Gleb", "Tiago")
    print(f"  Gleb and Tiago both know: {mutual}")   # {'John'}

    mutual2 = network.mutual_connections("Gleb", "Lamine")
    print(f"  Gleb and Lamine both know: {mutual2}")  # {'Tiago'}

    print("\n=== BFS from Gleb ===")
    print(f"  Visit order: {network.bfs('Gleb')}")

    print("\n=== DFS from Gleb ===")
    print(f"  Visit order: {network.dfs('Gleb')}")

    print("\n=== Shortest Path ===")
    path = network.shortest_path("Gleb", "Lamine")
    print(f"  Gleb → Lamine: {' → '.join(path)}")  # Gleb → Tiago → Lamine

    print("\n=== Remove a Member ===")
    network.remove_node("John")
    print(f"  After removing John: {network}")
    print(f"  Gleb's neighbours: {network.neighbours('Gleb')}")
