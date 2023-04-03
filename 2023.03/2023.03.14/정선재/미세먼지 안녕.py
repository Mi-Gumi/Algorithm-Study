import sys
input = sys.stdin.readline

def dust():
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    V = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C): 
            if arr[i][j] !=0 and arr[i][j] != -1:
                cnt = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C:
                        if arr[ni][nj] != -1:
                            V[ni][nj] += arr[i][j]//5
                            cnt += arr[i][j]//5
                
                arr[i][j] -= cnt
    
    for i in range(R):
        for j in range(C):

                arr[i][j] += V[i][j]
    
   

def fr_con():
    di = [0,-1,0,1]
    dj = [1,0,-1,0]
    d = [0]
    flag = 1
    i = fr
    j = 0
    idx = 0
    while flag:
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] == -1:
                flag = 0
                return 
            else:
                d.append(arr[ni][nj])
                arr[ni][nj] = d.pop(0)
                i, j = ni,nj
        if 0 > ni or ni >= R or 0 > nj or nj>= C:
            idx += 1
               

def se_con():
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    d = [0]
    flag = 1
    i = se
    j = 0
    idx = 0
    while flag:
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] == -1:
                flag = 0
                return
            else:
                d.append(arr[ni][nj])
                arr[ni][nj] = d.pop(0)
                i, j = ni,nj
        if 0 > ni or ni >= R or 0 > nj or nj >= C:
            idx += 1
        

R,C,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

fr = 0
se = 0
di = [0,1,0,-1]
dj = [1,0,-1,0]
for i in range(R):
    if arr[i][0] == -1:
        fr = i
        se = i + 1
        break


for i in range(T):
    dust()
    fr_con()
    se_con()

dust_cnt = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != -1:
            dust_cnt += arr[i][j] 
    
    
print(dust_cnt)