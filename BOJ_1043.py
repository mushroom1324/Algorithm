import sys

N, M = map(int, sys.stdin.readline().split())

temp = list(map(int, sys.stdin.readline().split()))
num_know = temp[0]
know = set(temp[1:])
temp.clear()

party = []

for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    del temp[0]
    temp = set(temp)
    party.append(temp)

update = True
while update:
    update = False
    for i in party:
        if len(i & know) and len(i & know) != len(i):
            update = True
            know.update(i)

cnt = 0

for i in party:
    if not len(i & know):
        cnt += 1

print(cnt)