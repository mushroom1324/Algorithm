import sys
from collections import deque



def d(x):
    temp = str(int(x) * 2 % 10000)
    while len(temp) != 4:
        temp = '0' + temp
    return temp


def s(x):
    if int(x) - 1 < 0:
        return "9999"
    else:
        temp = str(int(x) - 1)
        while len(temp) != 4:
            temp = '0' + temp
        return temp


def l(x):
    return x[1] + x[2] + x[3] + x[0]


def r(x):
    return x[3] + x[0] + x[1] + x[2]


T = int(sys.stdin.readline())

for _ in range(T):

    deq = deque()
    visited = set()

    A, B = sys.stdin.readline().rstrip().split()
    if A == B:
        print(0)
        continue

    while len(A) != 4:
        A = '0' + A

    while len(B) != 4:
        B = '0' + B

    deq.append((A, ''))
    cur = str()

    while cur != B:
        temp = deq.popleft()
        cur, cnt = temp[0], temp[1]
        if cur in visited:
            continue
        visited.add(cur)

        d_result = d(cur)
        if d_result == B:
            print(cnt + 'D')
            break
        else:
            deq.append((d_result, cnt + 'D'))

        s_result = s(cur)
        if s_result == B:
            print(cnt + 'S')
            break
        else:
            deq.append((s_result, cnt + 'S'))

        l_result = l(cur)
        if l_result == B:
            print(cnt + 'L')
            break
        else:
            deq.append((l_result, cnt + 'L'))

        r_result = r(cur)
        if r_result == B:
            print(cnt + 'R')
            break
        else:
            deq.append((r_result, cnt + 'R'))

