
# return the sum of all nodes in a binary tree

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

def treeSum(root):
    if root == None: return 0
    return root.val + treeSum(root.left) + treeSum(root.right)

print(treeSum(a)) # prints 21

# using BFS
def treeSumBFS(root):
    if root == None: return 0
    Sum, queue = 0, [root]
    while len(queue) > 0:
        current = queue.pop(0)
        Sum += current.val
        if current.left != None: queue.append(current.left)
        if current.right != None: queue.append(current.right)
    return Sum

print(treeSumBFS(a)) # prints 21