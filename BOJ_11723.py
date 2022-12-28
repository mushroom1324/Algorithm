import sys

M = int(sys.stdin.readline())
nums = set()

for _ in range(M):
    command = list(sys.stdin.readline().rstrip().split())
    if len(command) == 1:
        if command[0] == 'all':
            nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        else:
            nums.clear()
    else:
        x = int(command[1])
        if command[0] == 'add':
            nums.add(x)
        elif command[0] == 'remove':
            nums.discard(x)
        elif command[0] == 'check':
            if x in nums:
                print(1)
            else:
                print(0)
        else:
            if x in nums:
                nums.discard(x)
            else:
                nums.add(x)
