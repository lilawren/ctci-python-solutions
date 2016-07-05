# Create alg to determine str is all unique characters. What if cannot use additional data structures?

input = input("enter a string:")

history = [False] * 128

print(history)

for c in input:
	index = ord(c)
	if history[index]:
		print("Not unique!")
		exit(1)
	else:
		history[index] = True

print(history)
print("Unique string!")
