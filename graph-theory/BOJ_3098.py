import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [[] for _ in range(N + 1)]
temp = [[] for _ in range(N + 1)]
ans = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    visited[A].append(B)
    visited[B].append(A)


def visit(each):
    return visited[each]

cnt = 0
while True:
    ans.append(0)
    for i in range(1, 1 + N):
        for each in visited[i]:
            v = visit(each)
            for t in v:
                temp[i].append(t)

    for i in range(1, 1 + N):
        while temp[i]:
            t = temp[i].pop()
            if t not in visited[i] and t != i:
                visited[i].append(t)
                ans[len(ans)-1] += 1
    cnt += 1
    isThatIt = True
    for i in range(1, 1 + N):
        if len(visited[i]) != N-1:
            isThatIt = False
    if isThatIt:
        break
print(cnt)
for each in ans:
    print(each // 2)
"""

1. 각각의 노드에 있는 value에 해당하는 노드들을 방문() 
2. 방문()해서 그 안에 있는 value들을 어미 노드에 추가




"""