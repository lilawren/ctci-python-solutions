# return number of paths in binary tree with sum of target

#we reuse this function a lot


def countFromRoot(root, target, cursum):
	cursum += root.data
	totalpaths = 0
	if cursum == target:
		totalpaths+=1

	totalpaths += countFromRoot(root.left, target)
	totalpaths += countFromRoot(root.right, target)
	return totalpaths


def countPathsWithSum(root, target):
	if root == None:
		return 0

	pathsFromRoot = countFromRoot(root, target, 0)

	pathsOnLeft = countPathsWithSum(root.left, target)
	pathsOnRight = countPathsWithSum(root.right, target)

	return pathsFromRoot + pathsOnLeft + pathsOnRight

