import sys
from collections import deque

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

deq = deque()


def bfs(i, j):
    deq.append((i, j))

    while deq:
        x, y = deq.popleft()

        if visited[x][y] == 1:
            continue
        visited[x][y] = 1

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and path[nx][ny] == 1:
                deq.append((nx, ny))


while True:

    N, M = map(int, sys.stdin.readline().split())

    if N == M == 0:
        break

    path = []
    for _ in range(M):
        path.append(list(map(int, sys.stdin.readline().split())))


    visited = [[0 for _ in range(N)] for _ in range(M)]
    cnt = 0
    for i in range(M):
        for j in range(N):
            if path[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    print(cnt)