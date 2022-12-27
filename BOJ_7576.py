import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
path = []
for i in range(N):
    path.append(list(map(int, sys.stdin.readline().split())))

bfs = deque()
shortest = 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def search():
    global shortest
    while len(bfs) != 0:
        temp = bfs.popleft()
        shortest = max(temp[2], shortest)
        for i in range(4):
            nx, ny = temp[0] + dx[i], temp[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if path[nx][ny] == 0 or path[nx][ny] > temp[2] + 1:
                    path[nx][ny] = temp[2] + 1
                    bfs.append((nx, ny, temp[2]+1))


for i in range(N):
    for j in range(M):
        if path[i][j] == 1:
            bfs.append((i, j, 1))

search()

for i in path:
    if 0 in i:
        print(-1)
        quit()

print(shortest-1)