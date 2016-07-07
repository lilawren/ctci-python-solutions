# sort stack so smallest items on top, can use additional temp stack but nothing else

class Stack:
	list = []

	def __init__(self):
		self.list = []

	def push(self, d):
		self.list.append(d)

	def sort(self):
		# first elt
		if len(self.list) == 0:
			return

		s = Stack()
		while not self.isEmpty():
			tmp = self.pop()
			if s.peek() == None or s.peek() <= tmp:
				s.push(tmp)
			elif s.peek() > tmp:
				while s.peek() != None and s.peek() > tmp:
					self.push(s.pop())

				s.push(tmp)

		while not s.isEmpty():
			self.push(s.pop())


	def pop(self):
		return self.list.pop()

	def peek(self):
		if self.isEmpty():
			return
		return self.list[-1]

	def isEmpty(self):
		if len(self.list) < 1:
			return True
		return False


s1 = Stack()
s1.push(1)
s1.push(5)
s1.push(1)
s1.push(3)
s1.sort()
print(s1.peek())
s1.pop()
print(s1.peek())
s1.pop()
print(s1.peek())
s1.pop()
print(s1.peek())
s1.pop()
print(s1.peek())