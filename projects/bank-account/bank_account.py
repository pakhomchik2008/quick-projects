"""
Bank Account — OOP Mini Project
=================================
A fully object-oriented command-line banking application.

Architecture:
  - Account       — stores balance; exposes deposit/withdraw/statement
  - User          — stores credentials; handles authentication
  - Bank          — manages all users and accounts; entry point
  - Transaction   — immutable record of each account operation

Concepts demonstrated:
  - Encapsulation: balance is private (_balance), accessed only through methods
  - Composition: Bank owns Users; Users own Accounts
  - Dunder methods: __str__, __repr__
  - Properties: balance is a read-only @property
  - Exception handling for invalid operations
  - Data classes for immutable records (Transaction)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ── Transaction record ─────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Transaction:
    """
    Immutable record of a single account operation.
    frozen=True means fields cannot be changed after creation.
    """
    kind: str           # 'DEPOSIT' or 'WITHDRAWAL'
    amount: float
    balance_after: float
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self) -> str:
        sign = "+" if self.kind == "DEPOSIT" else "-"
        return (
            f"  {self.timestamp}  {self.kind:<12}"
            f"  {sign}£{self.amount:>8.2f}  "
            f"Balance: £{self.balance_after:.2f}"
        )


# ── Account ────────────────────────────────────────────────────────────────────

class Account:
    """
    A bank account with a running balance and transaction history.
    Balance is encapsulated — only accessible via the balance property.
    """

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance: float = 0.0
        self._transactions: list[Transaction] = []

    @property
    def balance(self) -> float:
        """Read-only balance — cannot be set directly from outside."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """
        Credit the account.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive, got £{amount:.2f}.")
        self._balance += amount
        self._transactions.append(
            Transaction("DEPOSIT", amount, self._balance)
        )
        print(f"  Deposited £{amount:.2f}. New balance: £{self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """
        Debit the account.

        Raises:
            ValueError: If amount is not positive or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive, got £{amount:.2f}.")
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds: tried to withdraw £{amount:.2f}, "
                f"balance is £{self._balance:.2f}."
            )
        self._balance -= amount
        self._transactions.append(
            Transaction("WITHDRAWAL", amount, self._balance)
        )
        print(f"  Withdrew £{amount:.2f}. New balance: £{self._balance:.2f}")

    def statement(self) -> None:
        """Print a formatted account statement."""
        print(f"\n  Account Statement — {self.owner}")
        print("  " + "=" * 60)
        if not self._transactions:
            print("  No transactions yet.")
        else:
            for tx in self._transactions:
                print(tx)
        print("  " + "-" * 60)
        print(f"  Current balance: £{self._balance:.2f}\n")

    def __str__(self) -> str:
        return f"Account(owner={self.owner!r}, balance=£{self._balance:.2f})"

    def __repr__(self) -> str:
        return self.__str__()


# ── User ───────────────────────────────────────────────────────────────────────

class User:
    """
    A bank customer with login credentials and an associated account.
    """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self._password = password
        self.account: Account = Account(owner=username)

    def check_password(self, password: str) -> bool:
        return self._password == password

    def __repr__(self) -> str:
        return f"User(username={self.username!r})"


# ── Bank ───────────────────────────────────────────────────────────────────────

class Bank:
    """
    Central bank managing all users and their accounts.
    Provides register, login, and an interactive CLI menu.
    """

    def __init__(self, name: str = "Python National Bank") -> None:
        self.name = name
        self._users: dict[str, User] = {}

    def register(self, username: str, password: str) -> bool:
        """Register a new user. Returns False if the username is taken."""
        if username in self._users:
            print(f"  Username '{username}' is already registered.")
            return False
        if len(password) < 4:
            print("  Password must be at least 4 characters.")
            return False
        self._users[username] = User(username, password)
        print(f"  Account created for '{username}'.")
        return True

    def login(self, username: str, password: str) -> Optional[User]:
        """Authenticate a user. Returns the User object on success."""
        user = self._users.get(username)
        if user and user.check_password(password):
            print(f"  Login successful. Welcome, {username}!")
            return user
        print("  Login failed: invalid username or password.")
        return None

    def run(self) -> None:
        """Interactive command-line banking session."""
        print(f"\n  Welcome to {self.name}")
        print("  " + "=" * 35)

        # Registration
        print("\n  -- Register --")
        username = input("  Choose a username: ").strip()
        password = input("  Choose a password: ").strip()
        if not self.register(username, password):
            return

        # Login
        print("\n  -- Login --")
        uname = input("  Username: ").strip()
        pword = input("  Password: ").strip()
        user = self.login(uname, pword)
        if not user:
            return

        # Banking menu
        account = user.account
        while True:
            print("\n  -- Menu --")
            print("  1. Deposit")
            print("  2. Withdraw")
            print("  3. View statement")
            print("  4. Exit")
            choice = input("  Choice: ").strip()

            if choice == "1":
                try:
                    amount = float(input("  Amount to deposit: £"))
                    account.deposit(amount)
                except ValueError as e:
                    print(f"  Error: {e}")

            elif choice == "2":
                try:
                    amount = float(input("  Amount to withdraw: £"))
                    account.withdraw(amount)
                except ValueError as e:
                    print(f"  Error: {e}")

            elif choice == "3":
                account.statement()

            elif choice == "4":
                print(f"\n  Thank you for banking with {self.name}. Goodbye!")
                break

            else:
                print("  Invalid choice. Please enter 1, 2, 3, or 4.")


# ── Example usage (non-interactive demo) ──────────────────────────────────────

if __name__ == "__main__":
    print("=== Bank Account Demo (non-interactive) ===\n")

    bank = Bank("Python National Bank")
    bank.register("gleb", "pass123")
    bank.register("gleb", "other")     # Duplicate — should fail

    user = bank.login("gleb", "pass123")
    if user:
        acc = user.account
        acc.deposit(1000)
        acc.deposit(500)
        acc.withdraw(200)
        acc.withdraw(150)

        try:
            acc.withdraw(5000)   # Should fail
        except ValueError as e:
            print(f"  Caught: {e}")

        acc.statement()

    print("\n=== Uncommenting the interactive mode ===")
    print("  Call bank.run() for the full interactive CLI experience.")
    # bank.run()
