def is_ice():
    global trigger
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                trigger = True
                return True
    trigger = False
    return False

N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

from collections import deque

dx = (0,0,1,-1)
dy = (1,-1,0,0)
def bfs(start):
    ice = [start]

    que = deque()
    que.append(start)
    is_visited[start[0]][start[1]] = True

    while que:
        x,y = que.popleft()

        for k in (0,1,2,3):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx <0 or ny < 0 or nx>= N or ny >= M:continue
            if is_visited[nx][ny] : continue
            if matrix[nx][ny] == 0: continue

            ice.append((nx,ny))
            is_visited[nx][ny]=True
            que.append((nx,ny))
    return ice

time = 0
trigger = None

while is_ice():
    


    ices = []
    is_visited = [[False for _ in range(M)] for _ in range(N)]

    melting = dict()

    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0 and not is_visited[i][j]:
                targets = bfs((i,j))
                
                for a, b in targets:
                    t = 0
                    for k in (0,1,2,3):
                        na = a + dx[k]
                        nb = b + dy[k]
                        if matrix[na][nb] == 0:
                            t += 1
                    melting[(a,b)] = t

                ices.append(targets)
    
    if len(ices) >= 2:
        break

    time += 1

    for a, b in melting:
        melt_range = melting[(a,b)]
        matrix[a][b] = matrix[a][b] - melt_range
        if matrix[a][b] < 0 :
            matrix[a][b] = 0

if trigger:
    print(time)
else:
    print(0)
    