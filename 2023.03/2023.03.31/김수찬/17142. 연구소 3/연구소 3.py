from itertools import combinations
from collections import deque

def check():
    for i in range(N):
        for j in range(N):
            if matrix_cpy[i][j] == 0:
                return False
    return True

def bfs(Vs):
    que = deque(Vs)
    cnt = 0
    while que:
        x,y,depth = que.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx = x + dx
            ny = y + dy
            if nx<0 or ny<0 or nx>=N or ny>=N : continue
            if matrix_cpy[nx][ny] == -1 or matrix_cpy[nx][ny] == -3: continue
            if matrix_cpy[nx][ny] == 0 :
                matrix_cpy[nx][ny] = depth + 1 if matrix_cpy[x][y] != -2 else 1
                cnt = max(cnt, matrix_cpy[nx][ny])
                que.append((nx,ny, matrix_cpy[nx][ny]))
            if matrix_cpy[nx][ny] == -2: # 바이러스가 있을 경우에는
                matrix_cpy[nx][ny] = -3 # 탐색한 바이러스는 탐색처리를 해주고
                # depth만 늘려준다. 
                cnt = max(cnt, matrix_cpy[nx][ny])
                que.append((nx,ny, depth+1))
    return cnt if check() else N*N+1

N,M = map(int,input().split())
matrix_row = [list(map(int,input().split())) for _ in range(N)]

V = []
for i in range(N):
    for j in range(N):
        if matrix_row[i][j] == 2:
            V.append((i,j,0))
            matrix_row[i][j] = -2
        if matrix_row[i][j] == 1:
            matrix_row[i][j] = -1

ans = N*N+1
# print(deque(V))
for virus in combinations(V,M):
    matrix_cpy = [arr[:] for arr in matrix_row]
    # print(virus)
    ans = min(ans,bfs(virus))

if ans != N*N+1:
    print(ans)
else:
    print(-1)