from collections import deque


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(start, is_rg = True): # bfs(시작지점, 색약인지 아닌지)
    global v_n, v_rg
    q = deque()
    q.append(start)
    
    ## 색약일 경우 혹은 정상일 경우 is_visited 를 분리 
    targ_visit = v_rg if is_rg else v_n
    t = m[start[0]][start[1]] # 타겟은 우리가 탐색을 처음 시작할 때의 색상
    while q:
        x,y = q.popleft()
        
        if targ_visit[x][y] : 
            continue
        targ_visit[x][y] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N : # 범위를 벗어나면 continue
                continue
            if targ_visit[nx][ny]: # 방문이 된 지역이면 continue
                continue
            
            ### 색약일 경우
            if is_rg:
                
                # 파란색 -> 파란색을 동일하게 보는데
                # 초록색 빨간색 -> 같은색 
                if m[nx][ny] == 'B' and t == 'B':
                    q.append((nx,ny))
                elif (t=='G' or t =='R')and (m[nx][ny] == 'R' or m[nx][ny]=='G'):
                    q.append((nx,ny))

            else: ## 정상일 경우
                if t == m[nx][ny]:
                    q.append((nx,ny))
    return 1

ans_n = 0
ans_rg = 0

N = int(input())

v_n = [[False for _ in range(N)] for _ in range(N)]  # 정상일 경우 탐색하는    visited Matrix
v_rg = [[False for _ in range(N)] for _ in range(N)] # 색약일 경우 탐색을 하는 visited Matrix

m = [list(input()) for _ in range(N)]

# 적록 색약인 사람은 R 과 G 를 구분하지 못하기 때문에, 이를 비교하며
# bfs를 진행하면 됨.
for i in range(N):
    for j in range(N):
        
        if not v_n[i][j]: # 정상인이 보는 부분에서 visited가 False (방문이 안됬을 경우)
            ans_n += bfs((i,j),False) # 정상인이 보는 구역에 1 추가
            
        if not v_rg[i][j]: # 색약이 보는 부분에서 visited가 False (방문이 안됬을 경우)
            ans_rg += bfs((i,j),True) # 색약이 보는 구역에 1 추가
            
print(ans_n, ans_rg)