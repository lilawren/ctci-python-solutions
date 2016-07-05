# Given a string write a function to CHECK if it is a permutation of a palindrome. A palindrome is str that is same forwards and backwards
# find all permutations that are palindromes

#str = input("enter a string:")

def palinPerm(str):
	words = str.split()

	total_length = 0
	for word in words:
		total_length += len(word)

	count = [0] * 128

	for word in words:
		for c in word:
			count[ord(c)] += 1

	found = False
	for ct in count:
		if not found and ct == 1:
			found = True
		elif ct == 1:
			return False

	return True

print(palinPerm("taco tac"))
