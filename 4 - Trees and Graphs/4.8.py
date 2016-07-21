# find first common ancestor

class Node:
	data = ""
	left = None
	right = None
	parent = None

	def __init__(self, d, l, r, p):
		self.data = d
		self.left = l
		self.right = r
		self.parent = p

def findAncestor(a, b):
	da = findDepth(a)
	db = findDepth(b)

	print(da)
	print(db)
	deeper = a
	higher = b
	if da < db:
		deeper = b
		higher = a

	for i in range(abs(da - db)):
		deeper = deeper.parent

	while higher!=None and deeper!=None and higher.parent != deeper.parent:
		higher = higher.parent
		deeper = deeper.parent

	return deeper.parent

def findDepth(n):
	depth = 0
	while n.parent != None:
		depth += 1
		n = n.parent
	return depth

l2 = Node(15, None, None, None)
l1 = Node(10, None, l2, None)
l2.parent = l1
r1 = Node(30, None, None, None)
root = Node(20, l1, r1, None)
l1.parent = root
r1.parent = root

print(findAncestor(l2, r1).data)