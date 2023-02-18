import sys
import heapq

"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""

V, E = map(int, sys.stdin.readline().split())

S = int(sys.stdin.readline())

path = [[] for _ in range(V + 1)]
visited = [1e9 for _ in range(V + 1)]
heap = []


def dijkstra(start):
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        weight, cur = heapq.heappop(heap)

        if visited[cur] < weight:
            continue

        for next, next_weight in path[cur]:
            temp = weight + next_weight
            if visited[next] > temp:
                visited[next] = temp
                heapq.heappush(heap, (temp, next))


for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    path[a].append((b, c))

dijkstra(S)

for i in range(1,V+1):
    print("INF" if visited[i] == 1e9 else visited[i])

