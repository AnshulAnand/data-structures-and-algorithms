import math

# return the minimum value/node in a binary tree

from node_class import Node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

def treeMinDFS(root):
    stack, minValue = [root], math.inf
    while len(stack) > 0:
        current = stack.pop(-1)
        if current.val < minValue: minValue = current.val
        if current.left != None: stack.append(current.left)
        if current.right != None: stack.append(current.right)
    return minValue

print(treeMinDFS(a)) # prints 1

# using recursion
def treeMinRecursive(root):
    if root == None: return math.inf
    leftMin = treeMinRecursive(root.left)
    rightMin = treeMinRecursive(root.right)
    return min(root.val, leftMin, rightMin)

print(treeMinRecursive(a)) # prints 1