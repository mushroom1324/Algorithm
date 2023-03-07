import sys

N = int(sys.stdin.readline())
arr = list(map(int ,sys.stdin.readline().split()))

max_val = -1e9
prev = 0

for index, each in enumerate(arr):
    added = prev + each
    max_val = max(max_val, added, each)
    prev = max(added, each)

print(max_val)

"""

    1. max
    2. added == prev + cur 
    3. cur == each 
    4. prev
    
"""