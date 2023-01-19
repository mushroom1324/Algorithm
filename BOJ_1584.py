import sys
from collections import deque


path = [[0] * 501 for _ in range(501)]
visited = [[-1] * 501 for _ in range(501)]

dangerNum = int(sys.stdin.readline())
for _ in range(dangerNum):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            path[i][j] = 1


deathNum = int(sys.stdin.readline())
for _ in range(deathNum):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            path[i][j] = 100


deq = deque()
deq.append((0, 0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while deq:
    x, y, damage = deq.popleft()

    if -1 < visited[x][y] <= damage:
        continue
    visited[x][y] = damage

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 500 and 0 <= ny <= 500:
            if not path[nx][ny]:
                deq.appendleft((nx, ny, damage))
            elif path[nx][ny] == 1:
                deq.append((nx, ny, damage + 1))

print(visited[500][500])



