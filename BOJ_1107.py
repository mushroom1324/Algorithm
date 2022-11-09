N = int(input())
M = int(input())


if M == 0:
    print(min(abs(100-N), len(str(N))))
    quit()

broken = list(map(int, input().split()))

minNum = abs(N - 100)


for i in range(1000000):
    temp = str(i)
    for n in range(len(temp)):
        if int(temp[n]) in broken:
            break
        elif n >= len(temp)-1:
            currNum = abs(N - i) + len(temp)
            if minNum > currNum:
                minNum = currNum

print(minNum)