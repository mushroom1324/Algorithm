import sys

N = int(sys.stdin.readline())

f2 = 3
f1 = 7
cur = 3
for i in range(N-2):
    cur = 2 * f1 + f2
    f2 = f1
    f1 = cur


print(cur % 9901) if N != 2 else print(7)

