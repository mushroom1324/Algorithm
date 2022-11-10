N, K = map(int, input().split())
bottles = list()
res = 0
curr = 1
while N > 0:
    val = divmod(N, 2)
    if val[1]:
        bottles.append(curr)
    curr *= 2
    N = val[0]

while len(bottles) > K:
    res += bottles[1] - bottles[0]
    bottles[1] *= 2
    del bottles[0]

print(res)

