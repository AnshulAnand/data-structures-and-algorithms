
# print sum of a linked list

from linked_list import Node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

def linkedListSum(head):
	ans = 0
	current = head
	while current != None:
		ans += current.val
		current = current.next
	return ans

print(linkedListSum(a)) # prints 10

# recursive approach

def linkedListSumRecursively(head):
	if head == None: return 0
	return head.val + linkedListSumRecursively(head.next)

print(linkedListSumRecursively(a)) # prints 10
