import sys
T = int(sys.stdin.readline())
cnt = 0
ans = []


# dfs
def dfs(y, x):
    arr[y][x] = 0
    if y + 1 < N:
        if arr[y+1][x] == 1:
            dfs(y+1, x)
    if y - 1 >= 0:
        if arr[y-1][x] == 1:
            dfs(y-1, x)
    if x + 1 < M:
        if arr[y][x+1] == 1:
            dfs(y, x+1)
    if x - 1 >= 0:
        if arr[y][x-1] == 1:
            dfs(y, x-1)




for i in range(T):
    N, M, K = map(int, sys.stdin.readline().split())

    arr = [[0 for j in range(M)] for i in range(N)]

    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        arr[X][Y] = 1

    for n in range(N):
        for m in range(M):
            if arr[n][m] == 1:
                cnt += 1
                dfs(n, m)

    ans.append(cnt)
    cnt = 0
for i in ans:
    print(i)
