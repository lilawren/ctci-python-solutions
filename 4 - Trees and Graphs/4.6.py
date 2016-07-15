# return the next inorder node of a BST

def mostLeft(n):
	if n == None:
		return None
	while n.left != None:
		n = n.left
	return n

def nextInorder(n):
	if n == None:
		return None
	if n.right != None: #there is a right node
		return mostLeft(n.right)
	else: #need to back up to untraversed territory
		q = n
		p = q.parent
		while p!= None and p.left != q:
			q = p
			p = p.parent
		return p