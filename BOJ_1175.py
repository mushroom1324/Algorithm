import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
path = []
start = []


def bfs(start):
    deq = deque(start)
    visited = [[[1 for _ in range(M)] for _ in range(N)] for _ in range(4)]
    check_c = 0
    check_deq = deque()
    while deq:
        x, y, direction, cnt = deq.popleft()
        for index, (px, py) in enumerate(zip(dx, dy)):
            if index == direction:
                continue
            nx, ny = x + px, y + py
            if 0 <= nx < N and 0 <= ny < M and path[nx][ny] != '#' and visited[index][nx][ny]:
                if path[nx][ny] == 'C':
                    if not check_deq:
                        check_c += 1
                        if check_c == 2:
                            return cnt + 1
                    elif check_deq[0][0] != nx or check_deq[0][1] != ny:
                        continue
                    check_deq.append((nx, ny, index, cnt+1))
                else:
                    if check_deq:
                        continue
                    visited[index][nx][ny] -= 1
                    deq.append((nx, ny, index, cnt+1))
        if not deq and check_deq:
            visited = [[[1 for _ in range(M)] for _ in range(N)] for _ in range(4)]
            path[check_deq[0][0]][check_deq[0][1]] = '.'
            while check_deq:
                deq.append(check_deq.pop())
    return -1


for i in range(N):
    temp = list(sys.stdin.readline()[:-1])
    if not start and 'S' in temp:
        start.append((i, temp.index('S'), -1, 0))
    path.append(temp)
print(bfs(start))
