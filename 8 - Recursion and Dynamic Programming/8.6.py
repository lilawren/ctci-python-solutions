# Towers of Hanoi

A = [3, 2, 1]
B = []
C = []

print(A)
print(B)
print(C)
print()

def move(n, s, t, buf):
    if n > 0:
        move(n-1, s, buf, t) # move n-1 disks from source to buffer
        t.append(s.pop())
        print(A)
        print(B)
        print(C)
        print()
        move(n-1, buf, t, s) # move the n-1 disks from buffer to target

move(3, A, C, B)
print(A)
print(B)
print(C)