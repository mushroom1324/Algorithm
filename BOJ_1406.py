import sys
string = sys.stdin.readline()
N = int(sys.stdin.readline())
stack = list()
for i in string[:len(string)-1]:
    stack.append(i)
temp = list()
for i in range(N):
    currInput = sys.stdin.readline().split()
    if currInput[0] == 'P':
        stack.append(currInput[1])
    elif currInput[0] == 'B':
        if len(stack) != 0:
            stack.pop()
    elif currInput[0] == 'L':
        if len(stack) != 0:
            temp.append(stack.pop())
    else:
        if len(temp) != 0:
            stack.append(temp.pop())

while len(temp) != 0:
    stack.append(temp.pop())

print(''.join(stack))

# index = len(string)-1
# for i in range(N):
#     currInput = sys.stdin.readline().split()
#     if currInput[0] == 'P':
#         string = string[:index] + currInput[1] + string[index:]
#         index += 1
#     elif currInput[0] == 'B':
#         if index != 0:
#             string = string[:index-1] + string[index:]
#             index -= 1
#     elif currInput[0] == 'L':
#         if index != 0:
#             index -= 1
#     else:
#         if index != len(string):
#             index += 1
# string = string.replace("\n", "")
#
# print(string)

# list = list(string)
# del list[len(list)-1]
#
# index = len(list)
# for i in range(N):
#     currInput = sys.stdin.readline().split()
#     if currInput[0] == 'P':
#         list.insert(index, currInput[1])
#         index += 1
#     elif currInput[0] == 'B':
#         if index == 0:
#             continue
#         else:
#             del list[index-1]
#             index -= 1
#     elif currInput[0] == 'L':
#         if index == 0:
#             continue
#         else:
#             index -= 1
#     else:
#         if index == len(list):
#             continue
#         else:
#             index += 1
#
# res = ''
# for i in list:
#     res += i
#
# print(res)
