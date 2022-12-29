import sys

N = int(sys.stdin.readline())

coords = list(map(int, sys.stdin.readline().split()))

temp = set()

for i in coords:
    temp.add(i)

temp = list(temp)
temp.sort()

temp_dict = dict()

for i in range(len(temp)):
    temp_dict[temp[i]] = i

for i in range(N):
    coords[i] = temp_dict[coords[i]]

print(*coords)