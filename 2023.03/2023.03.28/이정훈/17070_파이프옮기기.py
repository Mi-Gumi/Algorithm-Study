def move(ci, cj, dr) :
    if ci == N-1 and cj == N-1 :
        return 1
    memo[ci][cj][dr] = 0
    for di, dj, chk, ndr in dr_d[dr] :
        for chk_i, chk_j in chk :
            nchk_i = ci + chk_i
            nchk_j = cj + chk_j
            if nchk_i < N and nchk_j < N and state[nchk_i][nchk_j] == 0 :
                pass
            else :
                break
        else :
            ni, nj = ci + di , cj + dj
            if memo[ni][nj][ndr] >= 0 :
                tmp = memo[ni][nj][ndr]
            else :
                tmp = move(ni,nj,ndr)
            memo[ci][cj][dr] += tmp

    return memo[ci][cj][dr]

N = int(input())

state = [list(map(int,input().split())) for _ in range(N)]

dr_d = {
    0 : ((0,1,((0,1),), 0), (1,1,((0,1),(1,0),(1,1)), 1)),
    1 : ((0,1,((0,1),), 0), (1,1,((0,1),(1,0),(1,1)), 1),(1,0,((1,0),), 2)),
    2 : ((1,1,((0,1),(1,0),(1,1)), 1),(1,0,((1,0),), 2)),
}

dr = 0
memo = [[[-1]*3 for _ in range(N)] for _ in range(N)] 

ans = move(0,1,0)

print(ans)

