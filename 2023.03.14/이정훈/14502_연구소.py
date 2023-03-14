from itertools import combinations
from collections import deque

def bfs() :
    visited = [[0]*(M+2) for _ in range(N+2)]
    safe_count = SAFE
    for vi, vj in Q :
        visited[vi][vj] = 1
    while Q :
        si, sj = Q.popleft()
        for di, dj in d :
            ni, nj = si + di , sj + dj
            if lab[ni][nj] == 0 and visited[ni][nj] != 1 :
                Q.append((ni,nj))
                visited[ni][nj] = 1
                safe_count -= 1
    return safe_count

d = ((0,1),(1,0),(0,-1),(-1,0))

N, M = map(int,input().split())

lab = [[1]*(M+2)] + [ [1] + list(map(int,input().split())) + [1] for _ in range(N)] +  [[1]*(M+2)] 
virus = []
wall_possible = []
SAFE = -3
for i in range(1,N+1) :
    for j in range(1,M+1) :
        if lab[i][j] == 2 :
            virus.append((i,j))
        elif lab[i][j] == 0 :
            wall_possible.append((i,j))
            SAFE += 1

wall_combi = combinations(wall_possible, 3)
safe = []
for combi in wall_combi :
    for wall_i, wall_j in combi :
        lab[wall_i][wall_j] = 1
        
    Q = deque(virus)
    safe.append(bfs())
    
    for wall_i, wall_j in combi :
        lab[wall_i][wall_j] = 0
        
print(max(safe))
