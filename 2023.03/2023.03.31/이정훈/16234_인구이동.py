import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j,union_cnt) :
    
    queue = deque()
    queue.append((i,j))
    union_list = []

    while queue :
        ci, cj = queue.popleft()
        for di, dj in d :
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and L <= abs(kuni[ni][nj] - kuni[ci][cj]) <= R :
                queue.append((ni,nj))
                visited[ni][nj] = union_cnt
                union_list.append((ni,nj))
    return union_list


N, L, R = map(int,input().split())
NN = N*N
kuni = [list(map(int,input().split())) for _ in range(N)]
d = ((0,1),(1,0),(0,-1),(-1,0))
day = 0
while day <= 2000 :
    visited = [[0]*N for _ in range(N)] 
    union_cnt = 1
    unions = []
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                union = bfs(i,j,union_cnt)
                if len(union) != 0 :
                    unions.append(union)
                    union_cnt += 1
    unions_len = len(unions)
    # print(unions)
    if unions_len == 0 :
        break
    day += 1
    for union in unions :
        total = 0
        for i, j in union :
            total += kuni[i][j]
        population = total // len(union)
        for i, j in union :
            kuni[i][j] = population
            
print(day)



#  visited 를 만들고 0인 곳을 bfs, 같은 연합을 같은 숫자로 연합을 구하고 연합리스트안의 리스트에 좌표형태로 넣음 모든 연합을 구하면 연합들의 인구를 평균화 visited 초기화, 인구이동이 없는 경우는 모든 국가가 연합이 되어 평균화 된뒤
#  다시 과정을 반복