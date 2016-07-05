# assume you have method isSubsting which CHECKS if a word is substring of another. Given strs s1, s2, check if s2 is a rotation of s1 using only one call to isSubstring.

str1 = "waterbottle"
str2 = "erbottlewar"

def strRot(s1, s2):
	if(len(s1) == len(s2) and len(s1) > 0):
		return(isSubString(s1+s1, s2))

strRot(str1, str2)
