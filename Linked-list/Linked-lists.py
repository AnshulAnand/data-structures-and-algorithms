class Node():
	def __init__(self, val):
		self.val = val
		self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def printLinkedList(head):
	current = head
	while current != None:
		print(current.val)
		current = current.next

printLinkedList(a)


# above function recursively
"""
def printLinkedList(head):
	if head == None: return
	print(head.val)
	printLinkedList(head.next)

printLinkedList(a)
"""