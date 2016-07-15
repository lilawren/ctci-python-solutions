# given sorted ascending array with unique elements, write alg to create min height binary tree

class Node:
	data = ""
	left = None
	right = None

	def __init__(self, d, l, r):
		self.data = d
		self.left = l
		self.right = r

class Tree:
	root = None

	def __init__(self, r):
		self.root = r

# recursive tree constructor
def minTree(ar):
	print(ar)

	if len(ar) <= 0:
		return Tree(Node(None, None, None))
	if len(ar) == 1:
		return Tree(Node(ar[0], None, None))
	elif len(ar) == 2:
		n1 = Node(ar[1], None, None)
		n1.left = Node(ar[0], None, None)
		return Tree(n1)
	elif len(ar) == 3:
		n1 = Node(ar[1], None, None)
		n1.left = Node(ar[0], None, None)
		n1.right = Node(ar[2], None, None)
		return Tree(n1)
	else: 				# split the tree and call minTree on the parts
		half = int(len(ar) / 2) 		# where to split
		if len(ar) % 2 == 0: #even
			half = int(len(ar) / 2)


		print("### split:" + str(ar[half]))

		ar1 = ar[:int(half)]
		ar2 = ar[int(half + 1):]

		left = minTree(ar1)
		right = minTree(ar2)
		root = Node(ar[half], left.root, right.root)  # root node

		return Tree(root)

def inOrder(node):
	if node != None:
		inOrder(node.left)
		if node.data != None:
			print(node.data)
		inOrder(node.right)

a = list(range(10))
print(a)
treeroot = minTree(a).root

# do in order traversal
print("\nin order traversal:")
inOrder(treeroot)
