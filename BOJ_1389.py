import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

path = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    path[A].append(B)
    path[B].append(A)

deq = deque()
visited = [[101 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, 1 + N):
    deq.append((i, i, 0))

while deq:
    target, cur, cnt = deq.popleft()

    if visited[target][cur] <= cnt:
        continue
    visited[target][cur] = cnt
    for i in path[cur]:
        deq.append((target, i, cnt + 1))


index = 1
ans = 0
cur_min = 1e9
for each in visited[1:]:
    temp = 0
    for i in each[1:]:
        temp += i
    if temp < cur_min:
        cur_min = temp
        ans = index
    index += 1


print(ans)