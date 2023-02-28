import sys
from collections import deque, defaultdict

A, B = map(int ,sys.stdin.readline().split())
deq = deque()

deq.append((A, 1))

bool_dict = defaultdict(bool)
ans = 1e9
while deq:
    cur, cnt = deq.popleft()

    if cur == B:
        ans = min(ans, cnt)
        continue

    if bool_dict[cur]:
        continue
    bool_dict[cur] = True

    if cur * 2 <= B:
        deq.append((cur * 2, cnt + 1))
    if cur * 10 + 1 <= B:
        deq.append((cur * 10 + 1, cnt + 1))

if ans == 1e9:
    print(-1)
else:
    print(ans)