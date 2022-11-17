import sys
T = int(sys.stdin.readline())

count = [(1, 0), (0, 1)]
N = list()
for i in range(T):
    N.append(int(sys.stdin.readline()))

for N in N:
    if N < len(count):
        print(count[N][0], count[N][1])
    else:
        for l in range(N+1):
            if l < len(count):
                continue
            else:
                count.append((count[l-1][0] + count[l-2][0], count[l-1][1] + count[l-2][1]))
        print(count[N][0], count[N][1])


