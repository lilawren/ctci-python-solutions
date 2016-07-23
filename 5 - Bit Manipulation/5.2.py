# given double between 0 and 1 print the binary representation

def fracToBin(d):
	bstr = ""

	if d == 0:
		return 0
	elif d == 1:
		return 1

	while d != 0 and d != float("inf"):
		d *= 2
		bstr = bstr + str(d)[0]

		if int(d) == 1:
			d = d - 1

	if len(bstr) > 32:
		return False

	return bstr

print(fracToBin(0.125))
