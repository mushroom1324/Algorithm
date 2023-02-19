import sys
import heapq

heap = []

n, m, r = map(int, sys.stdin.readline().split())

item = list(map(int, sys.stdin.readline().split()))
item.insert(0, 0)

path = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    path[a].append((b, l))
    path[b].append((a, l))


def dijkstra(start):
    visited = [1e9 for _ in range(n + 1)]
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


ans = 0
for i in range(1, 1 + n):
    temp_ans = 0
    cur_visited = dijkstra(i)
    for j in range(1, 1 + n):
        if cur_visited[j] <= m:
            temp_ans += item[j]
    ans = max(ans, temp_ans)

print(ans)
