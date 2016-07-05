# string compression using counts of repeated characters
# ex: aabcccccaaa a2b1c5a3
# if compressed string is longer, return original string
# assume contains only uppercase and lowercase letters

def compression(input):


	if(len(input) < 2):
		return input

	#compress

	result = ""
	count = 1
	for i in range(0, len(input) - 1):
		if input[i] == input[i+1]:
			count+=1

		else:
			result += input[i] + str(count)
			count = 1

		if i + 1 == len(input) - 1:
			result += input[i+1] + str(count)


	if(len(input) < len(result)):
		return input
	else:
		return result

print(compression("aabcccccaaa"))