from LinkedList import Node

def removeDupes(head): #use set
	n = head
	prev = None
	myset = set()
	while n != None:
		if n.data in myset: #found dupe
			prev.next = n.next #remove dupe
		else:
			myset.add(n.data)
			prev = n
		n = n.next #move forward



head = Node("1")
head.appendToTail("2")
head.appendToTail("1")
head.appendToTail("4")

head.printLL()
removeDupes(head)
head.printLL()

