import sys

N = int(sys.stdin.readline())

ans = 0

for i in range(1, N + 1):
    temp = list(map(int, str(i)))
    if i < 100:
        ans += 1
    elif temp[0] - temp[1] == temp[1] - temp[2]:
        ans += 1

print(ans)