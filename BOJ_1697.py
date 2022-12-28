import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

deq = deque()
visited = [-1] * 100001

deq.append((N, 0))

while len(deq) != 0:
    temp = deq.popleft()
    cur, cnt = temp[0], temp[1]
    if not 0 <= cur <= 100000:
        continue
    if visited[cur] == -1 or visited[cur] > cnt:
        visited[cur] = cnt
    else:
        continue
    deq.append((cur+1, cnt+1))
    deq.append((cur-1, cnt+1))
    deq.append((cur*2, cnt+1))

print(visited[K])
