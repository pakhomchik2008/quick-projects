"""
OOP Basics
==========
Introduction to Python classes and objects — the four key concepts:

  ENCAPSULATION  — bundling data and behaviour into a single unit (class)
  ABSTRACTION    — exposing only what is necessary, hiding internal detail
  INHERITANCE    — building new classes from existing ones (covered in inheritance/)
  POLYMORPHISM   — treating different object types through a common interface

This file demonstrates:
  - Class definition, __init__, instance attributes
  - The __str__ and __repr__ dunder methods
  - Class attributes vs instance attributes
  - A simple module-import example
  - A register/login pattern with a bank account CLI
"""


# ── Basic class anatomy ────────────────────────────────────────────────────────

class Person:
    """
    Represents a person.

    Demonstrates __init__ (constructor) and __str__ (human-readable string).
    """

    species: str = "Homo sapiens"   # Class attribute — shared by all instances

    def __init__(self, name: str, age: int) -> None:
        # Instance attributes — unique to each object
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """Called by print() and str() — user-friendly representation."""
        return f"{self.name} (age {self.age})"

    def __repr__(self) -> str:
        """Called in the REPL and for debugging — unambiguous representation."""
        return f"Person(name={self.name!r}, age={self.age!r})"

    def greet(self) -> str:
        return f"Hi, I'm {self.name}!"


# ── Random number generation with seeding ─────────────────────────────────────

def random_demo() -> None:
    """
    Demonstrate the random module and the effect of seeding.

    Seeding with a fixed value makes results reproducible.
    Seeding with time.time() gives a different sequence each run.
    """
    import random
    import time

    print("Fixed seed (same every run):")
    random.seed(10)
    for _ in range(3):
        print(f"  {random.random():.6f}")

    print("Time-based seed (different each run):")
    random.seed(time.time())
    for _ in range(3):
        print(f"  {random.random():.6f}")


# ── Bank Account — a complete OOP mini-application ────────────────────────────

class Account:
    """
    A simple bank account demonstrating encapsulation.
    Balance is kept private; all mutations go through methods.
    """

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance: float = 0.0          # Convention: _ means 'private'

    @property
    def balance(self) -> float:
        """Read-only access to the balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"  Deposited £{amount:.2f}. Balance: £{self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        print(f"  Withdrew £{amount:.2f}. Balance: £{self._balance:.2f}")

    def __str__(self) -> str:
        return f"Account(owner={self.owner!r}, balance=£{self._balance:.2f})"


class User:
    """Stores login credentials."""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self._password = password          # Never store plain-text passwords in real code

    def check_password(self, password: str) -> bool:
        return self._password == password


class BankApp:
    """
    Combines User authentication with Account management.
    Demonstrates encapsulation: the UI (run()) drives internal objects.
    """

    def __init__(self) -> None:
        self._users: dict[str, User] = {}
        self._accounts: dict[str, Account] = {}

    def register(self, username: str, password: str) -> None:
        if username in self._users:
            print(f"  Username '{username}' is already taken.")
            return
        self._users[username] = User(username, password)
        self._accounts[username] = Account(username)
        print(f"  Registered '{username}' successfully.")

    def login(self, username: str, password: str) -> Optional_Account:
        user = self._users.get(username)
        if user and user.check_password(password):
            print(f"  Welcome back, {username}!")
            return self._accounts[username]
        print("  Invalid username or password.")
        return None


# Avoid importing typing just for one annotation — use a string alias
Optional_Account = "Optional[Account]"  # type: ignore[assignment]


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Person Class ===")
    p1 = Person("Alice", 21)
    p2 = Person("Bob", 25)
    print(f"  {p1}")           # Alice (age 21)
    print(f"  {p1.greet()}")   # Hi, I'm Alice!
    print(f"  repr: {p1!r}")
    print(f"  Species (class attr): {Person.species}")

    print("\n=== Random Module Demo ===")
    random_demo()

    print("\n=== Bank Account ===")
    acc = Account("Gleb")
    acc.deposit(500)
    acc.deposit(200)
    acc.withdraw(100)
    print(f"  {acc}")

    try:
        acc.withdraw(700)
    except ValueError as e:
        print(f"  Error: {e}")

    print("\n=== BankApp (register + login) ===")
    app = BankApp()
    app.register("gleb", "secret123")
    app.register("gleb", "other")           # Duplicate — should fail
    account = app.login("gleb", "secret123")
    if account:
        account.deposit(1000)
        account.withdraw(250)
        print(f"  Final: {account}")
    app.login("gleb", "wrongpassword")
