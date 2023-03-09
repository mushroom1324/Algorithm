import sys

"""

rate 

low = Y
high = 1_000_000_000
mid = (low + high) // 2

cur_rate = int((Y + mid / X + mid ) * 100)

"""


X, Y = map(int, sys.stdin.readline().split())
rate = (Y * 100) // X

ans = sys.maxsize
left = 1
right = X
while left <= right:
    mid = (left + right) // 2

    cur_rate = (Y + mid) * 100 // (X + mid)

    if cur_rate > rate:
        ans = min(mid, ans)
        right = mid - 1
    else:
        left = mid + 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)


