N, M = map(int, input().split())
res = 0

arr = list(map(int, input().split()))

positive = list()
negative = list()

for i in arr:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

#음수와 양수를 나눠서 처리
positive.sort(reverse=True)
negative.sort()

#마지막에는 돌아올 필요 없음 그부분 처리
if len(positive) != 0 and len(negative) != 0:
    if positive[0] > -negative[0]:
        res += positive[0]
        del positive[0:M]
    else:
        res += -negative[0]
        del negative[0:M]

elif len(positive) != 0:
    res += positive[0]
    del positive[0:M]
elif len(negative) != 0:
    res += -negative[0]
    del negative[0:M]
else:
    print("no input...")
    quit()



while len(positive) != 0 and len(negative) != 0:
    if positive[0] > -negative[0]:                                      # 양수의 절대값이 더 크면
        res += positive[0] * 2
        del positive[0:M]
    else:
        res += negative[0] * -2
        del negative[0:M]

while len(positive) != 0:
    res += positive[0] * 2
    del positive[0:M]

while len(negative) != 0:
    res += negative[0] * -2
    del negative[0:M]

print(res)




