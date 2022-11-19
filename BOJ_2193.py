import sys
N = int(sys.stdin.readline())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
dp[3] = 2

currentSum = 2
for i in range(4, N+1):
    dp[i] = 1 + currentSum
    currentSum += dp[i-1]

print(dp[N])