

N,M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
V = [[0]*M for _ in range(N)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
V[r][c] = 1
cnt = 1
flag = 1
while flag:
    for k in range(4):
        ni = r + di[d]
        nj = c + dj[d]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and V[ni][nj] == 0:
            V[ni][nj] = 1
            r, c = ni, nj
            cnt += 1
            break
        
        elif k == 3 and  (0 > ni or nj >= N or 0 > nj or nj >= M or arr[ni][nj] != 0):
            d = (d+2)%4 
            ni = r + di[d]
            nj = c + dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                r,c = ni,nj
                d = (d+2)%4

            else:
                flag = 0
                break
        else:
            d = (d+3)%4

print(cnt)
                

                





