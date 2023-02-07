import sys

N = int(sys.stdin.readline())


loss = list(map(int, sys.stdin.readline().split()))
loss.insert(0, 0)
joy = list(map(int, sys.stdin.readline().split()))
joy.insert(0, 0)

dp = [[0 for _ in range(101)] for _ in range(N + 1)]


for i in range(1, 1 + N):
    for j in range(1, 101):
        if loss[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss[i]] + joy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])