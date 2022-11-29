
# check whether tree includes target or not

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

# using BFS
def treeIncludesBFS(root, target):
	if root == None: return False
	queue = [root]
	while len(queue) > 0:
		current = queue.pop(0)
		if current.val == target: return True
		if current.left != None: queue.append(current.left)
		if current.right != None: queue.append(current.right)
	return False

print(treeIncludesBFS(a, 'e')) # prints True

# using DFS (recursive)
def treeIncludesDFS(root, target):
	if root == None: return False
	if root.val == target: return True
	return treeIncludesDFS(root.left, target) or treeIncludesDFS(root.right, target)

print(treeIncludesDFS(a, 'e')) # prints True