import sys
from collections import Counter
N = int(sys.stdin.readline())
skyline = list()
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    tup = (A, B)
    tup = list(tup)
    skyline.append(tup)
count = 0
index = 1

# 사실 지금 생각해보니 튜플로 저장할 필요가 없음
# x좌표는 어차피 순서대로 입력돼서 필요 없는데 왜 저장했지
# 아무튼 바꾸기 귀찮으니까 걍 커밋함
for i in skyline:
    if i[1] == 0:
        index += 1
        continue
    if i == skyline[N - 1]:
        count += 1
        break
    for n in skyline[index:]:
        if i[1] > n[1]:
            count += 1
            break
        elif i[1] == n[1]:
            n[1] = 0
        if n == skyline[N-1]:
            count += 1
    index += 1

print(count)