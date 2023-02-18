import sys
from collections import deque

N = int(sys.stdin.readline())

cost = list(map(int, sys.stdin.readline().split()))
cost.insert(0, 0)

path = []
for _ in range(N):
    temp = list(map(int, list(sys.stdin.readline().rstrip())))
    temp.insert(0, 0)
    path.append(temp)

path.insert(0, 0)

stack = deque()
visited = [0 for _ in range(N+1)]


def dfs(cur):
    visited[cur] = 1
    for each in range(1, 1 + N):
        if path[cur][each] == 1 and visited[each] == 0:
            stack.append(each)
            dfs(each)
    stack.append(cur)


def reversed_dfs(cur):
    visited[cur] = 0
    scc.append(cur)
    for each in range(1, 1 + N):
        if path[each][cur] == 1 and visited[each] == 1:
            reversed_dfs(each)


ans = 0

for i in range(1, 1 + N):
    if visited[i] == 0:
        dfs(i)

while stack:
    min_cost = 1e9
    scc = []
    temp = stack.pop()
    if visited[temp] == 1:
        reversed_dfs(temp)
        for i in scc:
            min_cost = min(min_cost, cost[i])
        ans += min_cost

print(ans)
"""

5
1 1 1 1 1
00000
10000
01000
00100
00010


5
1 1 1 1 1
00001
10000
01000
00100
00010


4
1 2 3 4
0100
0011
1000
0100

4
1 2 3 4
0100
0011
0100
1000

5
1 2 3 4 5
00000
00000
00000
00000
00000


6
1 1 1 1 1 1
001000
001000
000011
010000
001001
000100


6
1 1 3 2 1 5
000100
100000
000011
010000
001100
111111

"""