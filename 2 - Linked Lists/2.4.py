# partition linked list by element x

from LinkedList import Node

head = Node("3")
head.appendToTail("5")
head.appendToTail("8")
head.appendToTail("5")
head.appendToTail("10")
head.appendToTail("2")
head.appendToTail("1")

def LLpartition(head, x):
	n = head
	lesser = None
	greatereq = None

	while n.next != None:
		if int(n.data) < x: #lesser list
			if lesser == None:
				lesser = n
			else:
				lesser.appendToTail(n.data)
		elif int(n.data) >= x: #greater or equal to
			if greatereq == None:
				greatereq = n
			else:
				greatereq.appendToTail(n.data)
		n = n.next

	if int(n.data) < x:  # lesser list
		if lesser == None:
			lesser = n
		else:
			lesser.appendToTail(n.data)
	elif int(n.data) >= x:  # greater or equal to
		if greatereq == None:
			greatereq = n
		else:
			greatereq.appendToTail(n.data)

	lesser.appendTotail(greatereq)
	return lesser

head.printLL()
head = LLpartition(head, 5)
head.printLL()