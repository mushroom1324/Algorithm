import sys
from collections import deque


TC = int(sys.stdin.readline())


def bellman(start, v):
    visited = [1e9 for _ in range(v + 1)]
    deq.append((start, 0, 0))
    visited[start] = 0

    while deq:
        cur, weight, cnt = deq.popleft()

        if cnt == v or visited[cur] < weight:
            continue

        for next_weight, next in path[cur]:
            temp = weight + next_weight
            if visited[next] > temp:
                visited[next] = temp
                deq.append((next, temp, cnt + 1))

    return visited


for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())

    path = [[] for _ in range(N + 1)]
    deq = deque()

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        path[S].append((T, E))
        path[E].append((T, S))

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        path[S].append((-T, E))

    isYes = False
    for each in range(1, 1 + N):

        if bellman(each, N)[each] < 0:
            isYes = True
            break
        else:
            continue
    if isYes:
        print("YES")
    else:
        print("NO")


"""

2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8


1
6 4 4
1 2 1
2 3 1
4 5 1
5 6 1
3 2 1
2 1 1
6 5 1
5 4 2


벨만포드 문제네요 ..
"""