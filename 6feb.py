'''Write a Python program for the user to input a sequence of integer numbers. The user
must input multiple integers at once, and the map() function will convert all values to
an integer through a lambda function. Subsequently, sort the list using sort() or
sorted(). Finally, create a function using the BISEC module to identify the left and right
positions to insert a new value in the list whilst maintaining its sorted order. The user
also provides the new value, and the try and except error handling must be used to
guarantee that the input is an integer.
Example:
Input list from the user: 2 3 1 4 5 4 6 4 4 8
Expected Sorted Output list: [1, 2, 3, 4, 4, 4, 4, 5, 6, 8]
Input value to add to the list defined by the user: 4
Location to the left: 3, to the right: 7.'''

import bisect

'''a = [2,3,1,4,5,4,6,4,4,8] # list of integers in ascending order
x = 4 # number to insert
i = bisect.bisect_left(a, x) # call method
a.insert(i, x)
y = int(len(a)) - i
print('This means', i-0, 'times to the left and ' ,y-1, 'times to the right')
z = sorted(a)
print(z)'''
'''
import bisect

# Input list (space-separated integers)
a = list(map(int, input("Enter values: ").split()))

# Input value to insert
x = int(input("Enter value: "))

# Find insertion index
i = bisect.bisect_left(a, x)

# Insert value
a.insert(i, x)

# Count left and right positions
y = len(a) - i

print("This means", i, "times to the left and", y - 1, "times to the right")

# Sorted list
z = sorted(a)
print(z)
'''




# 2. Write an algorithm that will move the top value from one stack to the top of another.
'''
class Stack:
    def __init__(self):
        self.items = []   # better to start empty

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

def move_top(stackA, stackB):
    if not stackA.empty():
        value = stackA.pop()
        stackB.push(value)
    else:
        print("Stack A is empty")
A = Stack()
B = Stack()

A.items = [1,2,3,4,5]

move_top(A, B)

print(A.items)
print(B.items)
'''

#3 Given a stack S containing integers, write an algorithm that will reverse the order of
# the values in the stack.
'''
class Stack:
    def __init__(self):
        self.items = []   # better to start empty

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

def reverse_numbers(stack):
    temp = Stack()
    while not stack.empty():
        temp.push(stack.pop())

    stack.items = temp.items.copy()

A=Stack()

A.items = [1,2,3,4,5]
reverse_numbers(A)
print(A.items)
'''



