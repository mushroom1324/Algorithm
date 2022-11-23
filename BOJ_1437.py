import sys
N = int(sys.stdin.readline())

res = 1
mod = N % 3

if N < 3:
    print(N)
    quit()

if mod == 0:
    for i in range(N // 3):
        res = (3 * res) % 10007
    print(res)
elif mod == 1:
    for i in range(N // 3 - 1):
        res = (3 * res) % 10007
    print((4 * res) % 10007)
elif mod == 2:
    for i in range(N // 3):
        res = (3 * res) % 10007
    print((2 * res )% 10007)