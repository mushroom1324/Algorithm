# 이렇게 푸는거 아닌 것 같은데 내일 확인할게요 ..
CONST = 65

N = input()
arr = [0] * 65

for i in N:
    arr[ord(i)-CONST] += 1

odd = 0
for i in arr:
    if i % 2 == 1:
        odd += 1


code = ''
index = 0
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    for i in arr:
        if i != 0:
            for i in range(i//2):
                code += chr(CONST + index)
        index += 1
    index = 64
    for i in reversed(arr):
        if i != 0:
            for i in range(i//2):
                code += chr(CONST + index)
        index -= 1
    index = 0
    for i in arr:
        if i % 2 == 1:
            temp = list(code)
            temp.insert(len(temp)//2, chr(CONST+index))
            code = ''.join(temp)
        index += 1

print(code)

