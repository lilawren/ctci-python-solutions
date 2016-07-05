# partition linked list by element x

from LinkedList import Node


def LLpartition(head, x):
	n = head
	lesser = None
	greatereq = None

	if n.next == None:
		return n

	while n != None:
		if int(n.data) < x: #lesser list
			if lesser == None:
				lesser = Node(n.data)
				lesser.next = None
			else:
				lesser.appendToTail(n.data)
		elif int(n.data) >= x: #greater or equal to
			if greatereq == None:
				greatereq = Node(n.data)
				greatereq.next = None
			else:
				greatereq.appendToTail(n.data)
		n = n.next

	lesser.appendNode(greatereq) #combine
	return lesser


head = Node("3")
head.appendToTail("5")
head.appendToTail("8")
head.appendToTail("5")
head.appendToTail("10")
head.appendToTail("2")
head.appendToTail("1")

head.printLL()
head = LLpartition(head, 5)
head.printLL()