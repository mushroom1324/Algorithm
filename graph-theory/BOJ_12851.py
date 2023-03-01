import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

visited = [1e9 for _ in range(max(A + 1, B + 2))]

cur = B
deq = deque()
ways = 0
ans = 1e9

deq.append((B, 0))
visited[B] = 0

while deq:
    cur, cnt = deq.popleft()

    if visited[cur] < cnt:
        continue
    visited[cur] = cnt

    if cur == A:
        if ans > cnt:
            ans = cnt
            ways = 1
        elif ans == cnt:
            ways += 1
        continue

    if cur < A:
        deq.append((A, cnt + A - cur))
        continue
    if cur % 2 == 0:  # when even number
        deq.append((cur - 1, cnt + 1))
        deq.append((cur // 2, cnt + 1))
    else:
        deq.append((cur + 1, cnt + 1))
        deq.append((cur - 1, cnt + 1))

print(ans)
print(ways)