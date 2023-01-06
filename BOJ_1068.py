import sys
from collections import deque

N = sys.stdin.readline()

temp = list(map(int, sys.stdin.readline().split()))

edges = []


for index, i in enumerate(temp):
    edges.append((i, index))

del edges[int(sys.stdin.readline())]

visited = []
deq = deque()
cnt = 0

for i in edges:
    if i[0] == -1:
        deq.append(i)

while len(deq):
    i = deq.popleft()
    if i in visited:
        continue
    visited.append(i)

    check = True
    for j in edges:
        if j[0] == i[1]:
            deq.append(j)
            check = False

    if check:
        cnt += 1

print(cnt)
