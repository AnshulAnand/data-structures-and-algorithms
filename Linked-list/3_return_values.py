
# return values of linked list as an array

from linked_list import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def linkedListValues(head):
	values = []
	current = head
	while current != None:
		values.append(current.val)
		current = current.next
	return values

print(linkedListValues(a)) # prints ['A', 'B', 'C', 'D']

# recursive approach 

def linkedListValuesRecursively(head):
	values = []
	fillValues(head, values)
	return values

def fillValues(head, values):
	if head == None: return
	values.append(head.val)
	fillValues(head.next, values)

print(linkedListValuesRecursively(a)) # prints ['A', 'B', 'C', 'D']
