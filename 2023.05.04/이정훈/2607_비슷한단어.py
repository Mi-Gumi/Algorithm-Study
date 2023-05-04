n = int(input())

first = list(input())
ans = 0
for _ in range(n-1) :
    compare = first[:]
    word = input()
    cnt = 0
    for c in word :
        if c in compare :
            compare.remove(c)
        else :
            cnt += 1
    # 남아 있는 문자개수가 0 or 1 또는 없는 문자가 0 or 1
    if cnt < 2 and len(compare) < 2 :
        ans += 1
print(ans)

