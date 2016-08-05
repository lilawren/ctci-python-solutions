# write program to swap odd and even bits in an int

def rshift(val, n): return val>>n if val >= 0 else (val+0x100000000)>>n

def swap(myint):
	swapped = (rshift((myint & 0xaaaaaaaa), 1)) | ((myint & 0x55555555) << 1)
	return swapped

print(bin(swap(37)))
