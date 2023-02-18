import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

path = [[] for _ in range(N + 1)]
heap = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    path[a].append((b, c))


S, E = map(int, sys.stdin.readline().split())


def dijkstra(start):
    visited = [1e9 for _ in range(N + 1)]
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

    return visited

print(dijkstra(S)[E])
