import sys
from collections import deque

"""
good to go I guess.. 
LGTM
    >> failed 
"""

N, M = map(int, sys.stdin.readline().split())

path = []
deq = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    path.append(list(map(int, sys.stdin.readline().split())))


def bfs_air():
    deq.append((0, 0))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if path[nx][ny] == 0:
                    visited[nx][ny] = 1
                    deq.append((nx, ny))
                else:
                    path[nx][ny] += 1


def cheese_to_air():

    is_changed = False

    for i in range(N):
        for j in range(M):
            if path[i][j] >= 3:
                path[i][j] = 0
                is_changed = True
            elif path[i][j] == 2:
                path[i][j] = 1

    return is_changed


cnt = 0
while True:
    bfs_air()
    if not cheese_to_air():
        break
    cnt += 1

print(cnt)



"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 1 1 0 0
0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0


"""