# implement class with random node selection
import random

class TreeNode:
	data = ""
	left = None
	right = None
	size = 0

	def __init__(self, d):
		self.data = d
		self.size = 1

	def getRandomNode(self):
		leftSize = self.left.size
		rnd = random()
		index = round(rnd * self.size) # check random vs. size
		if index < leftSize:
			return self.left.getRandomNode()
		elif index == leftSize:
			return self
		else:
			return self.right.getRandomNode()

	def insertInOrder(self, d):
		if d <= self.data:
			if self.left == None:
				self.left = TreeNode(d)
			else:
				self.left.insertInOrder(d)
		else:
			if self.right == None:
				self.right = TreeNode(d)
			else:
				self.right.insertInOrder(d)

		self.size+=1

	def find(self, d):
		if d == self.data:
			return self
		elif d <= self.data:
			if self.left == None:
				return None
			return self.left.find(d)
		elif d > self.data:
			if self.right == None:
				return None
			return self.right.find(d)

		return None
	