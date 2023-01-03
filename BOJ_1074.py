import sys

n, R, C = map(int, sys.stdin.readline().split())


ans = 0

N = pow(2, n)
H = N // 2


while True:
    if R <= 0 and C <= 0 or H <= 0:
        break
    if R >= H:
        ans += N * H
        R -= H
    if C >= H:
        ans += H * H
        C -= H

    N = H
    H = N // 2

res = (R, C)
if res == (0, 0):
    print(ans)
elif res == (0, 1):
    print(ans + 1)
elif res == (1, 0):
    print(ans + 2)
else:
    print(ans + 3)

