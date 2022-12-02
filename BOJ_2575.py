import sys

M = int(sys.stdin.readline())

if M == 1:
    print('1 1')
    quit()

ansA = 0
ansB = 0
bothB = 0
divM = divmod(M, 3)

if divM[1] == 0:
    ansA = divM[0]
else:
    ansA = divM[0] + 1

d = 2
while d == 2:
    if M % d == 0:
        ansB += 1
        bothB += 1
        M /= d
    else:
        d += 1

while d <= M:
    if M % d == 0:
        ansB += 1
        M /= d
    else:
        d += 1

ans = []
ans.append(ansA)
ans.append(ansB - bothB // 2)
print(*ans)
