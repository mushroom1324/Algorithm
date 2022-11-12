N, L = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()
minL = hole[0]
diff = 0
count = 0
for i in hole:
    diff = i - minL
    if diff >= L:
        count += 1
        minL = i
count += 1
print(count)

