# Write a method to replace all spaces in a string with '%20' and you are given the true length of a string
# do not go beyond true length

def URLify(str, length):
	res = ""
	if length > len(str):
		return
	for i in range(length):
		if str[i] == ' ':
			res += "%20"
		else:
			res += str[i]
	print(res)

URLify("wa wee wooo  ha ", 16)