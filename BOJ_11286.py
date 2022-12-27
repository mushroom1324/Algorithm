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
            temp = heapq.heappop(heap)
            print(temp[0] * temp[1])
    else:
        if N < 0:
            heapq.heappush(heap, (-N, -1))
        else:
            heapq.heappush(heap, (N, 1))
