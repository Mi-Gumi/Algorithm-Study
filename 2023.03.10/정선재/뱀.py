from collections import deque

N = int(input())
ap = int(input())
arr = [[0]*N for _ in range(N)] 
cnt = 1
snake = deque()
x,y = 0,0
di = [0,1,0,-1]
dj = [1,0,-1,0]
idx = 0
arr[x][y] = 1
snake.append((x,y))
for _ in range(ap):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 2
D = int(input())
nex = []
sum_cnt = 0
for p in range(D):
    t,c = input().split()
    if p != 0:
        time = int(t) - int(sum_cnt)
        nex.append((time,c))
        sum_cnt = int(t)
    else:
        nex.append((t,c))
        sum_cnt = int(t)

flag = 1
for i in range(len(nex)):
    if flag == 0:
        break
    for j in range(int(nex[i][0])):
        ni = x + di[idx]
        nj = y + dj[idx]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 2:
            arr[ni][nj] = 1
            cnt += 1
            snake.append((ni,nj))
            x,y = ni,nj
        
        elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            cnt += 1
            arr[ni][nj] = 1
            snake.append((ni,nj))
            k,l = snake.popleft()
            arr[k][l] = 0
            x,y = ni,nj

        else:
            flag = 0
            break
    if nex[i][1] == 'L':
        idx = (idx-1)%4
    else:
        idx = (idx+1)%4

if flag != 0:
    for q in range(N):
        ni = x + di[idx]
        nj = y + dj[idx]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 2:
            arr[ni][nj] = 1
            cnt += 1
            snake.append((ni,nj))
            x,y = ni,nj
        
        elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            cnt += 1
            arr[ni][nj] = 1
            snake.append((ni,nj))
            k,l = snake.popleft()
            arr[k][l] = 0
            x,y = ni,nj

        else:
            flag = 0
            break

print(cnt)

