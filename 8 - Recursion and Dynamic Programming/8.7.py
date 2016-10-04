# find all permutations of strings without duplicate characters

def findPermutations(substr, memo):

    for i in range(len(substr)): #add character to end of each
        c = substr[i]
        print(memo + c)
        findPermutations(substr[:i] + substr[i+1:], memo + c)


findPermutations("abcd", "")