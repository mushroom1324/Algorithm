import sys

N, L, W, H = map(int, sys.stdin.readline().split())
start, end = 0, max(L, W, H)

for _ in range(10000):
    M = (start + end) / 2
    cnt = (L // M) * (W // M) * (H // M)
    if cnt >= N:
        start = M
    else:
        end = M

print(end)