import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



path = []
for _ in range(N):
    path.append(list(map(int ,sys.stdin.readline().split())))


visited = [[0 for _ in range(M)] for _ in range(N)]

deq = deque()


def bfs(x, y):
    cnt = 0
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        if visited[x][y]:
            continue
        visited[x][y] = 1
        cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and path[nx][ny]:
                deq.append((nx, ny))

    return cnt


cnt_paint = 0
max_val = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and path[i][j] == 1:
            cnt_paint += 1
            max_val = max(bfs(i, j), max_val)

print(cnt_paint)
print(max_val)


