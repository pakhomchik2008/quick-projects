# Object-Oriented Programming

Four pillars of OOP demonstrated through progressively complex examples.

---

## The Four Pillars

| Pillar | Meaning | Folder |
|--------|---------|--------|
| **Encapsulation** | Bundle data and behaviour; hide internal state | [`basics/`](basics/) |
| **Abstraction** | Expose only necessary interfaces; hide complexity | [`abstraction/`](abstraction/) |
| **Inheritance** | Build specialised classes from general ones | [`inheritance/`](inheritance/) |
| **Polymorphism** | Same interface, different behaviour per type | [`polymorphism/`](polymorphism/) |

---

## Contents

### `basics/` — Classes and Objects

First principles: `__init__`, `__str__`, `__repr__`, class attributes vs instance attributes,
encapsulated bank account with private `_balance` property, register/login pattern.

### `inheritance/` — RPG Character Hierarchy

Three-level inheritance tree:

```
Character
    ├── Warrior ──── NoviceWarrior
    │            ├── IntermediateWarrior
    │            └── AdvancedWarrior
    ├── Mage
    └── Rogue
```

Demonstrates `super().__init__()`, method overriding, class-level constants.

### `abstraction/` — Shape Hierarchy with ABC

Abstract base class enforcing a contract:

```
Shape (ABC)
    ├── Circle      — area = π r²
    ├── Rectangle   — area = width × height
    └── Triangle    — area via Heron's formula
```

`Shape` cannot be instantiated directly. Every subclass must implement `area()` and `perimeter()`.

### `polymorphism/` — Marketplace

```
User (base)
    ├── Buyer   — browse(), purchase()
    ├── Seller  — list_item(), show_listings(), revenue()
    └── Admin   — view_all_users(), reject_account()
```

The same `describe()` call produces different output depending on the actual type —
this is polymorphism.

---

## How to Run

```bash
python object-oriented-programming/basics/oop_basics.py
python object-oriented-programming/inheritance/rpg_characters.py
python object-oriented-programming/abstraction/shapes.py
python object-oriented-programming/polymorphism/marketplace.py
```
