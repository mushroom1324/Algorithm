import heapq
from collections import defaultdict

T = int(input())

for _ in range(T):
    maxheap = []
    minheap = []
    count = defaultdict(int)
    k = int(input())
    for _ in range(k):
        command, temp = input().split()
        num = int(temp)
        if command == 'I':
            heapq.heappush(maxheap, -num)
            heapq.heappush(minheap, num)
            count[num] += 1
        else:
            if num == 1:
                # delete max
                if len(maxheap) == 0:
                    minheap.clear()
                    continue
                temp = -heapq.heappop(maxheap)
                count[temp] -= 1

                while count[temp] == -1:
                    count[temp] = 0
                    if len(maxheap) == 0:
                        minheap.clear()
                        break
                    temp = -heapq.heappop(maxheap)
                    count[temp] -= 1

            else:
                # delete min
                if len(minheap) == 0:
                    maxheap.clear()
                    continue
                temp = heapq.heappop(minheap)
                count[temp] -= 1

                while count[temp] == -1:
                    count[temp] = 0
                    if len(minheap) == 0:
                        maxheap.clear()
                        break
                    temp = heapq.heappop(minheap)
                    count[temp] -= 1

    result = []
    for i in minheap:
        if count[i] > 0:
            result.append(i)

    result.sort()
    if len(result) == 0:
        print("EMPTY")
    else:
        print(result[len(result)-1], result[0])

# 1
# 4
# I 40
# I 40
# D 1
# D -1

# 1
# 9
# I 36
# I 37
# I 38
# D 1
# D 1
# I 39
# I 40
# D -1
# D -1