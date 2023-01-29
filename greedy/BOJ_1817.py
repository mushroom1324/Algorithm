import sys

N, M = map(int, sys.stdin.readline().split())
if N == 0:
    print(0)
    quit()

books = list(map(int, sys.stdin.readline().split()))
ans = 1
temp = 0
for i in books:
    temp += i
    if temp > M:
        temp = i
        ans += 1

print(ans)