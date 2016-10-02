# recursively multiply

def mult(n,m):
    if m%2==0: #even
        return n << int(m/2)
    else:
        return n + mult(n, m-1)

print(mult(4, 3))