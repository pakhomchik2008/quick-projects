# Python Learning Portfolio

A structured collection of Python implementations covering core computer science
fundamentals — from algorithms and data structures to object-oriented design
and real-world mini-projects.

Built during FP016 Computer Science coursework and self-directed learning.

---

## Repository Map

```
quick-projects/
│
├── algorithms/
│   ├── searching/          Linear search, Binary search + complexity analysis
│   ├── sorting/            Bubble, Insertion, Selection, Merge, Quick sort
│   └── recursion/          Factorial, Fibonacci (naive vs memoised), Power
│
├── data-structures/
│   ├── stack/              LIFO stack, bracket checker, bisect exercises
│   ├── binary-tree/        BST, DFS traversals, inversion, left-leaf sum
│   └── graph/              Adjacency list, BFS, DFS, shortest path
│
├── object-oriented-programming/
│   ├── basics/             Classes, __init__, __str__, encapsulation, bank account
│   ├── inheritance/        RPG character hierarchy (3 levels deep)
│   ├── abstraction/        Abstract base classes, Shape hierarchy
│   └── polymorphism/       Marketplace with Buyer, Seller, Admin
│
└── projects/
    ├── weather-app/        REST API + abstract classes + formatter pattern
    ├── social-network/     Graph-based social network with BFS/DFS
    ├── bank-account/       OOP banking app with transaction history
    └── vehicle-rental/     Fleet management with inheritance hierarchy
```

---

## Topics Covered

### Object-Oriented Programming

| Concept | Where demonstrated |
|---------|-------------------|
| Classes and objects | `basics/oop_basics.py` |
| `__init__`, `__str__`, `__repr__` | All OOP files |
| Encapsulation (`_private`) | `basics/oop_basics.py`, `bank_account.py` |
| Inheritance (`super().__init__`) | `inheritance/rpg_characters.py` |
| Multi-level inheritance | NoviceWarrior → Warrior → Character |
| Abstract base classes | `abstraction/shapes.py`, `weather_app.py` |
| Polymorphism (method overriding) | `polymorphism/marketplace.py` |
| Properties (`@property`) | `bank_account.py` |
| Dataclasses (`@dataclass`) | `bank_account.py`, `vehicle_rental.py` |
| Composition | `bank_account.py`, `vehicle_rental.py` |

### Data Structures

| Structure | Abstraction | File |
|-----------|-------------|------|
| Stack | LIFO | `data-structures/stack/stack.py` |
| Binary Tree | Hierarchical | `data-structures/binary-tree/binary_tree.py` |
| Binary Search Tree | Ordered hierarchical | `data-structures/binary-tree/binary_tree.py` |
| Graph (adjacency list) | Network | `data-structures/graph/graph.py` |

### Algorithms

| Algorithm | Category | Complexity | File |
|-----------|----------|-----------|------|
| Linear search | Searching | O(n) | `algorithms/searching/` |
| Binary search | Searching | O(log n) | `algorithms/searching/` |
| Bubble sort | Sorting | O(n²) | `algorithms/sorting/` |
| Insertion sort | Sorting | O(n²) | `algorithms/sorting/` |
| Selection sort | Sorting | O(n²) | `algorithms/sorting/` |
| Merge sort | Sorting | O(n log n) | `algorithms/sorting/` |
| Quick sort | Sorting | O(n log n) avg | `algorithms/sorting/` |
| Factorial (recursive) | Recursion | O(n) | `algorithms/recursion/` |
| Fibonacci (naive) | Recursion | O(2^n) | `algorithms/recursion/` |
| Fibonacci (memoised) | Dynamic programming | O(n) | `algorithms/recursion/` |
| Fast power | Recursion | O(log n) | `algorithms/recursion/` |
| BFS | Graph traversal | O(V+E) | `data-structures/graph/`, `projects/social-network/` |
| DFS | Graph traversal | O(V+E) | `data-structures/graph/`, `projects/social-network/` |
| Tree traversals (in/pre/post) | Tree algorithms | O(n) | `data-structures/binary-tree/` |

