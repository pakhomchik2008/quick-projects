"""
Vehicle Rental System — OOP Mini Project
==========================================
A vehicle rental management system demonstrating inheritance and composition.

Hierarchy:
    Vehicle (base)
        ├── Car         — passenger vehicle
        ├── Truck       — cargo vehicle
        └── Motorcycle  — two-wheel vehicle

Supporting classes:
    Customer        — renter with contact details
    Rental          — links a customer to a vehicle for a date range
    RentalSystem    — manages the fleet and all rentals

Concepts demonstrated:
  - Inheritance: Car/Truck/Motorcycle extend Vehicle
  - Polymorphism: display_info() overridden in each subclass
  - Composition: RentalSystem contains lists of Vehicles, Customers, Rentals
  - Encapsulation: availability managed internally by the Rental record
  - __str__ and __repr__ dunders
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import Optional


# ── Vehicle hierarchy ──────────────────────────────────────────────────────────

class Vehicle:
    """
    Base class for all rental vehicles.
    Tracks availability through the is_available flag.
    """

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        daily_rate: float,
    ) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available: bool = True

    def display_info(self) -> str:
        """Return a human-readable description — overridden by subclasses."""
        return (
            f"{self.year} {self.make} {self.model} "
            f"— £{self.daily_rate:.2f}/day "
            f"({'Available' if self.is_available else 'Rented'})"
        )

    def __str__(self) -> str:
        return self.display_info()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"make={self.make!r}, model={self.model!r}, year={self.year})"
        )


class Car(Vehicle):
    """A passenger car for personal or family use."""

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        daily_rate: float,
        num_doors: int,
        num_seats: int,
        fuel_type: str,
    ) -> None:
        super().__init__(make, model, year, daily_rate)
        self.num_doors = num_doors
        self.num_seats = num_seats
        self.fuel_type = fuel_type

    def display_info(self) -> str:
        base = super().display_info()
        return f"{base} | {self.num_doors}-door, {self.num_seats} seats, {self.fuel_type}"


class Truck(Vehicle):
    """A commercial truck for heavy goods transport."""

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        daily_rate: float,
        cargo_capacity: str,
        drive_type: str,
    ) -> None:
        super().__init__(make, model, year, daily_rate)
        self.cargo_capacity = cargo_capacity
        self.drive_type = drive_type

    def display_info(self) -> str:
        base = super().display_info()
        return f"{base} | Cargo: {self.cargo_capacity}, {self.drive_type}"


class Motorcycle(Vehicle):
    """A two-wheel motorcycle for single riders."""

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        daily_rate: float,
        engine_cc: int,
        num_cylinders: int,
    ) -> None:
        super().__init__(make, model, year, daily_rate)
        self.engine_cc = engine_cc
        self.num_cylinders = num_cylinders

    def display_info(self) -> str:
        base = super().display_info()
        return f"{base} | {self.engine_cc}cc, {self.num_cylinders}-cylinder"


# ── Customer ───────────────────────────────────────────────────────────────────

@dataclass
class Customer:
    """Represents a person renting a vehicle."""
    name: str
    age: int
    address: str
    phone: str

    def __str__(self) -> str:
        return f"Customer(name={self.name!r}, phone={self.phone!r})"


# ── Rental record ──────────────────────────────────────────────────────────────

@dataclass
class Rental:
    """Links a customer to a vehicle for a specific date range."""
    customer: Customer
    vehicle: Vehicle
    start_date: date
    end_date: date

    @property
    def duration_days(self) -> int:
        """Number of rental days."""
        return (self.end_date - self.start_date).days

    @property
    def total_cost(self) -> float:
        """Total rental cost."""
        return self.duration_days * self.vehicle.daily_rate

    def __str__(self) -> str:
        return (
            f"Rental({self.customer.name} | "
            f"{self.vehicle.make} {self.vehicle.model} | "
            f"{self.start_date} to {self.end_date} | "
            f"£{self.total_cost:.2f})"
        )


# ── Rental system ──────────────────────────────────────────────────────────────

class RentalSystem:
    """
    Central system managing the vehicle fleet and all active rentals.
    """

    def __init__(self, company_name: str = "Python Rentals") -> None:
        self.company_name = company_name
        self._fleet: list[Vehicle] = []
        self._rentals: list[Rental] = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the fleet."""
        self._fleet.append(vehicle)
        print(f"  Added to fleet: {vehicle}")

    def available_vehicles(self) -> list[Vehicle]:
        """Return all vehicles currently available for rental."""
        return [v for v in self._fleet if v.is_available]

    def rent_vehicle(
        self,
        vehicle: Vehicle,
        customer: Customer,
        start: date,
        end: date,
    ) -> Optional[Rental]:
        """
        Rent a vehicle to a customer for the given period.
        Returns the Rental record, or None if the vehicle is unavailable.
        """
        if not vehicle.is_available:
            print(f"  '{vehicle.make} {vehicle.model}' is already rented.")
            return None
        if end <= start:
            print("  End date must be after start date.")
            return None

        vehicle.is_available = False
        rental = Rental(customer, vehicle, start, end)
        self._rentals.append(rental)
        print(
            f"  Rented: {vehicle.make} {vehicle.model} to {customer.name} "
            f"({rental.duration_days} days, £{rental.total_cost:.2f})"
        )
        return rental

    def return_vehicle(self, rental: Rental) -> None:
        """Mark a vehicle as returned and available again."""
        rental.vehicle.is_available = True
        print(f"  Returned: {rental.vehicle.make} {rental.vehicle.model} from {rental.customer.name}")

    def display_fleet(self) -> None:
        """Print all vehicles in the fleet."""
        print(f"\n  {self.company_name} — Fleet ({len(self._fleet)} vehicles):")
        for vehicle in self._fleet:
            print(f"    {vehicle.display_info()}")

    def rental_report(self) -> None:
        """Print a summary of all rentals."""
        print(f"\n  {self.company_name} — Rental Report ({len(self._rentals)} rentals):")
        total_revenue = 0.0
        for rental in self._rentals:
            print(f"    {rental}")
            total_revenue += rental.total_cost
        print(f"\n  Total revenue: £{total_revenue:.2f}")


