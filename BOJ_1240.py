import sys
from collections import deque


def bfs(a, target):
   deq = deque()
   deq.append((a, 0))
   visited = [False] * (N+1)
   visited[a] = True

   while len(deq) != 0:
      cur, cnt = deq.popleft()

      if cur == target:
         return cnt

      for i, w in nodes[cur]:
         if not visited[i]:
            deq.append((i, cnt + w))
            visited[i] = True


N, M = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
   a, b, w = map(int, sys.stdin.readline().split())
   nodes[a].append((b, w))
   nodes[b].append((a, w))


for _ in range(M):
   a, b = map(int, sys.stdin.readline().split())
   print(bfs(a, b))



