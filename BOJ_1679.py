import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

deq = deque()
visited = dict()

for i in arr:
    deq.append((i, 1))

while deq:
    cur, cnt = deq.popleft()
    if cnt > K:
        continue
    if cur in visited and visited[cur] < cnt:
        continue
    visited[cur] = cnt
    for i in range(N):
        deq.append((cur + arr[i], cnt + 1))

index = 1
while index in visited:
    index += 1

if index % 2:
    print('jjaksoon win at', index)
else:
    print('holsoon win at', index)