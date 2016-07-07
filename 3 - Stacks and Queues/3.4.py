# implement queue using stacks

class Stack:
	list = []

	def __init__(self):
		self.list = []

	def pop(self):
		return self.list.pop()

	def push(self, d):
		self.list.append(d)

	def size(self):
		return len(self.list)

class stackQueue:
	s1 = Stack() #first store
	s2 = Stack() #returns front of queue

	def pop(self):
		if self.s2.size() < 1: #nothing left in s2
			for i in range(len(self.s1.list)):
				self.s2.push(self.s1.pop())
		self.s2.pop()

	def push(self, d):
		self.s1.push(d)

	def peek(self):
		if self.s2.size() < 1:  # nothing left in s2
			for i in range(len(self.s1.list)):
				self.s2.push(self.s1.pop())

		if len(self.s2.list) < 1:
			return
		return self.s2.list[-1]



s = stackQueue()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())