# write alg to print all valid combinations of n pairs of parenthesis
# ex: n = 3, output = ((())), (()()), (())(), ()(()), ()()()

def parens(n):
    memo = [""]
    if n == 0:
        print(memo)
    else:
        memo = ["()"]

    parens_helper(1, n, memo)


def parens_helper(m, n, memo):

    #print("\n m:" + str(m))
    if m == n:
        print(memo)
        return memo

    new_memo = []

    for i in range(len(memo)):
        #print(i)

        if m >= 1:
            #print("outside parens")
            new_memo.append("(" + memo[i] + ")") # add outside parens
            if m >= 2:
                #print("left right")

                if i < (len(memo) - 1):
                    new_memo.append(memo[i] + "()") # add right on side
                    new_memo.append("()" + memo[i])  # add left on side

        if i == (len(memo) - 1):  # add for single parens only (last one)
            if memo[i] != "":  # append
                #print("last parens")
                new_memo.append(memo[i] + "()")

    parens_helper(m+1, n, new_memo)

parens(3)