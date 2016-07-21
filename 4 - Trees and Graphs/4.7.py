# implement build order function
# incomplete

import copy

class Graph:
	nodes = []

	def __init__(self, n):
		self.nodes = [n]

	def add(self, n):
		self.nodes.append(n)

class Node:
	data = ""
	child = []

	def __init__(self, d, c):
		self.data = d
		self.child = c

def buildOrder(ar, build):
	g = Graph([])

	#loop through each build dependency
	for b in build:
		g.add(Node(b[0], b[1]))

	#compare with ar, add missing things

	return True

ar = list("abcdef")
print(ar)
build = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
print(buildOrder(ar, build))


