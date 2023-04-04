from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    
    v = [[0]*m for _ in range(n)]   
    for i in range(len(air)):
        arr[air[i][0]][air[i][0]] = 9
        v[air[i][0]][air[i][1]] = 1
    
    while air:
        i,j = air.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and v[ni][nj] != 1:
                air.append((ni,nj))
                v[ni][nj] = 1
                arr[ni][nj] = 9 


    


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

di = [1,0,-1,0]
dj = [0,1,0,-1]
cheeze_list = []
time = 0
air = deque()
air.append((0,0))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cheeze_list.append((i,j))

flag2 = 1
while flag2:
    if len(cheeze_list) == 0:
        flag2 = 0
        break
    if air != 0:
        bfs()
    else:
        continue

    i = 0
    flag = 1
    time += 1
    while flag:
        if len(cheeze_list)-1 < i:
            flag = 0
            break
        cnt = 0
        for k in range(4):
            ni = cheeze_list[i][0] + di[k]
            nj = cheeze_list[i][1] + dj[k]
            if arr[ni][nj] == 9:
                cnt += 1
            
        if cnt > 1:
            arr[cheeze_list[i][0]][cheeze_list[i][1]] = 0
            air.append((cheeze_list[i][0],cheeze_list[i][1]))
            cheeze_list.pop(i)

        else:
            i += 1    

print(time)