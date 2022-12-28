import sys
N, M = map(int, sys.stdin.readline().split())

g1 = set()
g2 = set()

for _ in range(N):
    g1.add(sys.stdin.readline().rstrip())

for _ in range(M):
    g2.add(sys.stdin.readline().rstrip())


ans = list(g1 & g2)

ans.sort()
print(len(ans))
for i in ans:
    print(i)