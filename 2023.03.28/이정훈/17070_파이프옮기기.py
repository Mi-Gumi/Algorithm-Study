def move(ci, cj, dr) :
    if ci == N-1 and cj == N-1 :
        return 1
    possible = 0
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
    
            if ndr == 0 :
                if memo[ni][nj][0] >= 0 and memo[ni][nj][1] >= 0 :
                    tmp = memo[ni][nj][0] + memo[ni][nj][1]
                else :
                    tmp = move(ni, nj, ndr )
            elif ndr == 1 :
                if memo[ni][nj][0] >= 0 and memo[ni][nj][1] >= 0 and memo[ni][nj][1] >= 0:
                    tmp = memo[ni][nj][0] + memo[ni][nj][1] + memo[ni][nj][2]
                else :
                    tmp = move(ni, nj, ndr )
            elif ndr == 2 :
                if memo[ni][nj][1] >= 0 and memo[ni][nj][1] >= 0:
                    tmp = memo[ni][nj][1] + memo[ni][nj][2]
                else :
                    tmp = move(ni, nj, ndr )
            
            memo[ni][nj][ndr] = tmp
            possible += tmp

    return possible

N = int(input())

state = [list(map(int,input().split())) for _ in range(N)]

d = ((0,1,((0,1)), 0), (1,1,((0,1),(1,0),(1,1)),1),(1,0,((1,0),)),2)
dr_d = {
    0 : ((0,1,((0,1),), 0), (1,1,((0,1),(1,0),(1,1)), 1)),
    1 : ((0,1,((0,1),), 0), (1,1,((0,1),(1,0),(1,1)), 1),(1,0,((1,0),), 2)),
    2 : ((1,1,((0,1),(1,0),(1,1)), 1),(1,0,((1,0),), 2)),
}

dr = 0
memo = [[[-1]*3]*N for _ in range(N)] 
state[0][0] = 2
state[0][1] = 2

head_i = 0
head_j = 1

ans = move(0,1,0)

print(ans)

