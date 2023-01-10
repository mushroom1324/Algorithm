import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

path = []

for _ in range(N):
    path.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

deq = deque()
cnt = 0
visited = [[False] * M for _ in range(N)]
top = True


for n in range(N):
    for m in range(M):
        if path[n][m] != 0 and not visited[n][m]:
            deq.append((n, m))
            while len(deq) != 0:
                x, y = deq.popleft()

                if visited[x][y]:
                    continue
                visited[x][y] = True

                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        if path[x][y] == path[nx][ny]:
                            deq.append((nx, ny))
                        elif path[x][y] < path[nx][ny]:
                            top = False
            if top:
                cnt += 1
            top = True


print(cnt)