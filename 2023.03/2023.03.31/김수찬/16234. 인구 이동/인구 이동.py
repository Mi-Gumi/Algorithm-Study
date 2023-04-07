from collections import deque
N, L, R = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]



def connected(): # 국가마다 연결된 연결 여부를 파악

    def bfs(start): # 그룹을 연결지을 bfs 코드
        nonlocal mt, group
        que = deque([start])
    
        total= matrix[start[0]][start[1]]
        cnt = 1
        mt[start[0]][start[1]] = group
        while que:
            x,y = que.popleft()
            for dx, dy in ((0,1),(0,-1),(-1,0),(1,0)):
                nx = x + dx
                ny = y + dy
                if nx<0 or ny<0 or nx>=N or ny>=N : continue
                if mt[nx][ny] != 0: continue
                if L <= abs(matrix[nx][ny] - matrix[x][y]) <= R:
                    mt[nx][ny] = group
                    total += matrix[nx][ny]
                    cnt += 1
                    que.append((nx,ny))
        return total//cnt # 나누어 담길 population을 return으로 
    
    group = 1 # 그룹으로 나누어서 groups에 담을 예정
    groups = dict()
    mt = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mt[i][j] == 0: # 그룹이 설정되어있지 않을 경우에 bfs 진행
                popl = bfs((i,j))
                groups[group] = popl
                group += 1 # 다음그룹으로 업데이트

    for i in range(N):
        for j in range(N): # 연합으로 바뀌게된 인구수로 업데이트
            matrix[i][j] = groups[mt[i][j]]

    return group # 현재 그룹의 수 제출

trigger = 0
ans = -1

# 그룹의 수가 matrix의 원소 수랑 같을 경우 더이상 진행이 안되기 때문에
# 이것을 while문의 trigger 로 진행
while trigger != N*N + 1:
    ans += 1
    trigger = connected()
print(ans)