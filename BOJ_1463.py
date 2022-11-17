import sys
N = int(sys.stdin.readline())

dp = [0] * (N+1)

for i in range(1, N):
    curr = i+1
    dp[i] = dp[i-1] + 1

    if curr % 2 == 0:
        dp[i] = min(dp[i], 1 + dp[curr//2-1])
    if curr % 3 == 0:
        dp[i] = min(dp[i], 1 + dp[curr//3-1])

print(dp[N-1])