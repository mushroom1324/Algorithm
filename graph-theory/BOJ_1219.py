import sys
from collections import deque

N, N_S, N_E, M = map(int, sys.stdin.readline().split())


path = [[] for _ in range(N)]
for _ in range(M):
    C_S, C_E, C_W = map(int, sys.stdin.readline().split())

    path[C_S].append((C_E, C_W))

earn = list(map(int, sys.stdin.readline().split()))



visited = [[1e9 for _ in range(N)] for _ in range(2 * N + 1)]

#  1
for k in range(2 * N + 1):
    visited[k][N_S] = -earn[N_S]
for each_node, each_weight in path[N_S]:
    temp = min(visited[0][each_node], each_weight - earn[each_node])
    for k in range(2 * N + 1):
        visited[k][each_node] = temp

#  2
for i in range(N+1):
    for j in range(N):
        if visited[i][j] != 1e9:
            for each_node, each_weight in path[j]:
                temp = min(visited[i][each_node], visited[i][j] + each_weight - earn[each_node])
                for k in range(i, 2 * N + 1):
                    visited[k][each_node] = temp
'''
아 모르겠다 ~
'''

if visited[N-1][N_E] == 1e9:
    print("gg")
    quit()


for i in range(N):
   if visited[N-1][i] != visited[N][i]:
        for k in range(N, 2 * N + 1):
            visited[k][i] = -1e10


for i in range(N, 2 * N):
    for j in range(N):
        if visited[i][j] != 1e9:
            for each_node, each_weight in path[j]:
                temp = min(visited[i][each_node], visited[i][j] + each_weight - earn[each_node])
                for k in range(i, 2 * N + 1):
                    visited[k][each_node] = temp




if visited[2 * N - 1][N_E] <= -1e9:
    print("Gee")
    quit()
else:
    print(-visited[N - 1][N_E])
    quit()
#
# if visited[N-1][N_E] != visited[N][N_E]:
#     if visited[N-1][N_E] > visited[N][N_E]:
#         print("Gee")
#         quit()
#     else:
#         print(-visited[N - 1][N_E])

print(-visited[N-1][N_E])



'''
1. visit possible nodes from N_S and save them to visited[0]
2. update visited with visited, possible nodes from visited[0]
3. repeat until visited[N]

check cycle:
    if visited[N][N_E] != visited[N - 1][N_E]:
        print "Gee" or "gg" according to that..

3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000


4 1 3 4 
0 1 0 
0 1 100000 
1 2 3 
2 3 4 
2 2 2 2
'''


