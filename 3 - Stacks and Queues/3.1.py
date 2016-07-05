# implement 3 stacks in an array

class superStack:
	values = []
	numStacks = 3
	sizes = []

	def __init__(self, numStacks):
		self.numStacks = numStacks
		self.sizes = [0] * numStacks

	def pop(self, stackNum):
		if self.sizes[stackNum] == 0:
			return

		# delete segmeent if all None
		for size in self.sizes:
			if self.sizes[stackNum] < size:
				# just set to None
				self.values[self.sizes[stackNum]] = None
				self.sizes[stackNum] -= 1
				return

		#delete segment
		s = int(self.sizes[stackNum] / 3)
		for i in range(s, s + self.numStacks):
			self.values.remove(i)


	def push(self, val, stackNum):
		#check if exists
		for size in self.sizes:
			if size > self.sizes[stackNum]: #segment exists
				self.values[stackNum + (self.sizes[stackNum] * self.numStacks)] = val
				self.sizes[stackNum] +=1
				return

		#segment doesn't exist, add it
		for i in range(0, self.numStacks):
			if i == stackNum:
				self.values.append(val)
				self.sizes[stackNum] += 1
			else:
				self.values.append(0)


	def peek(self, stackNum):
		return self.values[self.sizes[stackNum] - 1]

	def isEmpty(self, stackNum):
		return self.sizes[stackNum]