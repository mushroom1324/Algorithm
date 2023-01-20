import sys
from collections import deque

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)
a, b = map(int, sys.stdin.readline().split())
visited = [-1] * (N+1)
deq = deque()

deq.append((a, 0))
while deq:
    cur, cnt = deq.popleft()

    if -1 < visited[cur] <= cnt:
        continue
    visited[cur] = cnt

    index = 1
    while cur + index <= N:
        if not index % arr[cur]:
            deq.append((cur+index, cnt+1))
        index += 1

    index = -1
    while cur + index > 0:
        if not -index % arr[cur]:
            deq.append((cur+index, cnt+1))
        index -= 1

print(visited[b])