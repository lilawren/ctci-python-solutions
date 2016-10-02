# return subsets

import copy
def subset(A, ss):

    if len(A) > 0:
        #print(ss)

        # make copy
        for i in range(0, len(ss)):
            ss.append(copy.deepcopy(ss[i]))

        #print(ss)

        #add values to the subsets
        first = A[0]
        for i in range(int(len(ss)/2), len(ss)):
            if ss[i] == None: # if None
                ss[i] = first
            elif(isinstance(ss[i], list)): #check if already a list
                ss[i].append(first)
            else: #if it is a list
                l = [ss[i]]
                ss[i] = l
                ss[i].append(first)
            #print(ss)

        return subset(A[1:], ss)

    else:
        return(ss)

A = [1]
print(subset(A, [None]), end="\n\n")

B = [2,4]
print(subset(B, [None]), end="\n\n")

C = [8,3,2]
print(subset(C, [None]), end="\n\n")

