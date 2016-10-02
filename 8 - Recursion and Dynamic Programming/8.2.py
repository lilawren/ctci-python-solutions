# find a path for a robot starting from top left to move to bottom right
import copy

def findPath(map, r, c, deadends, path):
	path.append(str(r) + ", " + str(c))

	if r == len(map)-1 and c == len(map[r])-1: #return path
		print("Found path!")
		print(path)
		return True
	elif deadends[r][c] == True: #dead end
		path.pop()
		return False

	if r+1 < len(deadends) and deadends[r+1][c] == False and map[r+1][c] != False: #check down
		#print("check down")
		if not findPath(map, r+1, c, deadends, path):
			path.pop()

	if c+1 < len(deadends[r]) and deadends[r][c+1] == False and map[r][c+1] != False: #check right
		#print("check right")
		if not findPath(map, r, c+1, deadends, path):
			path.pop()

r = 3
c = 3

map = [[True for x in range(r)] for y in range(c)]

map[1][1] = False
map[2][1] = False
print(map)
deadends = [[False]*r]*c
path = []
findPath(map, 0, 0, deadends, path)