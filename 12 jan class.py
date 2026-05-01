# class usses


'''class Characters:
    def __init__(self,strength,magic,dexterity,health_points):
        self.strength = strength
        self.magic = magic
        self.dexterity = dexterity
        self.health_points = health_points
        def show_strength(self):
            print('strength is',self.strength)
        def show_magic(self):
            print('magic is',self.magic)
        def show_dexterity(self):
            print('dexterity is',self.dexterity)
        def show_health_points(self):
            print('health_points is',self.health_points)

class Warrior(Characters):
    def __init__(self,strength,magic,dexterity,health_points,weapon):
        super().__init__(strength,magic,dexterity,health_points)
        self.weapon = weapon


class Mage(Characters):
    def __init__(self,strength,magic,dexterity,health_points,spell_power):
        super().__init__(strength,magic,dexterity,health_points)
        self.spell_power = spell_power

class Rogue(Characters):
    def __init__(self,strength,magic,dexterity,health_points,stealth):
        super().__init__(self,strength,magic,dexterity,health_points)
        self.stealth = stealth

class NoviceWarrior(Warrior):
    def __init__(self,strength,magic,dexterity,health_points,weapon):
        super().__init__(self, strength, magic, dexterity, health_points,weapon)
        self.level = 'novice'
class AdvancedWarrior(Warrior):
    def __init__(self,strength,magic,dexterity,health_points,weapon):
        super().__init__(self, strength, magic, dexterity, health_points, weapon)
        self.level = 'advanced'
class IntermediateWarrior(Warrior):
    def __init__(self,strength,magic,dexterity,health_points,weapon):
        super().__init__(self, strength, magic, dexterity, health_points, weapon)
        self.level = 'intermediate'

'''

'''
import math
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle:
    def __init__(self,radius,colour):
        self.radius = radius
        self.colour = colour
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle with radius {self.radius} and colour {self.colour}'

class Rectangle:
    def __init__(self,width,height,colour):
        self.width = width
        self.height = height
        self.colour = colour

    def area(self):
        return math.pi * self.width * self.height
    def perimeter(self):
        return 2 * math.pi * self.width * self.height
    def __str__(self):
        return f'Rectangle with width {self.width} and height {self.height} with colour {self.colour}'
class Triangle:
    def __init__(self,a,b,c,colour):
        self.a = a
        self.b = b
        self.c = c
        self.colour = colour
    def area(self):
        return self.a * self.b * self.c
    def perimeter(self):
        return self.a + self.b + self.c
    def __str__(self):
        return f'Triangle with {self.a} {self.b} {self.c} {self.colour}'


def display(shape):
    print(shape.area(), shape.perimeter())
r = Rectangle(10,20,30)

'''

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Buyer(User):
    def view_items(self, items):
        print("Available items:")
        for item in items:
            item.display()

    def buy(self, item):
        print(f"{self.name} bought {item.title}")


class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.title} added for sale")


class Admin(User):
    def reject_account(self, name):
        print(f"Rejected account {name}")


class Item:
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price

    def display(self):
        print(f"{self.title}: {self.description} (£{self.price})")



# add Transactions and polymorphism

seller = Seller("Gleb", "gleb@mail.com", "123")
buyer = Buyer("Alex", "alex@mail.com", "456")

item1 = Item("Dog", "Friendly pet", 300)
item2 = Item("Cow", "Farm animal", 500)

seller.add_item(item1)
seller.add_item(item2)

buyer.view_items(seller.items)


