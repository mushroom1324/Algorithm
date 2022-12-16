import sys

L, R = sys.stdin.readline().split()


if len(L) != len(R):
    print(0)
    quit()

ans = 0
index = 0
while index != len(L):
    if L[index] < R[index]:
        break
    if L[index] == '8' and R[index] == '8':
        ans += 1
    index += 1

print(ans)