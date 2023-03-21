from collections import deque
N, M = map(int, input().split())

dx = (-1,1,0,0)
dy = (0,0,-1,1)

## 치즈를 일일이 bfs 를 돌리니 시간초과가 나서
## 외부를 bfs 를 돌린 후 치즈와 접하는 부분을 찾았습니다.

def bfs(start):
    que = deque()
    que.append(start)
    while que:
        x, y = que.popleft()

        for k in (0,1,2,3,):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if cheeses[nx][ny] == 1: continue
            if cheeses[nx][ny] == 2: continue
            cheeses[nx][ny] = 2
            que.append((nx,ny))

cheeses = [list(map(int,input().split())) for _ in range(N)]
che =[]

def find_outside() : 
    check = False
    for i in range(N):
        for j in range(M):
            if cheeses[i][j] == 0:
                bfs((i,j))
                return True
            if cheeses[i][j] == 1:
                che.append((i,j))
                check= True
    return check
## 치즈가 있는 위치 찾기
def find_cheese() : 
    for i in range(N):
        for j in range(M):
            if cheeses[i][j] == 1:
                che.append((i,j))

time = 0
find_outside()
find_cheese()
l_che = len(che)

## 치즈가 다 녹았는지 확인하는 코드
def check():
    chee = 0
    for i,j in che:
        if cheeses[i][j] == 2 : chee += 1; continue
    return False if chee == l_che else True

## 치즈가 다 녹기 전까지 while 문 돌림
while check():
    time += 1

    C = set()
    for i,j in che:
        if cheeses[i][j] == 2 : continue


        count = 0## 치즈가 접한 부분 count
        for l in (0,1,2,3,): # 4방을 탐색했을 때 2 가 있으면 외부공기에 노출 된 치즈
            ni = i + dx[l]
            nj = j + dy[l]

            if cheeses[ni][nj] == 2:
                count +=1

        if count >= 2: # 노츨된 치즈는 담아뒀다가 다음 for문에서 녹임
            C.add((i,j))
    
    for cx, cy in C:
        cheeses[cx][cy] = 2
        bfs((cx,cy)) 
        # 치즈가 녹은 위치에서 bfs 돌려서 치즈 내부에 공기가 있는지 파악

print(time)