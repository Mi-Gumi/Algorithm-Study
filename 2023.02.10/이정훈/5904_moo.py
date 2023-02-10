def moo(length, m, target):
    nextlen = (length - m) // 2

    if target <= nextlen:
        return moo(nextlen, m - 1, target)
    if nextlen <= target <= nextlen + m:
        if target - nextlen == 1:
            return 'm'
        else:
            return 'o'
    else:
        return moo(nextlen, m - 1, target - (nextlen + m))


N = int(input())

num = 3
M = 3

while num < N:
    M += 1
    num = num * 2 + M

ans = moo(num, M, N)
print(ans)