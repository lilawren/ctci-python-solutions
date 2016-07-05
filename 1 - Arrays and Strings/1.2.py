# given 2 strings det if one is permutation of the other

str1 = "nan123#@#$no"
str2 = "non123#@#$na"

def hash(str):
	tbl = [0] * 128
	for c in str:
		index = ord(c)
		tbl[index]+=1
	return tbl

ar1 = hash(str1)
ar2 = hash(str2)

if(ar1 == ar2):
	print("they are permutations")
else:
	print("they are not permutations")


