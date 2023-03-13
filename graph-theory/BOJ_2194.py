import sys
from collections import deque

'''

N, M, A, B, 

N, M = map

A, B = unit

K : obstacles

for _ in range(K):
    input()

s_x, s_y

e_x, e_y

pivot point를 가장 좌측 상단으로 잡는다

cur_x, cur_y = 

방향에 따라 이동 방향의 면만 검사
ex) A, B = 100, 100
S_X, S_Y = 0, 0일 때,

우측으로 이동 : 
    for _ in range(X):
        ny = y + 1 
'''

N, M, A, B, K = map(int, sys.stdin.readline().split())
path = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    path[X][Y] = 1

for each in path:
    print(*each)

S_X, S_Y = map(int, sys.stdin.readline().split())
E_X, E_Y = map(int, sys.stdin.readline().split())

deq = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

deq.append((S_X, S_Y))
visited = [[0 for _ in range(N)] for _ in range(M)]

while deq:
    x, y = deq.popleft()

    if visited[x][y] or path[x][y]:
        continue