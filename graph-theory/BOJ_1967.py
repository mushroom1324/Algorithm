import sys
from collections import deque

"""

12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

BFS/DFS to find distance and save them to value[] : we use BFS.
    >> value[] should also save to path -> to find common(a, b)
    
radius(v1, v2) = value(v1) + value(v2) - 2 * value(common(v1, v2))
    >> FAILED bc of time limit ... should be 10000C2 -> way over the time
    

1. BFS to find distance.
2. choose max(BFS_result)
3. BFS(max(BFS_result))
4. max(BFS(max(BFS_result))) = ans
"""

N = int(sys.stdin.readline())

path = []
visited = [-1 for _ in range(N + 1)]
deq = deque()


for _ in range(N+1):
    path.append(list())

for _ in range(N-1):
    a, b, w = map(int, sys.stdin.readline().split())
    path[a].append((b, w))
    path[b].append((a, w))


def bfs(start):
    deq.append((start, 0))

    while deq:
        cur, weight = deq.popleft()
        visited[cur] = weight

        for each, next_weight in path[cur]:
            if visited[each] == -1:
                deq.append((each, weight + next_weight))

bfs(1)

v1 = visited.index(max(visited))
print(v1)
visited = [-1 for _ in range(N + 1)]
bfs(v1)
print(max(visited))

# max_temp = max(visited)
# max_indexes = []
# for i in range(1, 1 + N):
#     if max_temp == visited[i]:
#         max_indexes.append(i)
# ans = []
# for each in max_indexes:
#     visited = [-1 for _ in range(N + 1)]
#     bfs(each)
#     ans.append(max(visited))

# print(max(ans))


"""
7
1 2 1
1 3 1
2 4 100
2 5 50
3 6 1
3 7 100


"""