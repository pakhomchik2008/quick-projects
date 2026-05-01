'''from math import factorial


def fuctorial(k):
    if k > 1:
        return k * factorial(k-1)
    else:
        return 1
print(fuctorial(-7))'''

'''def fibonacci(n):
    if n > 1:
        value = fibonacci(n-1)+fibonacci(n-2)

    else:
        value = 1
    return value

print(fibonacci(3))'''

'''class lion:
    feet = 'paws'
    teeth ='sharp'
suzie = lion()
print(suzie.feet)'''

'''class lion:
    name = 'lion'
    feet = 'paws'
    teeth ='sharp'
suzie = lion()
print(suzie.name)'''

'''
class lion:
    name = 'lion'
    feet = 'paws'
    def roar(self):
        print('roarrrrrr')
suzie = lion()
print(lion.roar)
print(suzie.roar)
suzie.roar()
'''

'''
class lion:
    def __init__(self, name, feet, teeth):
        self.name = name
        self.feet = feet
        self.teeth = teeth
suzie = lion('lion', 'paws', 'sharps')
print(suzie.name)
print(suzie.feet)
print(suzie.teeth)'''

'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def __str__(self):
        return f'{self.name} ({self.age})'
p1= person('John', 18)
print(p1.name)
print(p1.age)
print(p1)'''

'''
class lion:
    'this is a lion class'
    name = 'lion'
suzie = lion()
print(suzie.__doc__)'''

def welcome_message(course):
    print('Welcome to our ',course, 'cource')
import welcome
welcome.welcome_message('CS')

