

'''

dx = [1, 1, -1, -1, 2, -2, 2, -2]
dy = [2, -2, 2, -2, 1, 1, -1, -1]

path = []

for _ in range(N):
    path.append(sys...)

visited = [[0 for _ in range(M)] for _ in range(N)]

bfs():



    while True:
        x, y = popleft()
        
        handleVisit()
    
    
        for i in range(8):
            nx, ny = ...
            
            if path:
                deq.append()
    
    


'''
"""
dx = [1, 1, -1, -1, 2, -2, 2, -2]
dy = [2, -2, 2, -2, 1, 1, -1, -1]

path = []

N, M = map(int, sys.stdin.readline().split())


for i in range(N):
    temp = sys.stdin.readline().rstrip()
    temp_arr = []
    for j, each in enumerate(temp):
        if each == '.':
            temp_arr.append(0)
        else:
            temp_arr.append(int(each))

    path.append(temp_arr)

deq = deque()


def bfs(x, y, c):
    deq.append((x, y, 0))
    visited = [[1e9 for _ in range(M)] for _ in range(N)]

    while deq:
        x, y, cnt = deq.popleft()
        cur_cnt = math.ceil(cnt / c)
        if visited[x][y] < cur_cnt:
            continue
        visited[x][y] = cur_cnt

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                deq.append((nx, ny, cnt + 1))

    return visited

chesses = []

for i in range(N):
    for j in range(M):
        if path[i][j] != 0:
            chesses.append(bfs(i, j, path[i][j]))

ans = 1e9

for i in range(N):
    for j in range(M):
        temp = 0
        for each in range(len(chesses)):
            temp += chesses[each][i][j]

        ans = min(temp, ans)


print(ans) if ans != 1e9 else print(-1)
"""

"""

MLE FUCKING HATE YOU 

sol)
    maybe I have to go top-down

"""
import sys, math
from collections import deque
dx = [1, 1, -1, -1, 2, -2, 2, -2]
dy = [2, -2, 2, -2, 1, 1, -1, -1]

path = []

N, M = map(int, sys.stdin.readline().split())


for i in range(N):
    temp = sys.stdin.readline().rstrip()
    temp_arr = []
    for j, each in enumerate(temp):
        if each == '.':
            temp_arr.append(0)
        else:
            temp_arr.append(int(each))

    path.append(temp_arr)

deq = deque()


def bfs(x, y):
    deq.append((x, y, 0))
    visited = [[1e9 for _ in range(M)] for _ in range(N)]

    while deq:
        x, y, cnt = deq.popleft()

        if visited[x][y] <= cnt:
            continue
        visited[x][y] = cnt

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                deq.append((nx, ny, cnt + 1))

    temp = 0
    for i in range(N):
        for j in range(M):
            if path[i][j] != 0:
                temp += math.ceil(visited[i][j] / path[i][j])
    return temp

ans = 1e9
for i in range(N):
    for j in range(M):
        t = bfs(i, j)
        if t >= 1e8:
            continue
        else:
            ans = min(ans, t)

print(ans) if ans <= 1e8 else print(-1)

"""
10 10
..........
..........
..........
..........
..........
........11
..........
..........
..........
..........


아니 틀린게 없는데 ..

"""