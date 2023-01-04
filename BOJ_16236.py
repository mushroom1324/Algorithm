import sys
from collections import deque

N = int(sys.stdin.readline())
path = []
visited = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    path.append(temp[:])
    visited.append(temp[:])

deq = deque()
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cur_size = 2
eaten = 0
ans = 0

for i in range(N):
    for j in range(N):
        if path[i][j] == 9:
            path[i][j] = 0
            deq.append((i, j, 1))
while True:
    food = []
    while len(deq) != 0:
        temp = deq.popleft()
        x, y, cnt = temp[0], temp[1], temp[2]
        if visited[x][y] < 0:
            continue
        visited[x][y] = -cnt

        # handle when found
        if 0 < path[x][y] < cur_size:
            food.append((x, y))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and path[nx][ny] <= cur_size:
                deq.append((nx, ny, cnt + 1))

    ################ end of while ###############

    if len(food) == 0:
        break
    shortest = [food[0][0], food[0][1]]
    cur = -visited[food[0][0]][food[0][1]]
    for i in food[1:]:
        x, y = i[0], i[1]
        if -visited[x][y] < cur:
            cur = -visited[x][y]
        elif -visited[x][y] == cur:
            if x < shortest[0]:
                shortest[0] = x
                shortest[1] = y
            elif x == shortest[0] and y < shortest[1]:
                shortest[1] = y

    x, y = shortest[0], shortest[1]
    path[x][y] = 0
    deq.clear()
    deq.append((x, y, 1))
    ans += -visited[x][y] - 1

    for i in range(N):
        for j in range(N):
            visited[i][j] = 0

    eaten += 1
    if cur_size == eaten:
        cur_size += 1
        eaten = 0

print(ans)