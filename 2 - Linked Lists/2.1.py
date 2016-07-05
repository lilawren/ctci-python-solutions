from LinkedList import Node

def removeDupes(head): #use set
	n = head
	prev = None
	myset = set()
	while n.next != None:
		if n.data in myset: #found dupe
			prev.next = n.next #remove dupe
		else:
			myset.add(n.data)
			prev = n
		n = n.next #move forward

	#do for last element
	if n.data in myset:  # found dupe
		prev.next = None



head = Node("1")
head.appendToTail("2")
head.appendToTail("1")
head.appendToTail("4")

head.printLL()
removeDupes(head)
head.printLL()

