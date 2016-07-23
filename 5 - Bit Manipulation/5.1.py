# Insert M bits into N bits at [j,i]

def insertBits(N, M, i, j):

	#clear area for M
	#command = "{:0" + str(len(str(N))) + "b}" #used for format

	#padding
	padding = '1' * len(str(N))

	#mask = command.format(int('1' * len(str(M)),2))
	mask = int('1' * len(str(M)), 2)
	print(bin(mask))

	mask = mask << int(i)
	print("shift " + bin(mask))

	mask = ~mask & int(padding, 2) # pad the mask
	print("negate " + bin(mask))

	cleared = int(N) & int(mask)
	print("cleared " + bin(cleared))

	#insert M, shift and or it
	mask2 = int(str(M), 2) << int(i)
	print("mask to or with " + bin(mask2))
	return bin(int(cleared) | int(mask2))


print(insertBits(10000000000, 10011, 2, 6))
