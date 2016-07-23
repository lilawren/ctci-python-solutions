# return max number of 1s if one 0 bit if flipped to a 1

def maxOnes(b):
	maxz = 0
	left = 0
	right = 0

	init = False
	for i in range(len(b)):

		if b[i] == '0' or i == len(b)-1:
			if left+right+1 > maxz:
				maxz = left+right+1
			left = right
			right = 0
			init = True
		else:
			if not init:
				left += 1
			else:
				right += 1

	return maxz

print(maxOnes("110111011110"))
