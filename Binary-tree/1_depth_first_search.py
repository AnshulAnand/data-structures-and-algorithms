
# print a array consisting all values(nodes) of a binary tree using DFS

from node_class import Node

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

def depthFirstSearch(root):
    if root == None: return []
    res, stack = [], [root]
    while len(stack) > 0:
        current = stack.pop(-1)
        res.append(current.val)
        if current.right != None: stack.append(current.right)
        if current.left != None: stack.append(current.left)
    return res

print(depthFirstSearch(a)) # prints ['a', 'b', 'd', 'e', 'c', 'f']