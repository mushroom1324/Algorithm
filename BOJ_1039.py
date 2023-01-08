import sys
from collections import deque


N, K = sys.stdin.readline().rstrip().split()
N = list(N)
K = int(K)
length = len(N)

visited = []

# always have to change the biggest value to the top.
# but going with bfs bc the value is very short..

deq = deque()

deq.append((N[:], 0))
ans = []

while len(deq) != 0:
    temp = deq.popleft()
    val, cnt = temp[0], temp[1]
    if cnt == K:
        ans.append("".join(val))
        continue

    if ("".join(val), cnt) in visited:
        continue
    visited.append(("".join(val), cnt))

    for i in range(length):
        for j in range(length):
            temp = val[:]
            if i != j:
                temp[j], temp[i] = temp[i], temp[j]
                if temp[0] != '0':
                    deq.append((temp[:], cnt + 1))


if len(ans) == 0:
    print(-1)
else:
    print(max(ans))