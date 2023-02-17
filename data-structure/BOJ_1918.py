import sys

eq = sys.stdin.readline().rstrip()

stack = []
ans = ""

op = dict()
op['+'] = 1
op['-'] = 1
op['*'] = 2
op['/'] = 2
op['('] = 0
op[')'] = 10


for each in eq:
    if each == '*' or each == '/' or each == '+' or each == '-':
        if stack:
            top = stack[len(stack)-1]
            if op[each] > op[top]:
                stack.append(each)
            else:
                while stack:
                    top = stack[len(stack)-1]
                    if op[each] > op[top]:
                        break
                    else:
                        ans += stack.pop()
                stack.append(each)

        else:
            stack.append(each)

    elif each == '(':
        stack.append(each)
    elif each == ')':
        while stack:
            top = stack.pop()
            if top == '(':
                break
            else:
                ans += top

    else:
        ans += each

while stack:
    ans += stack.pop()

print(ans)