import sys
global size, level

N = int(sys.stdin.readline())

friend = []

for i in range(N):
    friend.append(sys.stdin.readline())



prev = 0
curr = 0

for each in friend:
    queue = []
    visited = []
    cnt = 0
    index = 0
    while index != N:
        if each[index] == 'Y':
            queue.append(index)
            visited.append(index)
            cnt += 1
        index += 1

    while len(queue) != 0:
        temp = queue.pop(0)
        index = 0
        while index != N:
            if index == curr:
                index += 1
                continue
            if index in visited:
                index += 1
                continue
            if friend[temp][index] == 'Y':
                visited.append(index)
                cnt += 1
            index += 1
    curr += 1
    prev = max(prev, cnt)

print(prev)
