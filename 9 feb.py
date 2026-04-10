#1
'''from os.path import split


class Node:
    def __init__(self, data = None):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node(84)
n2 = Node(41)
n3 = Node(96)
n4 = Node(24)
n5 = Node(50)
n6 = Node(98)
n7 = Node(13)
n8 = Node(37)

n1.left_child = n2
n1.right_child = n3

n2.left_child = n4
n2.right_child = n5

n3.right_child = n6

n4.left_child = n7
n4.right_child = n8

def in_order(node):
    if node is None:
        return
    in_order(node.left_child)
    print(node.data)

def pre_order(node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left_child)
    pre_order(node.right_child)

def post_order(node):
    if node is None:
        return
    post_order(node.left_child)
    post_order(node.right_child)
    print(node.data)

current = n1


print('In order:')
print(in_order(current))
print('Pre-order:')
print(pre_order(current))
print('Post-order:')
print(post_order(current))

print('check')
while current:
    print(current.data)
    current = current.left_child'''
from os.path import split

#2
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


n1 = Node(4)
n2 = Node(1)
n3 = Node(7)
n4 = Node(6)
n5 = Node(8)
n6 = Node(3)
n7 = Node(9)

n1.left_child = n2
n1.right_child = n3

n3.left_child = n4
n3.right_child = n5

n4.left_child = n6

n5.right_child = n7
print('This prints the nodes using inorder traversal')
inorder(n1)
print('This prints the nodes using preorder traversal')
preorder(n1)
print('This prints the nodes using postorder traversal')
postorder(n1)
'''

#3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


n1 = Node(4)
n2 = Node(1)
n3 = Node(7)
n4 = Node(6)
n5 = Node(8)
n6 = Node(9)
n1.left_child = n2
n1.right_child = n3


n2.left_child = n4
n2.right_child = n5
n6.left_child = n6
print('This prints the nodes using inorder traversal')
inorder(n1)
print('This prints the nodes using preorder traversal')
preorder(n1)
print('This prints the nodes using postorder traversal')
postorder(n1)
'''

'''
#4

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


# -------- STEP 1: get all values --------
user_input = list(map(int, input("Enter integers: ").split()))

# -------- STEP 2: create nodes automatically --------
nodes = map(Node, user_input)

root = nodes[0] # first value = root


# -------- STEP 3: define children --------
for value in user_input:
    current = nodes[value]

    print(f"\nDefine the left and right children of {value}")

    left = input("User(left): ")
    right = input("User(right): ")

    # assign left child
    if left != "None":
        current.left_child = nodes[int(left)]

    # assign right child
    if right != "None":
        current.right_child = nodes[int(right)]



# -------- DFS traversals --------
def inorder(node):
    if node:
        inorder(node.left_child)
        print(node.data, end=" ")
        inorder(node.right_child)


def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left_child)
        preorder(node.right_child)


def postorder(node):
    if node:
        postorder(node.left_child)
        postorder(node.right_child)
        print(node.data, end=" ")


print("\n\nInorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)


'''

#1 worksheet 2
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.right_child = n2
n2.left_child = n3


print('This prints the nodes using inorder traversal')
inorder(n1)
print('This prints the nodes using preorder traversal')
preorder(n1)
print('This prints the nodes using postorder traversal')
postorder(n1)
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# ---------- Traversal ----------
def inorder(node):
    if node is None:
        return []
    return inorder(node.left_child) + [node.data] + inorder(node.right_child)


# ---------- Invert ----------
def invert(node):
    if node is None:
        return None

    node.left_child, node.right_child = node.right_child, node.left_child

    invert(node.left_child)
    invert(node.right_child)

    return node


# ---------- Build tree ----------
n1 = Node(4)
n2 = Node(2)
n3 = Node(7)
n4 = Node(1)
n5 = Node(3)
n6 = Node(6)
n7 = Node(9)

n1.left_child = n2
n1.right_child = n3

n2.left_child = n4
n2.right_child = n5

n3.left_child = n6
n3.right_child = n7


# ---------- Run ----------
print("Before invert:", inorder(n1))

invert(n1)

print("After invert:", inorder(n1))

print("Before invert:", inorder(n2))

invert(n2)

print("After invert:", inorder(n2))
'''
#3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


def convert(node):
    current = n1
    if node is None:
        return None
    node.left_child = None


    return current


n1 = Node(1)
n2 = Node(2)
n7 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(4)
n6 = Node(3)


n1.left_child = n2
n1.right_child = n7

n2.left_child = n3
n2.right_child = n4

n3.left_child = n5
n3.right_child = n6


convert(n1)

print("After invert:", inorder(n1))
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)

def sum_of_left_leaves(node):
    if node is None:
        return 0

    total = 0

    if node.left_child:
        # check if left child is leaf
        if node.left_child.left_child is None and node.left_child.right_child is None:
            total += node.left_child.data
        else:
            total += sum_of_left_leaves(node.left_child)

    total += sum_of_left_leaves(node.right_child)

    return total
n1 = Node(3)
n2 = Node(9)
n7 = Node(20)
n3 = Node(15)
n4 = Node(7)

n1.left_child = n2
n1.right_child = n7

n2.left_child = n3
n2.right_child = n4

print(sum_of_left_leaves(n1))
'''
