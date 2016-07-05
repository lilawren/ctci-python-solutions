class Node:
	next = None
	data = None

	def __init__(self, d):
		self.data = d
		self.next = None

	def appendToTail(self, d):
		n = Node(d)
		cur = self
		while cur.next != None:
			cur = cur.next

		cur.next = n

	def appendNode(self, d):
		cur = self
		while cur.next != None:
			cur = cur.next

		cur.next = d

	def printLL(self):
		n = self
		while n != None:
			print(n.data, end=",")
			n = n.next


def deleteNode(head, d):
	n = head
	#head deleted
	if n.data == d:
		return head.next

	while n.next != None:
		if n.next.data == d: #found
			n.next = n.next.next
			return head #head not changed
		n = n.next
	return head #head not changed