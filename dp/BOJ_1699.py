import sys

N = int(sys.stdin.readline())

dp = [i for i in range(100_001)]

for i in range(1, N + 1):
    if i * i <= 100000:
        for each_dp in range(1, N + 1):
            if each_dp >= i * i:
                dp[each_dp] = min(dp[each_dp], 1 + dp[each_dp - (i * i)])

print(dp[N])