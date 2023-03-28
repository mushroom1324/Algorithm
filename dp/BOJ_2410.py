import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N + 1)]

if N == 1:
    print(1)
    quit()

dp[1] = 1
dp[2] = 2
for i in range(3, 1 + N):
    if i % 2:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i//2]) % 1_000_000_000

print(dp[N])