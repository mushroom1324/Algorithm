import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

path = []

for _ in range(N):
    path.append(list(map(int, list(sys.stdin.readline().rstrip()))))

deq = deque()
visited = [[[1e9 for _ in range(2)] for _ in range(M)] for _ in range(N)]


def bfs(i, j):
    deq.append((i, j, 0, 0))

    while deq:
        x, y, wall, cnt = deq.popleft()

        if visited[x][y][wall] <= cnt:
            continue
        if wall == 1 and visited[x][y][0] <= cnt:
            continue
        visited[x][y][wall] = cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if path[nx][ny] == 1:
                    if wall == 0:
                        deq.append((nx, ny, 1, cnt + 1))
                else:
                    deq.append((nx, ny, wall, cnt + 1))


bfs(0, 0)
ans = min(visited[N-1][M-1])
if ans == 1e9:
    print(-1)
else:
    print(ans + 1)