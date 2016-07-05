# 3 edits: add, delete, or replace a char. Given two strings, write a function to check if they are one/0 edits away

def checkStrs(str1, str2):
	if str1 == str2:
		return True

	found = False

	# at most one character disparity

	#count total of each char and allow only one disparity
	count1 = [0] * 128
	for c in str1:
		count1[ord(c)] += 1

	count2 = [0] * 128
	for c in str2:
		count2[ord(c)] += 1

	found2 = False

	for i in range(128):
		if abs(count1[i] - count2[i]) == 1 and not found:	#found single disparity
			found = True
		elif abs(count1[i] - count2[i]) == 1 and found and not found2:	#found second disparity
			found2 = True
		elif abs(count1[i] - count2[i]) == 1 and found2:  # found third disparity
			return False
		elif abs(count1[i] - count2[i]) > 1: # found more than 1 disparity
			return False

	return True

print(checkStrs("pale", "bake"))