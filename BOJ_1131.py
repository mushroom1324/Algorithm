import sys

"""
A ~ B 에 대해 반복
함수 S()를 구현


각각의 수열에 대해서 visited에 있는 값이면 break


"""


A, B, K = map(int, sys.stdin.readline().split())


def s(num):
    result = 0
    while num:
        result += (num % 10) ** K
        num = num // 10
    return result


ans = 0
for i in range(A, B+1):
    visited = [i]

    temp = s(i)
    while temp not in visited:
        visited.append(temp)
        temp = s(temp)
    ans += min(visited)

print(ans)