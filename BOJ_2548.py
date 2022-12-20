import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
sums = []
for i in arr:
    sum = 0
    for j in arr:
        sum += abs(i - j)
    sums.append((sum, i))
sums.sort()
print(sums[0][1])