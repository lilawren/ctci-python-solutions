class SetOfStacks:
	stacks = []
	limit = 2

	def __init__(self, l):
		self.limit = l

	def push(self,d):
		if (len(self.stacks) == 0) or (len(self.stacks[-1].list) == self.limit): #create new stack
			st = Stack()
			st.push(d)
			self.stacks.append(st)
		else: #use existing stack
			self.stacks[-1].push(d)

	def pop(self):
		if len(self.stacks[-1].list) == 1:  # delete stack
			self.stacks.pop()
		else:
			self.stacks[-1].pop()

	def popAt(self, i):
		if(len(self.stacks[i].list) == 1):
			self.stacks.pop(i)
		else:
			self.stacks[i].pop()

class Stack:
	list = []

	def __init__(self):
		self.list = []

	def push(self, d):
		self.list.append(d)

	def pop(self):
		self.list.pop()


setstk = SetOfStacks(2)

setstk.push(1)
setstk.push(2)
setstk.push(3)
setstk.push(4)
setstk.popAt(0)
setstk.popAt(0)

for s in setstk.stacks:
	print(s.list)
print()
