# In a sorted array of distinct ints find i s.t. A[i] = i

def binSearch(A, start, end):
    i = start + int((end-start)/2)
    #print(A)
    #print("start:" + str(start) + " end:" + str(end) + " i:" + str(i))
    #print(str(A[i]) + " " + str(i))
    local_i = int((end-start)/2)
    if len(A) == 0:
        print("No number found!\n")
    elif A[local_i] == i:
        print("Found magic number at " + str(i) + "\n")
    elif A[local_i] < i: #split to right
        binSearch(A[i:end], i, end)
    elif A[local_i] > i: #split to left
        binSearch(A[start:i], start, i)


A1 = [-3, -1, 0, 3, 5, 7]
A2 = [-2, -2, 3, 3, 9, 9]

binSearch(A1, 0, len(A1)-1)
binSearch(A2, 0, len(A2)-1)