import sys
from collections import deque
N = int(sys.stdin.readline())

path = [0]
build_time = [0 for _ in range(N + 1)]
level = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
deq = deque()

for i in range(1, 1 + N):
    temp = list(map(int, sys.stdin.readline().split()))
    build_time[i] = temp[0]
    path.append(temp[1:-1])
    level[i] = len(temp[1:-1])
    if level[i] == 0:
        dp[i] = build_time[i]
        deq.append(i)

while deq:
    cur = deq.popleft()
    for i in range(1, 1 + N):
        if cur in path[i]:
            level[i] -= 1
            if level[i] == 0:
                max_build_time = 0
                for each in path[i]:
                    max_build_time = max(max_build_time, build_time[each])
                build_time[i] += max_build_time
                deq.append(i)

for i in build_time[1:]:
    print(i)


# 4
# 100 -1
# 10 1 -1
# 10 -1
# 10 1 3  -1