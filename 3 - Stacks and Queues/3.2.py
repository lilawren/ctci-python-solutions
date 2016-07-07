# design stack O(1) pop, push, and min which returns min

class myStack:
	stack = []
	globalMin = 0

	def pop(self):
		self.stack.pop()

	def push(self, d):
		#init first globalMin
		if len(self.stack) < 1:
			self.globalMin = d.data

		d.prevMin = self.globalMin

		if d.data < self.globalMin: #if new data is smaller
			self.globalMin = d.data

		self.stack.append(d)

	def min(self):
		return self.globalMin

class stackNode:
	def __init__(self, d):
		self.data = d

	data = 0
	prevMin = 0

a = stackNode(4)
b = stackNode(7)
c = stackNode(1)

stk = myStack()
stk.push(a)
stk.push(b)
stk.push(c)

for s in stk.stack:
	print(s.data)
print(stk.min())
