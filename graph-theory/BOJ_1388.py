import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

path = []
for _ in range(N):
    path.append(sys.stdin.readline().rstrip())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

deq = deque()

visited = [[0 for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    if path[x][y] == '-':
        adder = 2
    else:
        adder = 0

    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        if visited[x][y]:
            continue
        visited[x][y] = 1

        for i in range(2):
            nx, ny = x + dx[i + adder], y + dy[i + adder]

            if 0 <= nx < N and 0 <= ny < M:
                if path[nx][ny] == '-' and adder == 2:
                    deq.append((nx, ny))
                elif path[nx][ny] == '|' and adder == 0:
                    deq.append((nx, ny))




cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            cnt += 1
            bfs(i, j)

print(cnt)
