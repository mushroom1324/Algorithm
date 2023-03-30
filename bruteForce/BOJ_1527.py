import sys
from collections import deque, defaultdict

A, B = map(int, sys.stdin.readline().split())

deq = deque()

deq.append(4)
deq.append(7)

visited = defaultdict(int)
cnt = 0

while deq:
    cur = deq.popleft()

    if cur <= B and visited[cur] == 0:
        if A <= cur:
            cnt += 1

        visited[cur] = 1

        deq.append(cur * 10 + 4)
        deq.append(cur * 10 + 7)


print(cnt)
