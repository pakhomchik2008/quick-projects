"""
OOP Polymorphism — Marketplace
================================
Demonstrates polymorphism: multiple classes share a common interface
(the User base class), and the same method calls produce different behaviour
depending on the actual object type.

Hierarchy:
    User (base)
        ├── Buyer   — can browse and purchase items
        ├── Seller  — can list items for sale
        └── Admin   — can manage accounts and view all activity

Concepts covered:
  - Polymorphism: describe() works on any User subclass
  - Method overriding: each User subclass overrides describe()
  - Encapsulation: Item manages its own state
  - Composition: Seller owns a list of Items
  - isinstance() check for role-based access control
"""

from __future__ import annotations
from typing import Optional


class Item:
    """
    Represents a product listed for sale in the marketplace.
    """

    def __init__(self, title: str, description: str, price: float) -> None:
        self.title = title
        self.description = description
        self.price = price
        self.sold = False

    def mark_as_sold(self) -> None:
        self.sold = True

    def display(self) -> None:
        status = "SOLD" if self.sold else f"£{self.price:.2f}"
        print(f"  [{status}] {self.title} — {self.description}")

    def __str__(self) -> str:
        return f"Item(title={self.title!r}, price=£{self.price:.2f})"

    def __repr__(self) -> str:
        return self.__str__()


class User:
    """
    Base class for all marketplace participants.
    Defines the shared interface that every user type must support.
    """

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self._password = password

    def describe(self) -> str:
        """
        Return a description of this user's role.
        Overridden by each subclass — this is POLYMORPHISM.
        """
        return f"User: {self.name} ({self.email})"

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, email={self.email!r})"


class Buyer(User):
    """
    A marketplace buyer who can browse and purchase items.
    """

    def __init__(self, name: str, email: str, password: str) -> None:
        super().__init__(name, email, password)
        self.purchase_history: list[Item] = []

    def describe(self) -> str:
        return (
            f"Buyer: {self.name} | "
            f"Purchases: {len(self.purchase_history)}"
        )

    def browse(self, items: list[Item]) -> None:
        """Display all available (unsold) items."""
        available = [item for item in items if not item.sold]
        if not available:
            print(f"  {self.name}: No items currently available.")
            return
        print(f"  {self.name} is browsing {len(available)} item(s):")
        for item in available:
            item.display()

    def purchase(self, item: Item) -> bool:
        """
        Attempt to purchase an item.
        Returns True on success, False if the item is already sold.
        """
        if item.sold:
            print(f"  {self.name}: '{item.title}' is already sold.")
            return False
        item.mark_as_sold()
        self.purchase_history.append(item)
        print(f"  {self.name} purchased '{item.title}' for £{item.price:.2f}.")
        return True


class Seller(User):
    """
    A marketplace seller who can list items for sale.
    """

    def __init__(self, name: str, email: str, password: str) -> None:
        super().__init__(name, email, password)
        self.listings: list[Item] = []

    def describe(self) -> str:
        active = sum(1 for item in self.listings if not item.sold)
        return (
            f"Seller: {self.name} | "
            f"Active listings: {active} / {len(self.listings)}"
        )

    def list_item(self, item: Item) -> None:
        """Add an item to this seller's listings."""
        self.listings.append(item)
        print(f"  {self.name} listed '{item.title}' for £{item.price:.2f}.")

    def show_listings(self) -> None:
        """Display all items this seller has listed."""
        print(f"  {self.name}'s listings:")
        if not self.listings:
            print("    (none)")
        for item in self.listings:
            item.display()

    def revenue(self) -> float:
        """Return total revenue from sold items."""
        return sum(item.price for item in self.listings if item.sold)


class Admin(User):
    """
    A marketplace administrator with elevated permissions.
    Can view all users and manage the platform.
    """

    def describe(self) -> str:
        return f"Admin: {self.name} [ELEVATED PERMISSIONS]"

    def reject_account(self, user: User) -> None:
        print(f"  Admin {self.name} rejected account: {user.name} ({user.email})")

    def view_all_users(self, users: list[User]) -> None:
        """Display a summary of all registered users — admin only."""
        print(f"  Admin {self.name} — All registered users ({len(users)}):")
        for user in users:
            print(f"    {user.describe()}")   # Polymorphic call


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Create participants
    seller = Seller("Gleb",  "gleb@mail.com",  "pass123")
    buyer  = Buyer("Alex",   "alex@mail.com",  "pass456")
    admin  = Admin("Victor", "admin@mail.com", "admin999")

    # Create items
    item1 = Item("Dog",     "Friendly pet, great with children", 300.00)
    item2 = Item("Cow",     "Farm animal, produces milk",        500.00)
    item3 = Item("Bicycle", "Barely used, 21 gears",             150.00)

    print("=== Seller Lists Items ===")
    seller.list_item(item1)
    seller.list_item(item2)
    seller.list_item(item3)

    print("\n=== Buyer Browses ===")
    buyer.browse(seller.listings)

    print("\n=== Buyer Purchases ===")
    buyer.purchase(item1)
    buyer.purchase(item1)   # Try to buy again — already sold

    print("\n=== Seller Stats ===")
    seller.show_listings()
    print(f"  Revenue so far: £{seller.revenue():.2f}")

    print("\n=== Polymorphism: describe() on any User ===")
    all_users: list[User] = [seller, buyer, admin]
    for user in all_users:
        # Same method call — different output based on the actual type
        print(f"  {user.describe()}")

    print("\n=== Admin Actions ===")
    admin.view_all_users(all_users)
    admin.reject_account(buyer)

    print("\n=== Type checking with isinstance() ===")
    for user in all_users:
        if isinstance(user, Admin):
            print(f"  {user.name} has admin access.")
        elif isinstance(user, Seller):
            print(f"  {user.name} is a seller with {len(user.listings)} listing(s).")
        elif isinstance(user, Buyer):
            print(f"  {user.name} has made {len(user.purchase_history)} purchase(s).")
