import sys

N, M = map(int, sys.stdin.readline().split())

edge = []
visited = []
cnt = 0

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    edge.append((A, B))

if M == 0:
    print(N)
    quit()

def dfs(A, B):
    global cnt
    if A in visited and B in visited:
        return
    elif A in visited:
        visited.append(B)
        curr = B
    elif B in visited:
        visited.append(A)
        curr = A
    else:
        cnt += 1
        visited.append(A)
        visited.append(B)
        for i in edge:
            if A in i or B in i:
                dfs(i[0], i[1])
        return

    for i in edge:
        if curr in i:
            dfs(i[0], i[1])

for i in edge:
    dfs(i[0], i[1])

for i in range(N):
    if i+1 not in visited:
        cnt += 1

print(cnt)