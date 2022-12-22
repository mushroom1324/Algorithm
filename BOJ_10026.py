import sys
from collections import deque

N = int(sys.stdin.readline())
pic = []
visited = []
deq = deque()

cnt = 0
for i in range(N):
    pic.append(sys.stdin.readline())

def visit(x, y):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and pic[nx][ny] == pic[x][y]:
            deq.append((nx, ny))

def bfs(x, y):
    if (x, y) in visited:
        return

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and pic[nx][ny] == pic[x][y]:
            deq.append((nx, ny))

    while len(deq) != 0:
        temp = deq.popleft()
        if temp not in visited:
            visited.append(temp)
            visit(temp[0], temp[1])


for i in range(N):
    for j in range(N):
        if (i, j) in visited:
            continue
        cnt += 1
        bfs(i, j)

visited.clear()
cnt2 = 0

for i in range(N):
    for j in range(N):
        if pic[i][j] == 'G':
            pic[i] = list(pic[i])
            pic[i][j] = 'R'
            pic[i] = ''.join(pic[i])

for i in range(N):
    for j in range(N):
        if (i, j) in visited:
            continue
        cnt2 += 1
        bfs(i, j)

print(cnt, cnt2)

# def findpath(x, y):
#     if (x, y) in visited:
#         return
#     visited.append((x, y))
#     for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N and pic[nx][ny] == pic[x][y]:
#             findpath(nx, ny)
#
# for i in range(N):
#     for j in range(N):
#         if (i, j) in visited:
#             continue
#         cnt += 1
#         findpath(i, j)
#
# visited.clear()
# cnt2 = 0
#
# for i in range(N):
#     for j in range(N):
#         if pic[i][j] == 'G':
#             pic[i] = list(pic[i])
#             pic[i][j] = 'R'
#             pic[i] = ''.join(pic[i])
#
# for i in range(N):
#     for j in range(N):
#         if (i, j) in visited:
#             continue
#         cnt2 += 1
#         findpath(i, j)
#
# print(cnt, cnt2)