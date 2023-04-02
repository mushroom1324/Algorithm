import sys
from collections import deque, defaultdict

D, S = sys.stdin.readline().split()
D = int(D)

words = []

for _ in range(D):
    words.append(sys.stdin.readline().rstrip())

deq = deque()

deq.append(S)

max = 0
ans = ''
visited = defaultdict(int)

while deq:
    cur = deq.popleft()

    if visited[cur] == 1:
        continue
    visited[cur] = 1

    if max < len(cur):
        max = len(cur)
        ans = cur

    for target in filter(lambda u: len(u) == len(cur) + 1, words):
        for i in range(len(target)):
            temp = target[:i] + target[i+1:]
            if temp == cur:
                deq.append(target)
print(ans)