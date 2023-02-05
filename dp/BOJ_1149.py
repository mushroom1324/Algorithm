import sys
N = int(sys.stdin.readline())

path = []
for _ in range(N):
    path.append(list(map(int, sys.stdin.readline().split())))

"""
logic:
    1. bfs           
        - failed (time limit exceeded)
    2. dp
        - gotcha bitch
========================================================================
from collections import deque

deq = deque()
visited = [[1e9 for _ in range(3)] for _ in range(N)]

for i in range(3):
    deq.append((i, 0, 0))

while deq:
    index, cnt, cost = deq.popleft()
    if visited[cnt][index] <= cost + path[cnt][index]:
        continue
    visited[cnt][index] = cost + path[cnt][index]
    if cnt + 1 == N:
        continue
    for i in range(3):
        if i != index:
            deq.append((i, cnt + 1, visited[cnt][index]))

print(min(visited[N-1]))
========================================================================
"""

dp = [[1e9 for _ in range(3)] for _ in range(N)]

for i in range(3):
    dp[0][i] = path[0][i]

for cnt in range(N-1):
    for i in range(3):
        for j in range(3):
            if i != j:
                dp[cnt + 1][j] = min(dp[cnt + 1][j], dp[cnt][i] + path[cnt + 1][j])

print(min(dp[N-1]))