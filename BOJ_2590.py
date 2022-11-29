import sys
size = list()
ans = 0
for i in range(6):
    size.append(int(sys.stdin.readline()))

ans += size[5]
size[5] = 0

ans += size[4]
for l in range(size[4]):
    size[0] = max(0, size[0] - 11)
size[4] = 0

ans += size[3]
for l in range(size[3]):
    twos = max(0, size[1] - 5)
    size[0] = max(0, size[0] - (5 - (size[1] - twos)) * 4)
    size[1] = twos
size[3] = 0

ans += size[2]//4
if size[2] % 4 == 1:
    ans += 1
    twos = max(0, size[1] - 5)
    size[0] = max(0, size[0] - (5 - (size[1] - twos)) * 4 - 7)
    size[1] = twos
elif  size[2] % 4 == 2:
    ans += 1
    twos = max(0, size[1] - 3)
    size[0] = max(0, size[0] - (3 - (size[1] - twos)) * 4 - 6)
    size[1] = twos
elif size[2] % 4 == 3:
    ans += 1
    twos = max(0, size[1] - 1)
    size[0] = max(0, size[0] - (1 - (size[1] - twos)) * 4 - 5)
    size[1] = twos
size[2] = 0

ans += size[1] // 9
if size[1] % 9 != 0:
    ans += 1
    size[0] = max(0, size[0] - ((9 - size[1]%9) * 4))
size[1] = 0

ans += size[0] // 36
if size[0] % 36 != 0:
    ans += 1

print(ans)