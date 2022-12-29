import sys

T = int(sys.stdin.readline())

arr = [1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline())
    n -= 1
    if n <= 2:
        print(arr[n])
        continue
    else:
        for i in range(n-2):
            if len(arr) > i+3:
                continue
            arr.append(arr[i]+arr[i+1]+arr[i+2])
        print(arr[n])
