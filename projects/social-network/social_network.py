"""
Social Network — Graph-Based Mini Project
==========================================
A social network simulation built on a weighted undirected graph.

Each person is a NODE; each friendship is an EDGE with a connection
strength weight (1–10).

Features:
  - Add / remove members with profile metadata
  - Add / remove friendships with connection strength
  - Mutual friends discovery
  - Friend suggestions (friends-of-friends not yet connected)
  - Shortest social path between two people (BFS)
  - Community detection (connected components via DFS)
  - Influence score (degree centrality)

This project demonstrates:
  - Graph data structure (adjacency list)
  - BFS and DFS traversal algorithms
  - OOP design (Network + Member classes)
  - Python sets for efficient mutual-friend lookup
"""

from __future__ import annotations
from collections import deque
from typing import Optional


class Member:
    """Represents a social network user with profile attributes."""

    def __init__(self, name: str, age: int, interests: list[str]) -> None:
        self.name = name
        self.age = age
        self.interests = interests

    def __repr__(self) -> str:
        return f"Member(name={self.name!r}, age={self.age}, interests={self.interests})"

    def shared_interests(self, other: Member) -> set[str]:
        """Return interests this member shares with another."""
        return set(self.interests) & set(other.interests)


class SocialNetwork:
    """
    An undirected, weighted social network graph.

    Nodes  = Members
    Edges  = Friendships (weighted by connection strength 1–10)
    """

    def __init__(self, name: str = "My Network") -> None:
        self.name = name
        self._members: dict[str, Member] = {}
        self._connections: dict[str, dict[str, float]] = {}   # adjacency list

    # ── Member management ──────────────────────────────────────────────────────

    def add_member(self, name: str, age: int, interests: list[str]) -> None:
        """Add a new member to the network."""
        if name in self._members:
            print(f"  '{name}' is already a member.")
            return
        self._members[name] = Member(name, age, interests)
        self._connections[name] = {}
        print(f"  Added member: {name}")

    def remove_member(self, name: str) -> None:
        """Remove a member and all their connections."""
        if name not in self._members:
            raise KeyError(f"Member '{name}' not found.")
        for other in self._connections:
            self._connections[other].pop(name, None)
        del self._members[name]
        del self._connections[name]
        print(f"  Removed member: {name}")

    # ── Connection management ──────────────────────────────────────────────────

    def add_friendship(self, name1: str, name2: str, strength: float = 5.0) -> None:
        """
        Add a bidirectional friendship with a given strength (1–10).
        Higher strength = closer friends.
        """
        for name in (name1, name2):
            if name not in self._members:
                raise KeyError(f"Member '{name}' not found.")
        self._connections[name1][name2] = strength
        self._connections[name2][name1] = strength
        print(f"  {name1} <-> {name2} (strength: {strength})")

    def remove_friendship(self, name1: str, name2: str) -> None:
        """Remove the friendship between two members."""
        self._connections[name1].pop(name2, None)
        self._connections[name2].pop(name1, None)

    def friendship_strength(self, name1: str, name2: str) -> Optional[float]:
        """Return the strength of the friendship, or None if not friends."""
        return self._connections.get(name1, {}).get(name2)

    # ── Social intelligence ────────────────────────────────────────────────────

    def mutual_friends(self, name1: str, name2: str) -> set[str]:
        """Return the set of members who are friends with both name1 and name2."""
        friends1 = set(self._connections[name1])
        friends2 = set(self._connections[name2])
        return friends1 & friends2

    def friend_suggestions(self, name: str) -> list[str]:
        """
        Suggest new friends: friends-of-friends that are not already connected.
        Ordered by number of mutual friends (most mutual first).
        """
        my_friends = set(self._connections[name])
        suggestions: dict[str, int] = {}

        for friend in my_friends:
            for friend_of_friend in self._connections[friend]:
                if friend_of_friend != name and friend_of_friend not in my_friends:
                    suggestions[friend_of_friend] = suggestions.get(friend_of_friend, 0) + 1

        return sorted(suggestions, key=suggestions.get, reverse=True)

    def shortest_social_path(self, start: str, end: str) -> Optional[list[str]]:
        """
        Find the shortest chain of friendships between two members (BFS).
        Returns the path as a list of names, or None if no path exists.

        Time:  O(V + E)
        """
        if start == end:
            return [start]

        seen = {start}
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            current = path[-1]

            for neighbour in self._connections.get(current, {}):
                if neighbour == end:
                    return path + [neighbour]
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(path + [neighbour])

        return None

    def community_members(self, start: str) -> list[str]:
        """
        Return all members reachable from `start` via DFS.
        This identifies the connected community a member belongs to.

        Time:  O(V + E)
        """
        visited: list[str] = []
        seen: set[str] = set()

        def dfs(node: str) -> None:
            seen.add(node)
            visited.append(node)
            for neighbour in self._connections[node]:
                if neighbour not in seen:
                    dfs(neighbour)

        dfs(start)
        return visited

    def influence_score(self, name: str) -> int:
        """
        Return the influence score (degree centrality) of a member.
        Simply the number of direct connections — higher is more connected.
        """
        return len(self._connections[name])

    def most_influential(self) -> str:
        """Return the member with the most connections."""
        return max(self._members, key=self.influence_score)

    # ── Display ────────────────────────────────────────────────────────────────

    def display(self) -> None:
        """Print the full network state."""
        print(f"\n  Network: {self.name}")
        print(f"  Members ({len(self._members)}):")
        for member in self._members.values():
            friends = list(self._connections[member.name].keys())
            print(f"    {member.name} (age {member.age}) — friends: {friends}")

    def __repr__(self) -> str:
        return f"SocialNetwork(name={self.name!r}, members={len(self._members)})"


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Building the Social Network ===\n")
    net = SocialNetwork("CS Student Network")

    net.add_member("Gleb",   19, ["karate", "coding", "chess"])
    net.add_member("John",   20, ["football", "coding"])
    net.add_member("Tiago",  21, ["volleyball", "chess"])
    net.add_member("Lamine", 22, ["volleyball", "football"])
    net.add_member("Sara",   20, ["chess", "coding", "art"])

    print("\n=== Adding Friendships ===\n")
    net.add_friendship("Gleb",  "John",   strength=5)
    net.add_friendship("Gleb",  "Tiago",  strength=7)
    net.add_friendship("Tiago", "John",   strength=8)
    net.add_friendship("Tiago", "Lamine", strength=9)
    net.add_friendship("John",  "Lamine", strength=6)
    net.add_friendship("Sara",  "Gleb",   strength=4)

    net.display()

    print("\n=== Mutual Friends ===")
    mutual = net.mutual_friends("Gleb", "Tiago")
    print(f"  Gleb & Tiago share: {mutual}")         # {'John'}

    print("\n=== Friend Suggestions for Lamine ===")
    suggestions = net.friend_suggestions("Lamine")
    print(f"  Lamine might know: {suggestions}")

    print("\n=== Shared Interests ===")
    gleb = net._members["Gleb"]
    sara = net._members["Sara"]
    print(f"  Gleb & Sara share: {gleb.shared_interests(sara)}")   # chess, coding

    print("\n=== Shortest Social Path ===")
    path = net.shortest_social_path("Sara", "Lamine")
    if path:
        print(f"  Sara → Lamine: {' → '.join(path)}")

    print("\n=== Community Detection (DFS from Sara) ===")
    community = net.community_members("Sara")
    print(f"  Sara's community: {community}")

    print("\n=== Influence Scores ===")
    for name in net._members:
        score = net.influence_score(name)
        print(f"  {name}: {score} connection(s)")
    print(f"\n  Most influential: {net.most_influential()}")

    print("\n=== Remove a Member ===")
    net.remove_member("John")
    net.display()
