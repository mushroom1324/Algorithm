import sys

N = int(sys.stdin.readline())

arr = []
white = 0
blue = 0

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

def check(x, y, length):
    global white, blue
    flag = arr[x][y]
    for i in range(x, x+length):
        for j in range(y, y+length):
            if arr[i][j] != flag:
                check(x, y, length//2)
                check(x, y+length//2, length//2)
                check(x+length//2, y, length//2)
                check(x+length//2, y+length//2, length//2)
                return
    if flag == 0:
        white += 1
    else:
        blue += 1

check(0, 0, N)

print(white)
print(blue)