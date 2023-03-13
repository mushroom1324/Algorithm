import sys
import heapq

"""

dijkstra?
for i in range(N):
    




TLE : 

    10000 * 10000log(10000) .... XXXXXXXX
    
    트리의 지름 ?
    
    1. A -> 가장 먼 곳 
    2. 가장 먼 곳 -> 가장 먼 곳
     
    
"""

path = [[] for _ in range(10001)]
N = 0

while True:
    try:
        A, B, W = map(int, sys.stdin.readline().split())
        path[A].append((B, W))
        path[B].append((A, W))
        N = max(N, A, B)
    except:
        break
if N == 0:
    print(0)
    quit()
heap = []

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

    return visited[1:]

dp = dijkstra(1)
dp2 = dijkstra(dp.index(max(dp)) + 1)
print(max(dp2))
