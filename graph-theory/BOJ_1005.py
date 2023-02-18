import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    delay = list(map(int, sys.stdin.readline().split()))
    delay.insert(0, 0)
    path = [[] for _ in range(N+1)]
    checkStart = [0 for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        path[a].append(b)
        checkStart[b] += 1

    deq = deque()
    visited = delay[:]
    W = int(sys.stdin.readline())
    for i in range(1, N+1):
        if not checkStart[i]:
            deq.append(i)

    while deq:
        cur = deq.popleft()

        for target in path[cur]:
            checkStart[target] -= 1
            visited[target] = max(visited[target], visited[cur] + delay[target])
            if not checkStart[target]:
                deq.append(target)

    print(visited[W])
