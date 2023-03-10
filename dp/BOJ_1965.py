"""
1, 5, 2, 3, 7

i)

1 -> 5
1, 5

ii)
1 -> 5, 2
1 -> 2, 5
1, 5, 2

iii)
1 -> 5, 2 -> 3
1 -> 5, 2, 3




1. 좌 -> 우로 검사
2. 넣을 수 있다면, 넣는 경우와 넣지 않는 경우를 저장함
----- XXXXXXXX -----
1, 5, 2, 3, 7

i)

    7 -> 3
    7

ii)

    7 -> 3 -> 2
    7 -> 2 (숫자가 작거나 같고 카운트가 작다 -> 버림)
    7

iii)

    7 -> 3 -> 2
    7 -> 5

iv)

    7 -> 3 -> 2 -> 1
    7 -> 5 -> 1 (숫자가 작거나 같고 카운트가 작다 -> 버림)

1. 우 -> 좌로 검사
2. 숫자가 작거나 같고 카운트가 작으면 버린다
3. 숫자가 크면 dp에 저장해둔다


dp = 2차원 배열
1차원 : 박스의 인덱스
2차원 : 박스의 크기

->
    1, 5, 2, 3, 7

    i)
        7   dp[i][7]
        -   dp[i][1000]

    ii)
        7 -> 3  dp[i][3] // dp[i][3:]중 가장 큰 수를 가져옴 -> max(dp[i][3:])
        7       dp[i][7]
        -       dp[i][1000]

    iii)
        7 -> 3 -> 2 dp[i][2]
        7 -> 2      dp[i][2] // 이미 3이 있음, 버림
        7           dp[i][7]
        -           dp[i][1000]

    iiii)
        7 -> 3 -> 2 dp[i][2] // 3
        7 -> 5      dp[i][5] // 2
        7           dp[i][7] // 1
        -           dp[i][7] // 0
=======XXXXXXX========



"""


import sys

N = int(sys.stdin.readline())

boxes = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))