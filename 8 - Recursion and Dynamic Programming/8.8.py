# find all permutations of strings with duplicate characters. List of permutations should not have duplicates

def findPermutations(substr, memo):

    for i in range(len(substr)): #add character to end of each
        c = substr[i]
        if c not in substr[i+1:]:
            print(memo + c)
            findPermutations(substr[:i] + substr[i+1:], memo + c)


findPermutations("abca", "")