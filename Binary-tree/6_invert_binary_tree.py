
# Given the root of a binary tree, invert the tree

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

def invertTreeBFS(root):
    if root == None: return None
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        current.left = current.right
        current.right = current.left
        if current.left != None: queue.append(current.left)
        if current.right != None: queue.append(current.right)
        return root

print(invertTreeBFS(a))

def invertTreeRecursive(root):
    if root == None: return None
    right = invertTreeRecursive(root.right)
    left = invertTreeRecursive(root.left)
    root.left = right
    root.right = left
    return root

print(invertTreeBFS(a))