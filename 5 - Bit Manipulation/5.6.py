# write fcn to det the number of bits to flip to convert int A into B

def bitsToFlip(a, b):
	res = bin(a ^ b)
	print(res)
	return res.count('1')

print(bitsToFlip(29, 15))
print(bitsToFlip(15, 1))
