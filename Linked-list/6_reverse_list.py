
# reverse the order of the nodes in the linked list and
# return the head of the reversed list

from linked_list import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def reverseLinkedList(head):
	previous_node = None
	current = head
	while current != None:
		next_node = current.next
		current.next = previous_node
		previous_node = current
		current = next_node
	return previous_node.val

print(reverseLinkedList(a))
"""
above function reverses the list
A -> B -> C -> D    to    D -> C -> B -> A
and prints new head D
"""

# recursive approach 

def reverseLinkedListRecursively(head, previous_node):
	if head == None: return previous_node
	next_node = head.next
	head.next = previous_node
	return reverseLinkedListRecursively(next_node, head)

print(reverseLinkedListRecursively(a, None).val)
"""
above function will print A not D because "reverseLinkedList" function
reverses the list, if we comment first function out then second function
will also return D
"""