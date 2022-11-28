import sys
ans = 0
N = int(sys.stdin.readline())
nums = list()
for i in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort(reverse=True)

prev = nums[0]
pair = True
nonpair = list()
zero = False
minus = list()

if len(nums) == 1:
    print(nums[0])
    quit()

for i in nums[1:]:
    if i > 1:
        if pair:
            ans += prev * i
        pair = not pair
    else:
        if pair:
            if prev == 0:
                zero = True
            elif prev < 0:
                minus.append(prev)
            else:
                nonpair.append(prev)
            pair = False
        if i == 1:
            nonpair.append(i)
        elif i == 0:
            zero = True
        else:
            minus.append(i)
    prev = i
if pair:
    nonpair.append(prev)
pair = True
minus.sort()
if len(minus) > 1:
    prev = minus[0]
    for i in minus[1:]:
        if pair:
            ans += prev * i
        pair = not pair
        prev = i
    if pair:
        if not zero:
            ans += i

if len(minus) == 1:
    if not zero:
        ans += minus[0]

for i in nonpair:
    ans += i

print(ans)