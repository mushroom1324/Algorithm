import sys

N, M = map(int, sys.stdin.readline().split())

path = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]


def flip(a, b):
    for i in range(a + 1):
        for j in range(b + 1):
            path[i][j] ^= 1


cnt = 0

for row in range(N - 1, -1, -1):
    for col in range(M - 1, -1, -1):
        if path[row][col]:
            cnt += 1
            flip(row, col)

print(cnt)
