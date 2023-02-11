import sys
import heapq

N, E = map(int, sys.stdin.readline().split())


def dijkstra(start):
    visited = [1e9 for i in range(N + 1)]
    visited[start] = 0
    heap = []
    heapq.heappush(heap, (start, 0))
    while heap:
        cur, cnt = heapq.heappop(heap)
        for next, cost in path[cur]:
            temp = cnt + cost
            if visited[next] > temp:
                visited[next] = temp
                heapq.heappush(heap, (next, temp))
    return visited

path = []
for _ in range(N + 1):
    path.append(list())

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    path[a].append((b, c))
    path[b].append((a, c))


v1, v2 = map(int, sys.stdin.readline().split())

d0 = dijkstra(1)
d1 = dijkstra(v1)
d2 = dijkstra(v2)
cnt = min(d0[v1] + d1[v2] + d2[N], d0[v2] + d2[v1] + d1[N])
print(cnt if cnt < 1e9 else -1)
