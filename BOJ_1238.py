import sys
from collections import deque


def bfs(cur):
    deq = deque()
    visited = [0] * N
    deq.append((cur, 0))
    while len(deq) != 0:
        x, cnt = deq.popleft()

        for i in range(N):
            if path[x][i]:
                if 0 < visited[i] <= cnt + path[x][i]:
                    continue
                visited[i] = cnt + path[x][i]
                deq.append((i, cnt + path[x][i]))
    return visited


N, M, X = map(int, sys.stdin.readline().split())

path = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    path[a-1][b-1] = w

ans = []
for i in range(N):
    ans.append(bfs(i))

max_val = 0
for i in range(N):
    if i != X-1:
        max_val = max(ans[i][X-1] + ans[X-1][i], max_val)

print(max_val)



# 6 20 3
# 3 2 45
# 6 1 66
# 6 2 31
# 2 4 94
# 5 3 46
# 5 2 79
# 3 1 64
# 4 3 74
# 3 5 59
# 1 6 93
# 3 6 45
# 6 4 40
# 3 4 67
# 1 3 61
# 1 2 42
# 4 2 50
# 4 1 55
# 2 6 93
# 5 4 95
# 1 4 54