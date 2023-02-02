"""

DP but we should consider memory size
    1. using dict(): A[0] = 1
        save when the value has to be changed : use prev
            p_last, q_last to indicate last indexes : initial value to 0

            if i // P != p_last:
                p_last = cur
            if i // Q != q_last:
                q_last = cur

            cur = A[p_last] + A[q_last]

            if prev != cur:
                A[i] = cur
            prev = cur




            case 7 2 3)
                A[1]:
                    cur = A[0] + A[0] = 2
                        prev(1) != cur(2):
                            A[1] = cur
                A[2]:
                    i // P != p_last ( 1 != 0 )
                    p_last = 1
                    cur = A[1] + A[0] = 3
                        prev(2) != cur(3):
                            A[2] = cur



"""
import sys
N, P, Q = map(int, sys.stdin.readline().split())


def dfs(cur):
    if cur not in A:
        A[cur] = dfs(cur // P) + dfs(cur // Q)
    return A[cur]


A = dict({0: 1})
print(dfs(N))