### Projects

| Project | Key Concepts | Technologies |
|---------|-------------|-------------|
| [Weather App](projects/weather-app/) | Abstract classes, REST API, error handling | `requests`, `abc` |
| [Social Network](projects/social-network/) | Graph algorithms, BFS/DFS, OOP | Pure Python |
| [Bank Account](projects/bank-account/) | Encapsulation, dataclasses, transaction records | Pure Python |
| [Vehicle Rental](projects/vehicle-rental/) | Inheritance hierarchy, composition, polymorphism | Pure Python |

### Python Features

- Type hints (`list[int]`, `Optional[str]`, `dict[str, float]`)
- `@dataclass` and `@dataclass(frozen=True)` for immutable records
- `@property` for controlled attribute access
- `@lru_cache` for memoisation
- `functools`, `collections.deque`, `bisect` standard library modules
- `abc.ABC` and `@abstractmethod`
- `__str__`, `__repr__`, `__len__`, `__init__` dunder methods
- f-strings, list comprehensions, set operations
- `try / except` for structured error handling
- Environment variables via `os.getenv`

---

## Learning Progression

```
Week 1–2   Classes, objects, __init__, __str__
           ↓
Week 3–4   Inheritance, super(), method overriding
           ↓
Week 5–6   Abstract base classes, polymorphism
           ↓
Week 7–8   Linear and binary search algorithms
           ↓
Week 9–10  Sorting algorithms (O(n²) → O(n log n))
           ↓
Week 11–12 Recursion (factorial, Fibonacci, memoisation)
           ↓
Week 13–14 Stack and binary tree data structures
           ↓
Week 15–16 Graph theory (BFS, DFS, shortest path)
           ↓
Week 17+   Full projects: weather app, social network, bank, rental system
```

---

## Setup

```bash
git clone <repo-url>
cd quick-projects

# Create virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# Install dependencies (only needed for the weather app)
pip install requests
```

## Running Examples

Every file has a runnable `if __name__ == "__main__"` block:

```bash
# Algorithms
python algorithms/searching/searching.py
python algorithms/sorting/sorting.py
python algorithms/recursion/recursion.py

# Data Structures
python data-structures/stack/stack.py
python data-structures/binary-tree/binary_tree.py
python data-structures/graph/graph.py

# OOP
python object-oriented-programming/basics/oop_basics.py
python object-oriented-programming/inheritance/rpg_characters.py
python object-oriented-programming/abstraction/shapes.py
python object-oriented-programming/polymorphism/marketplace.py

# Projects
python projects/social-network/social_network.py
python projects/bank-account/bank_account.py
python projects/vehicle-rental/vehicle_rental.py
python projects/weather-app/weather_app.py   # Requires API key
```

---

## Key Design Decisions

**Every algorithm file includes:**
- Full docstring with time and space complexity
- A human-readable explanation of the approach
- A runnable `__main__` block with example output
- A printed complexity comparison table

**Every OOP file includes:**
- Docstrings on every class and method
- Type hints throughout
- `__str__` and `__repr__` on every class
- A runnable `__main__` demonstration

**Bug fixes applied from original coursework:**
- Merge sort: moved `left[i:]` append outside the `while` loop
- Insertion sort: corrected loop bounds and removed early `return`
- `Rectangle.area()`: corrected to `width × height` (not `π × width × height`)
- `Triangle.area()`: implemented Heron's formula (was `a × b × c`)
- `Rogue.__init__`: removed duplicate `self` in `super().__init__(self, ...)`
- `NoviceWarrior` / `AdvancedWarrior` / `IntermediateWarrior`: same fix
- `Character` methods: moved out of `__init__` to correct class level
- Binary tree `in_order`: added missing right-child traversal call

---

*Built with Python 3.12+ | University coursework + independent study*
