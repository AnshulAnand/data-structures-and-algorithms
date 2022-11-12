
# check whether linked list contains "target" or not
# if it does then print True else print False

from linked_list import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def linkedListFind(head, target):
	current = head
	while current != None:
		if current.val == target: return True
		current = current.next
	return False

print(linkedListFind(a, 'C')) # prints True

# recursive approach

def linkedListFindRecursively(head, target):
	if head == None: return False
	if head.val == target: return True
	return linkedListFindRecursively(head.next, target)

print(linkedListFindRecursively(a, 'C')) # prints True
