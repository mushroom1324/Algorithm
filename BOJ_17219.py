import sys

N, M = map(int, sys.stdin.readline().split())

site = dict()

for _ in range(N):
    key, val = sys.stdin.readline().rstrip().split()
    site[key] = val


for _ in range(M):
    print(site[sys.stdin.readline().rstrip()])