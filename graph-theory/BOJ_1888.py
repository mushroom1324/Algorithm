import sys
from collections import deque

'''



M, N 

dx, dy = 

bfs(x, y):

    cnt = path[x][y]
    
    visit()
    
    for j in range(cnt):
        for i in range(4):
            nx, ny = x + dx[i] * j, y + dy[i] * j
            
            traverse()

    
def check():
    # normal bfs

while True:
    for i in range(N):
        for j in range(M):
            if not visited:
                bfs()
                
    check()

'''


N, M = map(int, sys.stdin.readline().split())

path = []

for _ in range(N):
    path.append(list(map(int, list(sys.stdin.readline().rstrip()))))


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

deq = deque()


# def bfs(x, y):
#     deq.append((x, y))
#     while deq:
#         x, y = deq.popleft()
#         speed = path[x][y]
#
#         if visited[x][y] == 1:
#             continue
#         visited[x][y] = 1
#
#         for j in range(speed):
#             for i in range(8):
#                 nx, ny = x + dx[i] * j, y + dy[i] * j
#
#                 if 0 <= nx < N and 0 <= ny < M and path[nx][ny]:
#                     deq.append((nx, ny))

def check(x, y):
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        if visited[x][y]:
            continue
        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and path[nx][ny]:
                deq.append((nx, ny))


visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if path[i][j] and not visited[i][j]:
            cnt += 1
            check(i, j)

if cnt < 2:
    print(0)
    quit()


ans = 0
while True:
    ans += 1

    sub_deq = deque()


    for i in range(N):
        for j in range(M):
            if path[i][j]:
                for temp_i in range(2 * path[i][j] + 1):
                    for temp_j in range(2 * path[i][j] + 1):
                        ni, nj = i + temp_i - path[i][j], j + temp_j - path[i][j]
                        if 0 <= ni < N and 0 <= nj < M:
                            sub_deq.append((ni, nj, path[i][j]))

    while sub_deq:
        x, y, speed = sub_deq.popleft()
        if path[x][y] < speed:
            path[x][y] = speed

    visited = [[0 for _ in range(M)] for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if path[i][j] and not visited[i][j]:
                cnt += 1
                check(i, j)

    if cnt < 2:
        break

print(ans)