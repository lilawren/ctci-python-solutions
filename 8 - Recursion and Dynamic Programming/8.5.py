# write a function to recursively multiply 2 positive ints w/o * operator. Addition, subtraction, and bit shifting is allowed.

def mult(n, m):
    memo = list([0] * int(m + 1))
    memo[0] = 0
    memo[1] = n
    return mult2(n, m, memo)

def mult2(n, m, memo):
    m = int(m)
    if n == 0 or m == 0:
        return 0
    elif m == 1:
        return n
    elif memo[m] != 0:
        return memo[m]

    if m%2 == 0: #even
        memo[m] =  mult2(n, m/2, memo) + mult2(n, m/2, memo)
    else: #odd
        memo[m] = mult2(n, (m-1)/2, memo) + mult2(n, (m-1)/2, memo) + n

    return memo[m]



print(mult(9, 8))