# ── Example usage ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    system = RentalSystem("Python Rentals Ltd")

    print("=== Adding Vehicles to Fleet ===\n")
    car   = Car("Toyota",   "Corolla", 2022, 45.00, num_doors=4, num_seats=5, fuel_type="Petrol")
    truck = Truck("Ford",   "Ranger",  2021, 70.00, cargo_capacity="1,000 kg", drive_type="4WD")
    bike  = Motorcycle("Yamaha", "R6", 2020, 60.00, engine_cc=600, num_cylinders=4)

    system.add_vehicle(car)
    system.add_vehicle(truck)
    system.add_vehicle(bike)

    system.display_fleet()

    print("\n=== Registering Customers ===\n")
    customer1 = Customer("John Smith", 32, "12 Brooklyn Ave, London", "07780685237")
    customer2 = Customer("Emma Jones", 28, "5 Oxford Street, London", "07712345678")
    print(f"  {customer1}")
    print(f"  {customer2}")

    print("\n=== Renting Vehicles ===\n")
    rental1 = system.rent_vehicle(
        car, customer1,
        start=date(2026, 1, 10),
        end=date(2026, 1, 15),
    )
    rental2 = system.rent_vehicle(
        bike, customer2,
        start=date(2026, 1, 12),
        end=date(2026, 1, 14),
    )

    # Try to rent the same car again
    system.rent_vehicle(car, customer2, date(2026, 1, 11), date(2026, 1, 13))

    print("\n=== Available Vehicles ===\n")
    available = system.available_vehicles()
    if available:
        for v in available:
            print(f"  {v.display_info()}")
    else:
        print("  No vehicles available.")

    print("\n=== Returning a Vehicle ===\n")
    if rental1:
        system.return_vehicle(rental1)

    print("\n=== Rental Report ===")
    system.rental_report()

    print("\n=== Polymorphism: display_info() on any Vehicle ===\n")
    fleet: list[Vehicle] = [car, truck, bike]
    for vehicle in fleet:
        print(f"  {vehicle.display_info()}")
