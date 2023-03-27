import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

VIP = []

for _ in range(M):
    VIP.append(int(sys.stdin.readline()))


dp = [0 for _ in range(max(3, N + 1))]
dp[1] = 1
dp[2] = 2
for i in range(3, 1 + N):
    dp[i] = dp[i-2] + dp[i-1]


groups = []
streak = 0
for i in range(1, 1 + N):
    streak += 1
    if i in VIP:
        if streak > 1:
            groups.append(dp[streak - 1])
        streak = 0
if streak:
    groups.append(dp[streak])

ans = 1
for each in groups:
    ans *= each
print(ans)