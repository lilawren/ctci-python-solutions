# given a BST list arrays that could have produced it
# incomplete

class Node:
	data = ""
	left = None
	right = None

	def __init__(self, d, l, r):
		self.data = d
		self.left = l
		self.right = r

def findArrays(root):

	n = root

	leftPreorder(n)
	rightPreorder(n)

def leftPreorder(root):
	if root != None:
		print(root.data)
		print("left:")
		leftPreorder(root.left)
		leftPreorder(root.right)

def rightPreorder(root):
	if root != None:
		print(root.data)
		print("right:")
		rightPreorder(root.right)
		rightPreorder(root.left)


l2 = Node(15, None, None)
l1 = Node(10, None, l2)
r1 = Node(30, None, None)
root = Node(20, l1, r1)
findArrays(root)
