# Delete middle node

from LinkedList import Node

head = Node("1")
head.appendToTail("2")
head.appendToTail("1")
head.appendToTail("4")

def removeMid(node):
	if node == None or node.next == None:
		return
	else:
		d = node.next
		node.data = d.data
		node.next = d.next
		d.data = None
		d.next = None


head.printLL()
removeMid(head.next.next.next)
head.printLL()