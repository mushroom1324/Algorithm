import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(C)

    ans = 1
    while len(C) > 1:
        temp = heapq.heappop(C) * heapq.heappop(C)
        ans *= temp
        heapq.heappush(C, temp)
    print(ans % 1_000_000_007)