import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
ans = tuple(sorted(nums))
deq = deque()
visited = dict()

deq.append((nums[:], 0))

while len(deq) != 0:
    nums, cnt = deq.popleft()
    if tuple(nums) in visited:
        continue
    visited[tuple(nums)] = cnt

    for i in range(N-K+1):
        temp = nums[:]
        for j in range(K//2):
            temp[i+j], temp[i+K-1-j] = temp[i+K-1-j], temp[i+j]
        deq.append((temp[:], cnt+1))

if ans in visited:
    print(visited[ans])
else:
    print(-1)