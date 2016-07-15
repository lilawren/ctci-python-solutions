# function to check if binary tree is balanced


class Node:
	data = ""
	left = None
	right = None

	def __init__(self, d, l, r):
		self.data = d
		self.left = l
		self.right = r



def inOrder(root, minval, maxval):
	if root != None:

		if (minval != None and root.data <= minval) or (maxval != None and root.data > maxval):
			return False

		if not inOrder(root.left, minval, root.data) or not inOrder(root.right, root.data, maxval):
			return False

	return True

l2 = Node(15, None, None)
l1 = Node(10, None, l2)
r1 = Node(30, None, None)
root = Node(20, l1, r1)

print(inOrder(root, None, None))
