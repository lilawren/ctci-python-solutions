# count number of ways to climb n steps if can jump 1,2,or 3 steps at a time

def numWays(n, memo):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif memo[n] > -1:
		return memo[n]
	else:
		memo[n] = numWays(n - 1, memo) + numWays(n - 2, memo) + numWays(n - 3, memo)
		return memo[n]

n = 4
memo = [-1] * (n+1)
print(memo)
print(numWays(n, memo))