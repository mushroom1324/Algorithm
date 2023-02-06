import sys

N = int(sys.stdin.readline())

"""

nth triangle = T(n):
    T(n) = T(n-1) + n
     
nth tetrahedron = TE(n):
    TE(n) = T(n-1) + T(n-2) + ... + T(1)
"""

T = [1]

cur = T[0]
index = 2
while cur <= 300000:
    T.append(cur + index)
    cur = T[index-1]
    index += 1

TE = [0 for _ in range(120)]
TE[0] = 1
for i in range(1, 120):
    TE[i] = TE[i-1] + T[i]


dp = [1e9]*(N+1)

for i in range(1, N+1):
    for each in TE:
        if each >= i:
            if each == i:
                dp[i] = 1
            break
        dp[i] = min(dp[i], 1 + dp[i-each])
print(dp[N])
