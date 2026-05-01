'''from symtable import Class
class Dog:
    species = 'canis familarities'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

class JackRussel(Dog):
    pass
class dachsund(Dog):
    pass
class Buldog(Dog):
    pass

miles = JackRussel('Miles',4)
buddy = dachsund('Buddy',9)
print(miles)'''
'''
class Vehicle:
    def __init__(self,manufacturer,model,year,daily_rental_rate):
        self.make = manufacturer
        self.model = model
        self.year = year
        self.daily_rental_rate = daily_rental_rate
        self.is_available = True

    def display_info(self):
        print(f'{self.make} {self.model} is {self.year} years old and costs {self.daily_rental_rate} pounds' )

class Car(Vehicle):
    def __init__(self,manufacturer,model,year,daily_rental_rate,number_doors,number_seats,fuel_type):
        super().__init__(manufacturer,model,year,daily_rental_rate)
        self.number_doors = number_doors
        self.number_seats = number_seats
        self.fuel_type = fuel_type


class Track(Vehicle):
    def __init__(self,manufacturer,model,year,daily_rental_rate,cargo_capacity,drive_type):
        super().__init__(manufacturer,model,year,daily_rental_rate)
        self.cargo_capacity = cargo_capacity
        self.drive_type = drive_type
class Motorcycle(Vehicle):
    def __init__(self,manufacturer,model,year,daily_rental_rate,engine_displacement,nuber_cylinders):
        super().__init__(manufacturer,model,year,daily_rental_rate)
        self.engine_displacement = engine_displacement
        self.nuber_cylinders = nuber_cylinders
class Rental:
    def __init__(self,name,rental_start,rental_end):
        self.name = name
        self.rental_start = rental_start
        self.rental_end = rental_end

class Customer(Rental):
    def __init__(self,name,age,rental_start,rental_end,adress,phone_number):
        super().__init__(Vehicle,rental_start,rental_end)
        self.adress = adress
        self.phone_number = phone_number


class Rental_system:
    def __init__(self):
        self.vehicles = []
        self.rentals = []

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
    def display_rentals(self):
        for rental in self.rentals:
            if rental.is_available:
                rental.display_info()

    def rent_vehicle(self,customer):
        for rental in self.rentals:
            if rental.is_available:
                customer.vehicles.is_available = False
                self.rentals.append(rental)
                print('rented successfully by', {customer.customer_name})
        else:
            print('Vehicle not available')

    def rental_report(self):
        for rental in self.rentals:
            print(f' Customer named {rental.name} ordered - {rental.model}, from {rental.start_date} to {rental.end_date} for {rental.cost} pounds')

            
        
system = Rental_system()

car = Car("Toyota", "Corolla", 2022, 45, 4, 5, "Petrol")
truck = Track("Ford", "Ranger", 2021, 70, "1000kg", "4WD")
bike = Motorcycle("Yamaha", "R6", 2020, 60, 600, 4)

system.add_vehicle(car)
system.add_vehicle(truck)
system.add_vehicle(bike)

system.display_rentals()

customer1 = Customer(
    "John Smith",
    "32",
    "date (2026,1,10)",
    '(2026,1,15)',
    'Brooklyn Nets 12',
    '07780685237',

)

system.rent_vehicle(customer1)
system.rental_report()

system.display_rentals()





'''

