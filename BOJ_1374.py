import sys
N = int(sys.stdin.readline())
lec = list()
for i in range(N):
    num, start, finish = map(int, sys.stdin.readline().split())
    lec.append([start, finish])

lec.sort()

temp = [lec[0][1]]

index = 1
minStart = temp[0]
while index < len(lec):
    if lec[index][0] < minStart:
        temp.append(lec[index][1])
        if minStart > lec[index][1]:
            minStart = lec[index][1]
    else:
        temp.sort()
        temp[0] = lec[index][1]
        if len(temp) == 1:
            minStart = temp[0]
        else:
            minStart = temp[1]

    index += 1

print(len(temp))