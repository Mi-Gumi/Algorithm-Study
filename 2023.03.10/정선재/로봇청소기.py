import sys
input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
V = [[0]*M for _ in range(N)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
V[r][c] = 1
cnt = 1

while 1:
    flag = 0
    for k in range(4):
        ni = r + di[(d+3)%4]
        nj = c + dj[(d+3)%4]
        d = (d+3)%4
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and V[ni][nj] != 1:
            V[ni][nj] = 1
            r, c = ni, nj
            cnt += 1
            flag = 1
            break
    
    if flag == 0: 
        if arr[r-di[d]][c-dj[d]] == 1: 
            print(cnt)
            break
        else:
            r,c = r-di[d],c-dj[d]
