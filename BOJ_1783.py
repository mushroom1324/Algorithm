import sys
N, M = map(int, sys.stdin.readline().split())

if N >= 3 and M >= 7:
    print(M - 2)
else:
    if N == 1:
        print(1)
    elif N == 2:
        print(min(4, ((M-1) // 2) + 1))
    else:
        print(min(4, M))


