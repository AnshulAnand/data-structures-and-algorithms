
# print an array which consists all values(nodes) of a binary tree

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

def breadthFirstSearch(root):
    if root == None: return []
    res, queue = [], [root]
    while len(queue) > 0:
        current = queue.pop(0)
        res.append(current.val)
        if current.left != None: queue.append(current.left)
        if current.right != None: queue.append(current.right)
    return res

print(breadthFirstSearch(a)) # ['a', 'b', 'c', 'd', 'e', 'f']