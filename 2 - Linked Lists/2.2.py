# return kth to last element in a singly linked list

from LinkedList import Node

def removeKth(head, k):
	#Use two pointers
	n = head
	m = head
	counter = 0
	while m != None:
		if counter == k+1:
			n = n.next
		else:
			counter += 1
		m = m.next

	#check if out of bounds
	if counter  < k:
		return head

	# check if head changed
	if n == head and counter == k:
		return head.next

	#remove kth from last

	n.next = n.next.next

	return head

head = Node("1")
head.appendToTail("2")
head.appendToTail("1")
head.appendToTail("4")

head.printLL()
head = removeKth(head, 3)
head.printLL()
