import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
path = []
for j in range(H):
    temp = []
    for i in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))

    path.append(temp)

bfs = deque()
shortest = 0
dx, dy, dh = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

def search():
    global shortest
    while len(bfs) != 0:
        temp = bfs.popleft()
        shortest = max(temp[3], shortest)
        for i in range(6):
            nh, nx, ny = temp[0] + dh[i], temp[1] + dx[i], temp[2] + dy[i],

            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H:
                if path[nh][nx][ny] == 0 or path[nh][nx][ny] > temp[3] + 1:
                    path[nh][nx][ny] = temp[3] + 1
                    bfs.append((nh, nx, ny, temp[3]+1))

for h in range(H):
    for i in range(N):
        for j in range(M):
            if path[h][i][j] == 1:
                bfs.append((h, i, j, 1))

search()
for h in path:
    for i in h:
        if 0 in i:
            print(-1)
            quit()

print(shortest-1)