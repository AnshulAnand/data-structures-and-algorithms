
# linked list traversal

from linked_list import Node

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

printLinkedList(a) # prints A B C D


# above function recursively

def printLinkedListRecursively(head):
	if head == None: return
	print(head.val)
	printLinkedListRecursively(head.next)

printLinkedListRecursively(a) # prints A B C D
