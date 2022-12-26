N, M = map(int, input().split())
poke = dict()
pokel = list()

index = 0
for i in range(N):
    temp = input()
    poke[temp] = index
    pokel.append(temp)
    index += 1

for i in range(M):
    command = input()
    temp = command.isnumeric()
    if temp:
        print(pokel[int(command)-1])
    else:
        print(poke[command]+1)