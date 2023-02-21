import sys
from collections import deque

"""
ready to go!
LGTM
"""

deq = deque()
n, m = map(int, sys.stdin.readline().split())

visited = [1e9 for _ in range(100001)]

deq.append((n, 0))

while deq:
    cur, cnt = deq.popleft()

    # check when n >= m, in this case cnt + n - m is the only way to go ..
    # can prevent worst case of 100000 0..
    if cur >= m:
        if visited[m] > cnt + cur - m:
            visited[m] = cnt + cur - m
            continue

    if visited[cur] <= cnt:
        continue
    visited[cur] = cnt

    if cur - 1 > 0:
        deq.append((cur - 1, cnt + 1))

    if cur + 1 <= 100_000:
        deq.append((cur + 1, cnt + 1))

    if cur * 2 <= 100_000:
        deq.appendleft((cur * 2, cnt))

print(visited[m])

"""
5 17
>>2

5 201

maybe we should start from endpoint ...

##make a logic for when n < m!!!!##
    when n < m, only way to go is cur - 1..
"""

