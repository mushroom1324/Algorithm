import sys
import heapq

T = int(sys.stdin.readline())

heap = []

for i in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -N)