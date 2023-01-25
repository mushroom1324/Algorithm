import sys
from collections import deque

"""
simple bfs
add highway if possible
add +1 always
--time complexity..
"""

N, D = map(int, sys.stdin.readline().split())

path = []


for _ in range(N):
    s, e, d = map(int, sys.stdin.readline().split())
    path.append((s, e, d))


deq = deque()
visited = [1e9 for _ in range(D+1)]
deq.append((0, 0))
while deq:
    pos, cost = deq.popleft()

    if pos > D or visited[pos] < cost:
        continue
    visited[pos] = cost


    for high in path:
        if high[0] == pos:
            deq.append((high[1], cost + high[2]))
    deq.append((pos+1, cost+1))

print(visited[D])