N, M = map(int, input().split())

mat = list()
ans = list()

for i in range(N):
    temp = input()
    row = list()
    for t in temp:
        row.append(int(t))
    mat.append(row)

for i in range(N):
    temp = input()
    row = list()
    for t in temp:
        row.append(int(t))
    ans.append(row)


row = 0
col = 0

if N < 3 or M < 3:
    for col in range(N):
        for row in range(M):
            if mat[col][row] != ans[col][row]:
                print(-1)
                quit()
    print(0)
    quit()

count = 0

while True:
    if col > N-1 or row > M-1:
        print(-1)
        quit()
    if mat[col][row] != ans[col][row]:
        if col+3 > N or row+3 > M:
            print(-1)
            quit()
        else:
            count += 1
            for c in range(3):
                for e in range(3):
                    if mat[col+c][row+e] == 0:
                        mat[col+c][row+e] = 1
                    else:
                        mat[col+c][row+e] = 0


    if row+3 > M:
        col += 1
        row = 0
    elif col+3 > N:
        for i in range(N):
            for l in range(M):
                if mat[i][l] != ans[i][l]:
                    print(-1)
                    quit()
        print(count)
        quit()
    else:
        row += 1