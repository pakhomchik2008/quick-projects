"""
OOP Inheritance — RPG Character Hierarchy
=========================================
Demonstrates multi-level inheritance: building specialised classes
from general ones using Python's super() mechanism.

Hierarchy:
    Character (base)
        ├── Warrior
        │     ├── NoviceWarrior
        │     ├── IntermediateWarrior
        │     └── AdvancedWarrior
        ├── Mage
        └── Rogue

Concepts covered:
  - Single inheritance (Warrior extends Character)
  - Multi-level inheritance (NoviceWarrior extends Warrior extends Character)
  - super().__init__() to call the parent constructor
  - Method overriding (each class overrides attack())
  - __str__ for readable output
"""


class Character:
    """
    Base class for all RPG characters.
    Holds core stats shared by every character type.
    """

    def __init__(
        self,
        name: str,
        strength: int,
        magic: int,
        dexterity: int,
        health_points: int,
    ) -> None:
        self.name = name
        self.strength = strength
        self.magic = magic
        self.dexterity = dexterity
        self.health_points = health_points

    def show_stats(self) -> None:
        """Print all core stats."""
        print(f"  Name:    {self.name}")
        print(f"  STR: {self.strength}  MAG: {self.magic}  "
              f"DEX: {self.dexterity}  HP: {self.health_points}")

    def attack(self) -> str:
        """Generic attack — overridden by subclasses."""
        return f"{self.name} attacks!"

    def is_alive(self) -> bool:
        """Return True if the character still has health points."""
        return self.health_points > 0

    def take_damage(self, damage: int) -> None:
        """Reduce health by the given damage amount (minimum 0)."""
        self.health_points = max(0, self.health_points - damage)
        print(f"  {self.name} took {damage} damage. HP: {self.health_points}")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name!r}, "
            f"HP={self.health_points})"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Warrior(Character):
    """
    Melee fighter specialisation.
    Inherits all Character stats and adds a weapon.
    """

    def __init__(
        self,
        name: str,
        strength: int,
        magic: int,
        dexterity: int,
        health_points: int,
        weapon: str,
    ) -> None:
        super().__init__(name, strength, magic, dexterity, health_points)
        self.weapon = weapon

    def attack(self) -> str:
        """Warriors deal physical damage based on strength."""
        damage = self.strength * 2
        return f"{self.name} strikes with a {self.weapon} for {damage} damage!"

    def __str__(self) -> str:
        return f"Warrior(name={self.name!r}, weapon={self.weapon!r}, HP={self.health_points})"


class Mage(Character):
    """
    Magic-based specialisation.
    Spell power amplifies magic attacks.
    """

    def __init__(
        self,
        name: str,
        strength: int,
        magic: int,
        dexterity: int,
        health_points: int,
        spell_power: int,
    ) -> None:
        super().__init__(name, strength, magic, dexterity, health_points)
        self.spell_power = spell_power

    def attack(self) -> str:
        """Mages cast spells for magic-based damage."""
        damage = self.magic + self.spell_power
        return f"{self.name} casts a spell for {damage} magic damage!"

    def __str__(self) -> str:
        return (
            f"Mage(name={self.name!r}, spell_power={self.spell_power}, "
            f"HP={self.health_points})"
        )


class Rogue(Character):
    """
    Stealth-based specialisation.
    High dexterity enables critical strikes.
    """

    def __init__(
        self,
        name: str,
        strength: int,
        magic: int,
        dexterity: int,
        health_points: int,
        stealth: int,
    ) -> None:
        super().__init__(name, strength, magic, dexterity, health_points)
        self.stealth = stealth

    def attack(self) -> str:
        """Rogues deal dexterity-based backstab damage."""
        damage = self.dexterity + self.stealth
        return f"{self.name} backstabs for {damage} damage from the shadows!"

    def __str__(self) -> str:
        return (
            f"Rogue(name={self.name!r}, stealth={self.stealth}, "
            f"HP={self.health_points})"
        )


# ── Multi-level inheritance: Warrior tiers ─────────────────────────────────────

class NoviceWarrior(Warrior):
    """Entry-level warrior. Reduced attack multiplier."""

    LEVEL = "novice"

    def __init__(self, name: str, weapon: str) -> None:
        # Novices have lower stats
        super().__init__(name, strength=5, magic=1, dexterity=4,
                         health_points=80, weapon=weapon)

    def attack(self) -> str:
        damage = self.strength   # No multiplier yet
        return f"[Novice] {self.name} swings a {self.weapon} for {damage} damage."


class IntermediateWarrior(Warrior):
    """Mid-tier warrior. Standard attack multiplier."""

    LEVEL = "intermediate"

    def __init__(self, name: str, weapon: str) -> None:
        super().__init__(name, strength=12, magic=2, dexterity=8,
                         health_points=120, weapon=weapon)

    def attack(self) -> str:
        damage = self.strength * 2
        return f"[Intermediate] {self.name} strikes with {self.weapon} for {damage} damage."


class AdvancedWarrior(Warrior):
    """Elite warrior. High stats and enhanced attack."""

    LEVEL = "advanced"

    def __init__(self, name: str, weapon: str) -> None:
        super().__init__(name, strength=20, magic=5, dexterity=15,
                         health_points=200, weapon=weapon)

    def attack(self) -> str:
        damage = self.strength * 3 + self.dexterity
        return f"[Advanced] {self.name} unleashes a POWER STRIKE with {self.weapon} for {damage} damage!"


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Creating Characters ===")
    warrior = Warrior("Thor", strength=18, magic=2, dexterity=10,
                      health_points=150, weapon="Mjolnir")
    mage = Mage("Gandalf", strength=5, magic=20, dexterity=8,
                health_points=100, spell_power=25)
    rogue = Rogue("Shadow", strength=10, magic=4, dexterity=18,
                  health_points=90, stealth=15)

    for character in [warrior, mage, rogue]:
        print(f"\n  {character}")
        character.show_stats()
        print(f"  {character.attack()}")

    print("\n=== Warrior Progression (multi-level inheritance) ===")
    novice = NoviceWarrior("Bob", weapon="Wooden Sword")
    mid    = IntermediateWarrior("Alice", weapon="Iron Blade")
    elite  = AdvancedWarrior("Leonidas", weapon="Spartan Spear")

    for w in [novice, mid, elite]:
        print(f"\n  Level: {w.LEVEL}")
        print(f"  {w}")
        print(f"  {w.attack()}")

    print("\n=== Combat Demo ===")
    print(f"\n  {warrior} vs {mage}")
    print(f"  {warrior.attack()}")
    warrior.take_damage(30)
    print(f"  {mage.attack()}")
    mage.take_damage(50)
    print(f"  {warrior.name} alive: {warrior.is_alive()}")
    print(f"  {mage.name} alive: {mage.is_alive()}")

    print("\n=== isinstance() and Polymorphism ===")
    party = [warrior, mage, rogue, novice]
    print("  All characters attacking:")
    for member in party:
        print(f"  {member.attack()}")      # Each calls its OWN attack() — polymorphism
