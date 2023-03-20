import sys

K, N = map(int, sys.stdin.readline().split())

lan = []

for _ in range(K):
    lan.append(int(sys.stdin.readline()))

low = 0
high = 2**32

while low < high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(K):
        cnt += lan[i] // mid

    if cnt < N:
        high = mid
    else:
        low = mid + 1

print(low - 1)

''''
4 11
804
743
457
539

'''