# get next smallest and next largest given an int with the same number of binary 1s

def nextSmallest(n):
	c = n
	c0 = 0
	c1 = 0
	print(bin(c))

	while (c&1) == 1: #trailing 1s
		c1 += 1
		c >>= 1

	if c == 0:
		return None

	while c&1 == 0 and c!= 0: #trailing 0s
		c0 += 1
		c >>= 1

	p = c0 + c1
	print("p:" + str(p))
	#clear bits to right of p inclusive
	n = n & (-1 << (p+1))
	print("cleared")
	print(bin(n))
	#insert c1+1 ones to right of p
	n = n | (1 << c1 +1)-1 << (c0 -1)
	print("inserted")
	print(bin(n))

	return n



def nextLargest(n):
	c = n
	c0 = 0
	c1 = 0
	while (c & 1) == 0 and c!=0: #trailing 0s
		c0+=1
		c >>= 1
		#print(bin(c))
	#print(c0)

	while c & 1 == 1: # trailing 1s
		c1+=1
		c >>=1
		#print(bin(c))
	#print(c1)

	#consider error
	if c0 +c1 == 31 or c0 + c1 == 0:
		return None

	p = c0 + c1
	print("p:" + str(p))

	#flip right most non trailing 0
	n = n | (1 << p)
	print("flipped\n" + bin(n))

	#clear bits right of p
	n = n & (-1 << p)
	print("cleared\n" + bin(n))

	#insert c1-1 ones to the right
	n = n | (1 << c1 - 1)- 1
	print("inserted\n" + bin(n))

	return n

n = 13948
m = int("10011110000011",2)
print("next smallest:" + bin(nextSmallest(m)))
print()
print("next largest:" + bin(nextLargest(n)))