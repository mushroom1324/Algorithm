import sys
from collections import deque

num, E, W, S, N = map(int, sys.stdin.readline().split())
p = [E, W, S, N]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0] * (num*2+1) for _ in range(num*2+1)]
answer = 0


def dfs(x, y, prob, cnt):
    global answer

    if cnt == num:
        answer += prob
        return
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < num*2+1 and 0 <= ny < num*2+1 and not visited[nx][ny]:
            dfs(nx, ny, prob * (p[i] / 100), cnt + 1)
            visited[nx][ny] = 0


dfs(num, num, 1, 0)

print(answer)