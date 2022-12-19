import sys
N, R, C = map(int, sys.stdin.readline().split())

if (R + C) % 2 == 1:
    row = False
    for n in range(N):
        carr = row
        col = ''
        for m in range(N):
            if carr:
                col += 'v'
            else:
                col += '.'
            carr = not carr
        print(col)
        row = not row

if (R + C) % 2 == 0:
    row = True
    for n in range(N):
        carr = row
        col = ''
        for m in range(N):
            if carr:
                col += 'v'
            else:
                col += '.'
            carr = not carr
        print(col)
        row = not row
