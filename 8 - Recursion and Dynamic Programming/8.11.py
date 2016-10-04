# calc ways to represent n cents using quarters, dimes, nickels, and pennies
numways = 0

def coins(target, n, memo, cur):
    global numways
    if n < 0:
        return
    if n == 0 and cur not in memo and meets_target(target, cur):
        numways+=1
        print("way: " + str(cur))
        memo.append(cur)
        return

    coins(target, n-25, memo, str(int(cur) + 1000))
    coins(target, n-10, memo, str(int(cur) + 100))
    coins(target, n-5, memo, str(int(cur) + 10))
    coins(target, n-1, memo, str(int(cur) + 1))

def meets_target(target, cur):
    sum = 0
    cur = cur.zfill(4) #padding 0s
    for i in range(len(cur)):
        if i == 0:
            sum += 25 * int(cur[i])
        elif i == 1:
            sum += 10 * int(cur[i])
        elif i == 2:
            sum += 5 * int(cur[i])
        elif i == 3:
            sum += 1 * int(cur[i])

    return sum == target

coins(25, 25, [], 0)
print(numways)