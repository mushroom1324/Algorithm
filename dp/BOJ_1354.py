import sys

N, P, Q, X, Y = map(int, sys.stdin.readline().split())

A = dict()
A[0] = 1


def dfs(cur):
    if cur not in A:
        A[cur] = dfs(max(0, cur//P-X)) + dfs(max(0, cur//Q-Y))
    return A[cur]


print(dfs(N))