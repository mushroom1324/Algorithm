import sys


'''

문제
0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라. 

예를 들어 수열 1, 2, 2, 4, 4, 5, 7, 7, 2 의 경우에는 1 ≤ 2 ≤ 2 ≤ 4 ≤ 4 ≤ 5 ≤ 7 ≤ 7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다. 수열 4, 1, 3, 3, 2, 2, 9, 2, 3 의 경우에는 3 ≥ 3 ≥ 2 ≥ 2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다. 또 1, 5, 3, 6, 4, 7, 1, 3, 2, 9, 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.

입력
첫째 줄에는 수열의 길이 N이 주어지고, 둘째 줄에는 N개의 숫자가 빈칸을 사이에 두고 주어진다. N은 1 이상 100,000 이하의 정수이다.

출력
첫째 줄에 가장 긴 길이를 출력한다.


예제 입력 1 
9
1 2 2 4 4 5 7 7 2
예제 출력 1 
8
예제 입력 2 
9
4 1 3 3 2 2 9 2 3
예제 출력 2 
4
예제 입력 3 
11
1 5 3 6 4 7 1 3 2 9 5
예제 출력 3 
2

4 1 3 3 2 2 9 2 3
1 2 2 3 2 3 2 2 2 

-> 수열 반대방향 나오면 다시 이전으로 가면서 똑같은 수 처음으로 감 


'''

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if N <= 2:
    print(N)
    quit()

index = 1
prev = arr[0]
state = 0
dp = [2 for _ in range(N)]
dp[0] = 1
while index < N:
    cur = arr[index]
    if prev < cur:
        if state == 1:
            dp[index] = dp[index - 1] + 1
        else:
            temp_index = index - 2
            while arr[temp_index] == prev:
                dp[index] += 1
                temp_index -= 1
        state = 1
    elif prev > cur:
        if state == -1:
            dp[index] = dp[index - 1] + 1
        else:
            temp_index = index - 2
            while arr[temp_index] == prev:
                dp[index] += 1
                temp_index -= 1
        state = -1
    else:
        dp[index] = dp[index - 1] + 1

    prev = cur
    index += 1

print(max(dp))

