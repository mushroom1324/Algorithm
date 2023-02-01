"""
first implementation fucked up bc of the time complexity ...
===========================================first implementation===========================================
import sys
from collections import deque

N = int(sys.stdin.readline())
path = []
for _ in range(N):
    path.append(list(map(int, sys.stdin.readline().split())))


visited = [[0 for _ in range(3)] for _ in range(N + 1)]
deq = deque()
deq.append((0, 0, 0))
deq.append((0, 1, 0))
deq.append((0, 2, 0))
while deq:
    x, y, cnt = deq.popleft()

    visited[x][y] = cnt

    if x == N:
        continue

    cur = cnt + path[x][y]

    if y == 0:
        if visited[x+1][0] < cur:
            deq.append((x+1, 0, cur))
        if visited[x+1][1] < cur:
            deq.append((x+1, 1, cur))
    elif y == 1:
        if visited[x+1][0] < cur:
            deq.append((x+1, 0, cur))
        if visited[x+1][1] < cur:
            deq.append((x+1, 1, cur))
        if visited[x + 1][2] < cur:
            deq.append((x + 1, 2, cur))
    else:
        if visited[x+1][1] < cur:
            deq.append((x+1, 1, cur))
        if visited[x + 1][2] < cur:
            deq.append((x + 1, 2, cur))


temp_max = max(visited[N])

visited = [[1e9 for _ in range(3)] for _ in range(N + 1)]
deq.append((0, 0, 0))
deq.append((0, 1, 0))
deq.append((0, 2, 0))
while deq:
    x, y, cnt = deq.popleft()

    visited[x][y] = cnt

    if x == N:
        continue

    cur = cnt + path[x][y]

    if y == 0:
        if visited[x+1][0] > cur:
            deq.append((x+1, 0, cur))
        if visited[x+1][1] > cur:
            deq.append((x+1, 1, cur))
    elif y == 1:
        if visited[x+1][0] > cur:
            deq.append((x+1, 0, cur))
        if visited[x+1][1] > cur:
            deq.append((x+1, 1, cur))
        if visited[x + 1][2] > cur:
            deq.append((x + 1, 2, cur))
    else:
        if visited[x+1][1] > cur:
            deq.append((x+1, 1, cur))
        if visited[x + 1][2] > cur:
            deq.append((x + 1, 2, cur))

print(temp_max, min(visited[N]))
===========================================first implementation===========================================
now we're using dp..
"""
import sys

N = int(sys.stdin.readline())
path = []

dp_max = [0 for _ in range(3)]
dp_min = [0 for _ in range(3)]

cur_max = [0 for _ in range(3)]
cur_min = [0 for _ in range(3)]

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    for i in range(3):
        if i == 0:
            cur_max[i] = a + max(dp_max[0], dp_max[1])
            cur_min[i] = a + min(dp_min[0], dp_min[1])
        elif i == 1:
            cur_max[i] = b + max(dp_max[0], dp_max[1], dp_max[2])
            cur_min[i] = b + min(dp_min[0], dp_min[1], dp_min[2])
        else:
            cur_max[i] = c + max(dp_max[1], dp_max[2])
            cur_min[i] = c + min(dp_min[1], dp_min[2])

    dp_max = cur_max[:]
    dp_min = cur_min[:]


print(max(dp_max), min(dp_min))

