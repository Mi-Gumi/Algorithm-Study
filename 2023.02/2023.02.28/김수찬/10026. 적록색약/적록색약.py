from collections import deque
N = int(input())

m = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs_n(start, is_rg = True):
    global v_n, v_rg
    q = deque()
    q.append(start)
    targ_visit = v_rg if is_rg else v_n

    t = m[start[0]][start[1]]
    while q:
        x,y = q.popleft()
        if targ_visit[x][y] : continue
        targ_visit[x][y] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N : continue
            if targ_visit[nx][ny]: continue

            if is_rg:
                if m[nx][ny] == 'B' and t == 'B':
                    q.append((nx,ny))
                elif (t=='G' or t =='R')and (m[nx][ny] == 'R' or m[nx][ny]=='G'):
                    q.append((nx,ny))
            else:
                if t == m[nx][ny]:
                    q.append((nx,ny))
    return 1


ans_n = 0
ans_rg = 0
v_n = [[False for _ in range(N)] for _ in range(N)]
v_rg = [[False for _ in range(N)] for _ in range(N)]

# 적록 색약인 사람은 R 과 G 를 구분하지 못하기 때문에, 이를 비교하며
# bfs를 진행하면 됨.

for i in range(N):
    for j in range(N):
        if not v_n[i][j]:
            ans_n += bfs_n((i,j),False)
        if not v_rg[i][j]:
            ans_rg += bfs_n((i,j),True)
print(ans_n, ans_rg)