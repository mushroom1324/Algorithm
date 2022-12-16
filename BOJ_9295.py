import sys

T = int(sys.stdin.readline())
ans = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    ans.append(A+B)
for i in range(T):
    print('Case '+ str(i+1)+ ': '+ str(ans[i]))
