# det if there exists a path between a and b in a graph

#using recursive DFS
def search(node, node2):
	if node == None or node2 == None:
		return

	if node == node2:
		return True

	node.visited = True

	for n in node.adjacent:
		if n.visited == False:
			if search(n, node2):
				return True

#using iterative, queue based BFS
def search(node, node2):
	q = Queue()
	node.marked = True
	q.enqueue(node)
	while not q.isEmpty():
		r = q.dequeue()

		if r == node2:
			return True

		for n in r.adjacent:
			if n == node2:
				return True

			if n.marked == False:
				n.marked = True
				q.enqueue(n)

	return False
