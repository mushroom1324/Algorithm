import sys
sys.setrecursionlimit(10001)


V, E = map(int, sys.stdin.readline().split())

edge = [[] for _ in range(E + 1)]
reversed_edge = [[] for _ in range(E + 1)]
for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    edge[A].append(B)
    reversed_edge[B].append(A)

visited = [False for _ in range(V+1)]
stack = []
each = []


def dfs(cur):
    visited[cur] = True
    for next in edge[cur]:
        if not visited[next]:
            stack.append(next)
            dfs(next)
    stack.append(cur)


def reversed_dfs(cur):
    visited[cur] = False
    scc.append(cur)
    for next in reversed_edge[cur]:
        if visited[next]:
            reversed_dfs(next)


for i in range(1, 1 + V):
    if not visited[i]:
        dfs(i)

while stack:
    scc = []
    cur = stack.pop()
    if visited[cur]:
        reversed_dfs(cur)
        if scc:
            each.append(sorted(scc))

each.sort()
print(len(each))
for i in each:
    print(*i, -1)


# 11 16
# 1 4
# 4 5
# 5 6
# 6 7
# 7 5
# 4 6
# 1 3
# 3 2
# 2 8
# 8 10
# 10 11
# 11 8
# 8 9
# 9 5
# 2 1
# 9 10


# 11 17
# 1 4
# 4 5
# 5 6
# 6 7
# 7 5
# 4 6
# 1 3
# 3 2
# 2 8
# 8 10
# 10 11
# 11 10
# 10 8
# 8 9
# 9 5
# 2 1
# 9 11