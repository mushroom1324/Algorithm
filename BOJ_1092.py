# Fucking easy bro fucking EASY

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
count = 0
crane.sort(reverse=True)
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
    quit()

index = 0
for i in crane:
    if i < box[M-1]:
        del crane[index]
    else:
        index += 1
while len(box) != 0:
    for c in crane:
        boxIndex = 0
        for b in box:
            if c >= b:
                del box[boxIndex]
                break
            else:
                boxIndex += 1
    count += 1

print(count)