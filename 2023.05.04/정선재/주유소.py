from collections import deque

n = int(input())
ins = deque(list(map(int, input().split())))
val = deque(list(map(int, input().split())))
min_val = min(val)
ans = 0
now_min = 10**9
if val[0] == min_val:
    ans = val[0] * sum(ins)
else:
    for i in range(len(ins)):
        if now_min > val[i]:
            now_min = val[i]
            ans += now_min * ins[i]
        elif now_min <= val[i]:
            ans += now_min * ins[i]

print(ans)