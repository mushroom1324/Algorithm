N = int(input())
meetings = list()
for i in range(N):
    meetings.append(tuple(map(int, input().split())))

meetings.sort()
count = 0
index = 0
currentMin = 0
if N == 1:
    print(1)
    quit()


while True:
    if index == 0:
        currentMin = meetings[index][1]
        index += 1
        continue
    if index > len(meetings)-1:
        break
    if meetings[index][0] >= currentMin:            # 꼬리보다 대가리가 크다 = 이미 넘어갔다
        count += 1                                  # 카운트 더하고
        currentMin = meetings[index][1]             # 현재 꼬리로 바꿔준다
    else:
        if meetings[index][1] >= currentMin:        # 최소 꼬리보다 현재 꼬리가 더 크면
            index += 1                              # 패스
            continue
        else:
            currentMin = meetings[index][1]         # 최소 꼬리보다 현재 꼬리가 더 짧으면 바꿔준다
    index += 1

print(count + 1)
