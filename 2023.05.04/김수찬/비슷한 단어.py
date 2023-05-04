N = int(input())
first = list(input())

lst = [list(input()) for _ in range(N-1)]

def check(target,compare):
    T = target[:]
    cnt = 0
    for c in compare:
        if c in T:
            T.remove(c)
        else:
            cnt += 1
    
    return 1 if cnt < 2 and len(T) < 2 else 0

ans = 0
for i in range(N-1):
    compare_item = lst[i]

    ans += check(first,compare_item)
print(ans)