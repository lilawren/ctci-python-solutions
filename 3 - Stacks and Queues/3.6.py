import copy

class Animal:
	time = 0
	name = ""

class Dog(Animal):
	flu = False

class Cat(Animal):
	Fleas = False

class AnimalSheleter:
	cats = Node()
	dogs = Node()

	def __init__(self):
		self.cats = Node()
		self.dogs = Node()

	#obj contains pet info and time
	def enqueue(self, obj, type):
		if(type == "cat"):
			self.cats.addNode(obj) #add to end
		elif type == "dog":
			self.dogs.addNode(obj) #add to end

	def dequeueAny(self):
		if self.cats == None and self.dogs == None:
			return
		elif self.cats == None and self.dogs != None:
			res = copy.deepcopy(self.dogs)
			self.dogs = self.dogs.next
			return res
		elif self.cats != None and self.dogs == None:
			res = copy.deepcopy(self.cats)
			self.cats = self.cats.next
			return res

		if self.cats.time > self.dogs.time:
			res = copy.deepcopy(self.cats)
			self.cats = self.cats.next
			return res
		elif self.cats.time <= self.dogs.time:
			res = copy.deepcopy(self.dogs)
			self.dogs = self.dogs.next
			return res

	def dequeueDog(self):
		if self.dogs == None:
			return
		else:
			res = copy.deepcopy(self.dogs)
			self.dogs = self.dogs.next
			return res

	def dequeueCat(self):
		if self.cats == None:
			return
		else:
			res = copy.deepcopy(self.cats)
			self.cats = self.cats.next
			return res
