# function to check if binary tree is balanced


class Node:
	data = ""
	left = None
	right = None

	def __init__(self, d, l, r):
		self.data = d
		self.left = l
		self.right = r


def inOrder(root, depth):
	if root != None:

		inOrder(root.left, depth+1)
		if depth > checkBalanced.maxD:
			checkBalanced.maxD = depth
		inOrder(root.right, depth+1)

	return checkBalanced.maxD

def checkBalanced(root):
	checkBalanced.maxD = 0
	leftdepth = inOrder(root.left, 1)
	print("left:" + str(leftdepth))
	checkBalanced.maxD = 0
	rightdepth = inOrder(root.right, 1)
	print("right:" + str(rightdepth))

	if abs(leftdepth - rightdepth) > 1:
		return False
	return True

l1 = Node(1, None, None)
r2 = Node(4, None, None)
r1 = Node(3, None, r2)
root = Node(2, l1, r1)

print(checkBalanced(root))
