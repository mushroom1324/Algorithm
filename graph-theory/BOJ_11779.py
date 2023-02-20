import sys
import heapq


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
path = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    path[a].append((b, c))

S, E = map(int, input().split())

nearnest = [S] * (N + 1)
distance = [1e9] * (N + 1)

heap = [(0, S)]
while heap:
    dist, now = heapq.heappop(heap)
    if dist > distance[now]:
        continue

    for next, nextDist in path[now]:
        cost = nextDist + dist
        if cost < distance[next]:
            distance[next], nearnest[next] = cost, now
            heapq.heappush(heap, (cost, next))

ans = []
temp = E
while temp != S:
    ans.append(str(temp))
    temp = nearnest[temp]

ans.append(str(S))
ans.reverse()

print(distance[E])
print(len(ans))
print(" ".join(ans))