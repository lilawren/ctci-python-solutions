# create a LL for each depth in a binary tree

class LLNode:
	next = None
	data = ""

	def __init__(self, n, d):
		self.next = n
		self.data = d

class Node:
	data = ""
	left = None
	right = None

	def __init__(self, d, l, r):
		self.data = d
		self.left = l
		self.right = r

LL = []

def preOrder(root, depth):

	if root != None:
		if len(LL) < int(depth): #create new LL head
			newLL = LLNode(None, root.data)
			LL.append(newLL)
		else:
			#get last node
			head = LL[depth-1]
			while head.next != None:
				head = head.next
			newNode = LLNode(None, root.data)
			head.next = newNode
		print(root.data)

		preOrder(root.left, depth+1)
		preOrder(root.right, depth+1)

l1 = Node(1, None, None)
r2 = Node(4, None, None)
r1 = Node(3, None, r2)
root = Node(2, l1, r1)

preOrder(root, 1)

print("lists:")
for l in LL: #for each head
	p = l
	while p != None:
		print(p.data, end = " ")
		p = p.next
	print()