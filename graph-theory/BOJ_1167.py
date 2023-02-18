import sys
from collections import deque

V = int(sys.stdin.readline())

path = []
deq = deque()

for _ in range(V + 1):
    path.append(list())

for _ in range(V):
    temp = list(map(int, sys.stdin.readline().split()))

    next = 0
    checkPair = False
    for each in temp[1:-1]:
        if checkPair:
            path[temp[0]].append((next, each))
        else:
            next = each
        checkPair = not checkPair


def bfs(start):
    deq.append((start, 0))
    visited = [-1 for _ in range(V + 1)]

    while deq:
        cur, weight = deq.popleft()
        visited[cur] = weight

        for next, next_weight in path[cur]:
            if visited[next] == -1:
                deq.append((next, weight + next_weight))

    return visited

v1 = bfs(1)
v2 = bfs(v1.index(max(v1)))

print(max(v2))