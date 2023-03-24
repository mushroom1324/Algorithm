import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())

deq = deque()

ans = set()


def bfs(a, b, c):
    visited = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]
    deq.append((a, b, c))

    while deq:
        cur_a, cur_b, cur_c = deq.popleft()
        if visited[cur_a][cur_b][cur_c]:
            continue
        visited[cur_a][cur_b][cur_c] = 1

        if cur_a == 0:
            ans.add(cur_c)

        if cur_c + cur_a <= A:
            deq.append((cur_c + cur_a, cur_b, 0))
        else:
            deq.append((A, cur_b, cur_c + cur_a - A))

        if cur_c + cur_a <= C:
            deq.append((0, cur_b, cur_c + cur_a))
        else:
            deq.append((cur_c + cur_a - C, cur_b, C))


        if cur_b + cur_a <= A:
            deq.append((cur_a + cur_b, 0, cur_c))
        else:
            deq.append((A, cur_b + cur_a - A, cur_c))

        if cur_b + cur_a <= B:
            deq.append((0, cur_a + cur_b, cur_c))
        else:
            deq.append((cur_b + cur_a - B, B, cur_c))


        if cur_b + cur_c <= B:
            deq.append((cur_a, cur_b + cur_c, 0))
        else:
            deq.append((cur_a, B, cur_b + cur_c - B))


        if cur_b + cur_a <= C:
            deq.append((cur_a, 0, cur_b + cur_c))
        else:
            deq.append((cur_a, cur_b + cur_c - C, C))


bfs(0, 0, C)
ans = list(ans)
ans.sort()
print(*ans)