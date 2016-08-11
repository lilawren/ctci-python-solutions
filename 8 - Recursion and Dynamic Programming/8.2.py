# find a path for a robot starting from top left to move to bottom right

def findPath(map, r, c, deadends):
	if r == len(map) and c == len(map[r]): #return path
		return
	elif deadends[r][c] == True: #dead end
		return
	elif deadends[r+1][c] == False: #check down
		findPath(map, r+1, c, deadends)
	elif c+1 < len(deadends[r]) and deadends[r][c+1] == False: #check right
		findPath(map, r, c+1, deadends)
	else:
		deadends[r][c] == True
		return

	return None

r = 3

c = 3
maps = [[True]*r]*c
maps[1][1] = False
maps[2][1] = False
print(maps)
deadends = [[False]*r]*c
