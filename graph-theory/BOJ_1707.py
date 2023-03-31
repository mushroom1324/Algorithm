import sys
from collections import deque

T = int(sys.stdin.readline())


def bfs(index):

    deq.append((index, 1))

    while deq:
        cur, color = deq.popleft()

        if visited[cur] != 0:
            if visited[cur] * color == -1:
                return 0
            continue

        visited[cur] = color

        for each in path[cur]:
            deq.append((each, color * -1))

    return 1


for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    deq = deque()

    path = [[] for _ in range(V + 1)]

    for _ in range(E):
        A, B = map(int, sys.stdin.readline().split())

        path[A].append(B)
        path[B].append(A)

    visited = [0 for _ in range(V + 1)]

    ans = 1
    for i in range(1, 1 + V):
        if not visited[i]:
            if not bfs(i):
                ans = 0
                break

    print("YES") if ans else print("NO")


"""
2
3 3
1 2
2 3
3 1
3 3
1 2
2 3
3 1


1
4 3
1 3
2 4
3 4

1       
4 4
1 3
3 4
2 4
1 4

1
3 2
2 1
3 2

"""