N = int(input())
if N == 1:
    print('*')
    quit()
if N % 2 == 0:
    for i in range(N):
        sign = ''
        sign += '*'
        if i == 0 or i == N-1:
            sign += '*' * (N-2)
        else:
            i -= 1
            if i < N // 2 - 1:
                sign += ' ' * i
                sign += '*'
                sign += ' ' * (N - i - 4 - i)
                sign += '*'
                sign += ' ' * i
            else:
                sign += ' ' * (N - i - 3)
                sign += '*'
                sign += ' ' * (N - (N - i - 2) - (N - i - 3) - 3)
                sign += '*'
                sign += ' ' * (N - i - 3)

        sign += '*'
        print(sign)

else:
    for i in range(N):
        sign = ''
        sign += '*'
        if i == 0 or i == N-1:
            sign += '*' * (N-2)
        else:
            i -= 1
            if i < N // 2 - 1:
                sign += ' ' * i
                sign += '*'
                sign += ' ' * (N - i - 4 - i)
                sign += '*'
                sign += ' ' * i
            elif i == N // 2 -1:
                sign += ' ' * i
                sign += '*'
                sign += ' ' * i
            else:
                sign += ' ' * (N - i - 3)
                sign += '*'
                sign += ' ' * (N - (N - i - 2) - (N - i - 3) - 3)
                sign += '*'
                sign += ' ' * (N - i - 3)

        sign += '*'


        print(sign)