import sys

string = sys.stdin.readline().rstrip()
ex = sys.stdin.readline().rstrip()

lastChar = ex[-1]
stack = []
length = len(ex)

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == ex:
        del stack[-length:]

ans = ''.join(stack)

if ans == '':
    print("FRULA")
else:
    print(ans)

