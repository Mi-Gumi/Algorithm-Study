from collections import deque
N = int(input())

m = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs_n(start, is_rg = True):
    global v_n, v_rg
    q = deque()
    q.append(start)

    if is_rg:
        t = m[start[0]][start[1]]
        while q:
            x,y = q.popleft()
            if v_rg[x][y] :continue
            v_rg[x][y] = True

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N : continue
                if v_rg[nx][ny] : continue
                if m[nx][ny] == 'B' and t == 'B':
                    q.append((nx,ny))
                elif (t=='G' or t =='R')and (m[nx][ny] == 'R' or m[nx][ny]=='G'):
                    q.append((nx,ny))
    else:
        t = m[start[0]][start[1]]
        while q:
            x,y = q.popleft()
            if v_n[x][y] : continue
            v_n[x][y] = True

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= N or ny >= N : continue
                if v_n[nx][ny]: continue
                if t == m[nx][ny]:
                    q.append((nx,ny))
    return 1


ans_n = 0
ans_rg = 0
v_n = [[False for _ in range(N)] for _ in range(N)]
v_rg = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not v_n[i][j]:
            ans_n += bfs_n((i,j),False)
        if not v_rg[i][j]:
            ans_rg += bfs_n((i,j),True)
print(ans_n, ans_rg)