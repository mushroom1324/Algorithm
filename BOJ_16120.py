import sys
PPAP = list(sys.stdin.readline().split('AP'))

extraPs = 0
PinLast = 0
if len(PPAP[len(PPAP)-1]) > 1:
    if len(PPAP[len(PPAP)-1]) > 2:
        print('NP')
        quit()
    for i in PPAP[len(PPAP)-1]:
        if i == 'A':
            print('NP')
            quit()
        else:
            PinLast = 1

for i in PPAP[0]:
    if 'A' in i:
        print('NP')
        quit()

for i in range(len(PPAP)-1):
    extraPs += len(PPAP[i]) - 2
    if extraPs < 0:
        print('NP')
        quit()
    extraPs += 1
extraPs += PinLast
if extraPs > 1:
    print('NP')
else:
    print('PPAP')

# AAAP