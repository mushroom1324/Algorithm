import sys
N = int(sys.stdin.readline())
dp = [0, 1]

if N < 0:
    N = abs(N)
    if N % 2 == 0:
        print(-1)
    else:
        print(1)

elif N == 0:
    print(0)
else:
    print(1)


for i in range(2, N+1):
    dp.append((dp[i-1] + dp[i-2]) % 1000000000)

print(dp[N])