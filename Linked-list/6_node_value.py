
# print the node's value at given index, if not found print None

from linked_list import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def linkedListIndex(head, index):
	current = head
	count = 0
	while current != None:
		if count == index: return current.val
		index -= 1
		current = current.next
	return None

print(linkedListIndex(a, 2)) # prints C

# recursive approach

def linkedListIndexRecursively(head, index):
	if head == None: return None
	if index == 0: return head.val
	return linkedListIndexRecursively(head.next, index - 1)

print(linkedListIndexRecursively(a, 2)) # prints C