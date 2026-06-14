"""
OOP Abstraction — Shape Hierarchy
==================================
Demonstrates abstract base classes (ABC) in Python.

An abstract class defines a CONTRACT: it lists methods that every subclass
MUST implement. The abstract class itself cannot be instantiated.

Here, Shape declares area() and perimeter() as abstract.
Circle, Rectangle, and Triangle inherit from Shape and provide their own
correct implementations of those methods.

Concepts covered:
  - Abstract base class (abc.ABC)
  - @abstractmethod decorator
  - Concrete subclasses fulfilling the abstract contract
  - Polymorphism: display(shape) works for any Shape subclass
  - __str__ for human-readable output
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Subclasses MUST implement area() and perimeter().
    Attempting to instantiate Shape directly raises TypeError.
    """

    def __init__(self, colour: str = "white") -> None:
        self.colour = colour

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the shape."""

    def describe(self) -> str:
        """Return a formatted description — available to all subclasses."""
        return (
            f"{self.__class__.__name__} [{self.colour}] | "
            f"Area: {self.area():.4f} | "
            f"Perimeter: {self.perimeter():.4f}"
        )

    def __str__(self) -> str:
        return self.describe()


class Circle(Shape):
    """
    A circle defined by its radius.

    Formulae:
        Area      = π r²
        Perimeter = 2 π r  (circumference)
    """

    def __init__(self, radius: float, colour: str = "white") -> None:
        super().__init__(colour)
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius}, colour={self.colour!r})"


class Rectangle(Shape):
    """
    A rectangle defined by its width and height.

    Formulae:
        Area      = width × height
        Perimeter = 2 × (width + height)
    """

    def __init__(self, width: float, height: float, colour: str = "white") -> None:
        super().__init__(colour)
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return (
            f"Rectangle(width={self.width}, height={self.height}, "
            f"colour={self.colour!r})"
        )


class Triangle(Shape):
    """
    A triangle defined by its three side lengths.

    Formulae:
        Perimeter = a + b + c
        Area      = √(s(s-a)(s-b)(s-c))  [Heron's formula]
                    where s = (a + b + c) / 2  (semi-perimeter)

    Raises:
        ValueError: If the three sides do not form a valid triangle
                    (triangle inequality: each side < sum of the other two).
    """

    def __init__(self, a: float, b: float, c: float, colour: str = "white") -> None:
        super().__init__(colour)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All side lengths must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(
                f"Sides {a}, {b}, {c} do not form a valid triangle."
            )
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = self.perimeter() / 2          # Semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def __str__(self) -> str:
        return (
            f"Triangle(a={self.a}, b={self.b}, c={self.c}, "
            f"colour={self.colour!r})"
        )


# ── Polymorphism: one function, any Shape ─────────────────────────────────────

def display(shape: Shape) -> None:
    """
    Print a shape's full description.
    Works for ANY subclass of Shape — this is polymorphism.
    We do not need to know the concrete type; we only need Shape's interface.
    """
    print(f"  {shape.describe()}")


def total_area(shapes: list[Shape]) -> float:
    """Return the combined area of a list of shapes."""
    return sum(s.area() for s in shapes)


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Creating Shapes ===")
    circle    = Circle(radius=5, colour="red")
    rectangle = Rectangle(width=10, height=4, colour="blue")
    triangle  = Triangle(a=3, b=4, c=5, colour="green")   # Right triangle

    shapes: list[Shape] = [circle, rectangle, triangle]

    print("\n=== Individual Shape Details ===")
    for shape in shapes:
        print(f"\n  {shape}")
        display(shape)

    print("\n=== Polymorphic dispatch ===")
    print("  Calling display() with each shape — same function, different behaviour:")
    for shape in shapes:
        display(shape)

    print(f"\n  Total area of all shapes: {total_area(shapes):.4f}")

    print("\n=== Abstract class cannot be instantiated ===")
    try:
        s = Shape()
    except TypeError as e:
        print(f"  TypeError: {e}")

    print("\n=== Right Triangle (3-4-5) verification ===")
    rt = Triangle(3, 4, 5)
    print(f"  Area:       {rt.area():.4f}  (expected: 6.0000)")
    print(f"  Perimeter:  {rt.perimeter():.4f}  (expected: 12.0000)")

    print("\n=== Circle (r=1) verification ===")
    unit = Circle(1)
    print(f"  Area:      {unit.area():.6f}  (expected: {math.pi:.6f})")
    print(f"  Perimeter: {unit.perimeter():.6f}  (expected: {2*math.pi:.6f})")
