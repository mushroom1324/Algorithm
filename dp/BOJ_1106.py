"""
1106 :
first implementation with bfs has failed due to time limit..
==============================================================================
import sys
from collections import deque

C, N = map(int, sys.stdin.readline().split())

path = []
deq = deque()
visited = [0 for _ in range(1101)]
ans = 1e9

for i in range(N):
    path.append(tuple(map(int, sys.stdin.readline().split())))
    deq.append(path[i])

while deq:
    cost, customer = deq.popleft()
    if customer >= C:
        ans = min(ans, cost)
        continue

    visited[customer] = cost

    for i in range(N):
        cur_cost, cur_customer = path[i][0], path[i][1]
        if not 0 < visited[customer + cur_customer] <= cost + cur_cost:
            deq.append((cost + cur_cost, customer + cur_customer))

print(ans)
==============================================================================

"""
import sys

C, N = map(int, sys.stdin.readline().split())
arr = []

dp = [1e9 for _ in range(C + 100)]
dp[0] = 0
ans = 1e9

for i in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

for cost, customer in arr:
    for i in range(customer, C + 100):
        dp[i] = min(dp[i-customer] + cost, dp[i])

print(min(dp[C:]))
