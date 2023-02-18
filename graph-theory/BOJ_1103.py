"""
using bfs
**edit: hard to use bfs: hard to check cycle

initialize visited with 0s.
do if cur_cnt is bigger than visited[cur].
else continue.
    
make a function to move x times with four directions.
**edit: no need to make function.. just multiply dist into dx, dy.

initialize answer variable to check max count(include going off the grid).
"""

# ================= first implementation ================= #
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

path = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    path.append([int(x) for x in sys.stdin.readline().rstrip()])

deq = deque()
deq.append((0, 0, 0))
visited = [[0 for _ in range(N)] for _ in range(M)]
ans = 0
while deq:
    x, y, cnt = deq.popleft()

    visited[x-1][y-1] = cnt

    distance = path[x-1][y-1]
    for i in range(4):
        nx, ny = x + dx[i] * distance, y + dy[i] * distance
    ...
"""

"""
problem : hard to check cycle.

using dfs.

problem : need to clear visited every time.
    size not big ( 50 * 50 ) so imma just stick with this plan..
    
we will be using backtracking


def dfs(cur):
    if visited, print -1 and quit.
    for directions:
        if not off the grid or path[next][next] is not 'H':
            visited[cur][cur] = 1
            dfs(next, next, cnt + 1)
            visited[cur][cur] = 0
        else:
            save to ans if cnt is bigger than ans

"""

# ================= second implementation ================= #
import sys
N, M = map(int, sys.stdin.readline().split())

path = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    path.append(list(sys.stdin.readline().rstrip()))

visited = [[0 for _ in range(M)] for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

ans = 0


def dfs(x, y, cnt):
    global ans
    if visited[x][y]:
        print(-1)
        quit()

    distance = int(path[x][y])
    for i in range(4):
        nx, ny = x + dx[i] * distance, y + dy[i] * distance
        if 0 <= nx < N and 0 <= ny < M and path[nx][ny] != 'H' and dp[nx][ny] < cnt:
            dp[nx][ny] = cnt
            visited[x][y] = 1
            dfs(nx, ny, cnt + 1)
            visited[x][y] = 0
        else:
            ans = max(ans, cnt)

dfs(0, 0, 0)
print(ans + 1)

"""
problem: too slow
solve: use dp

"""