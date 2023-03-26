import sys

N, M = map(int, sys.stdin.readline().split())

chess = []

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    temp_list = []
    for each in temp:
        if each == 'W':
            temp_list.append(1)
        else:
            temp_list.append(0)
    chess.append(temp_list)


def check(n, m):
    case1 = 0
    case2 = 0
    cur = False

    for i in range(8):

        cur = not cur  # True for 'W' and False for 'B'
        line = cur
        for j in range(8):
            if chess[n + i][m + j] == line:
                case2 += 1
            else:
                case1 += 1

            line = not line

    return min(case1, case2)


ans = 1e9
for n in range(N - 7):
    for m in range(M - 7):
        ans = min(ans, check(n, m))

print(ans)