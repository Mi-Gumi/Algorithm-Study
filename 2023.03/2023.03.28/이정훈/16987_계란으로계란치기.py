def eggtoegg(now, cnt) :
    if now == N-1 :
        return cnt
    tmp_dura = eggs[now][0]

    for i in range(now+1, N) :
        pass



    return eggtoegg(now+1, cnt)

N = int(input())

eggs = []
for _ in range(N) :
    dura , w = map(int,input().split())
    eggs.append((dura, W))


hand = 0
