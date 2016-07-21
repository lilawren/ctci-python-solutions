# det if tree 2 is subtree of tree 1

# easy approach with more memory

def containsTree(t1, t2):
	str1 = ""
	str2 = ""
	preOrder(t1, str1)
	preOrder(t2, str2)
	return str2 in str1

def preOrder(root, s):
	if root != None:
		s.append(root.data)
		preOrder(root.left, s)
		preOrder(root.right, s)
	elif root == None:
		s.append("X")


# alternative with less memory but poorer worse case run time
def treeMatches(r1, r2):
	if r1 == None and r2 == None:
		return True
	elif r1 == None or r2 == None:
		return False
	elif r1.data != r2.data:
		return False
	else:
		return treeMatches(r1.left, r2.left) and treeMatches(r1.right, r2.right)


def containsTree(t1, t2):
	if t2 == None:
		return True
	return subTree(t1,t2)

def subTree(r1, r2):
	if r1 == None:
		return False
	elif r1.data == r2.data and treeMatches(r1, r2):
		return True
	return subTree(r1.left, r2) or subTree(r1.right, r2)