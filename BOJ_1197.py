import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

root = []
edges = []

for i in range(V):
    root.append(-1)


for _ in range(E):
    A, B, w = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (w, A, B))


def find_parent(N):
    while root[N-1] != -1:
        N = root[N-1]
    return N


num_of_edges = 0
ans = 0

while num_of_edges < V-1:
    temp = heapq.heappop(edges)
    w, A, B = temp[0], temp[1], temp[2]

    v1 = find_parent(temp[1])
    v2 = find_parent(temp[2])

    if v1 != v2:
        num_of_edges += 1
        ans += w
        if v1 < v2:
            root[v1 - 1] = v2
        else:
            root[v2 - 1] = v1

print(ans)
