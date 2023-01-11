import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

path = []

for _ in range(N):
    temp = list(sys.stdin.readline().rstrip())
    for i in range(M):
        temp[i] = int(temp[i])
    path.append(temp)

deq = deque()
deq.append((0, 0, 0))

visited = [[1000] * M for _ in range(N)]



while len(deq) != 0:
    x, y, cnt = deq.popleft()

    if visited[x][y] <= cnt:
        continue
    visited[x][y] = cnt

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if path[nx][ny] == 1:
                deq.append((nx, ny, cnt + 1))
            else:
                deq.append((nx, ny, cnt))

print(visited[N-1][M-1])

