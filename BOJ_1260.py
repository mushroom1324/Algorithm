import sys

# DFS
ansDFS = list()


def dfs(curr, val):
    if val in ansDFS:
        return
    ansDFS.append(val)
    for i in curr[1:]:
        dfs(edges[i-1], i)


# BFS
ansBFS = list()
queue = list()


def bfs(curr, val):
    if val in ansBFS:
        return
    ansBFS.append(val)

    for i in curr[1:]:
        queue.append(i)

    while len(queue) != 0:
        temp = queue.pop(0)
        bfs(edges[temp-1], temp)


N, M, V = map(int, sys.stdin.readline().split())
edges = list()
check = list()
for i in range(N):
    edges.append([0])

for i in range(M):
    first, second = map(int, sys.stdin.readline().split())
    edges[first-1].append(second)
    edges[second-1].append(first)

for i in edges:
    i.sort()

dfs(edges[V-1], V)
print(*ansDFS)
bfs(edges[V-1], V)
print(*ansBFS)