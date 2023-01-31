import sys
from collections import deque

N, S, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
deq = deque()
visited = [-1 for _ in range(M+1)]

visited[S] = 0

for index, num in enumerate(arr):
    for i in range(M+1):

        if visited[i] == index:

            if i + num <= M:
                deq.append(i + num)
            if i - num >= 0:
                deq.append(i - num)

    while deq:
        temp = deq.pop()
        visited[temp] = index + 1


for i in range(M+1):
    if visited[M - i] == N:
        print(M-i)
        quit()
print(-1)
