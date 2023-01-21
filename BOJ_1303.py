import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [[False] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

path = []
for _ in range(M):
    path.append(list(sys.stdin.readline().rstrip()))

blue = 0
white = 0

def bfs(i, j):
    global blue, white
    deq = deque()
    deq.append((i, j))
    max_cnt = 0
    color = path[i][j]
    while deq:
        x, y = deq.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        max_cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and path[nx][ny] == color:
                deq.append((nx, ny))
    if color == 'B':
        blue += max_cnt**2
    else:
        white += max_cnt**2


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

print(white, blue)