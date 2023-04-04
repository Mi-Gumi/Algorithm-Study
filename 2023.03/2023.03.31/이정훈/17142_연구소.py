from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

lab = [list(map(int,input().strip().split())) for _ in range(N)]
ans = 1<<30
virus = []
blank = 0
for i in range(N) :
    for j in range(N) :
        if lab[i][j] == 2 :
            virus.append((i, j))
        elif lab[i][j] == 0 :
            blank += 1

flag = False

for combi in combinations(virus, M) :
    visited = [[0]*N for _ in range(N)]
    queue = deque(combi)
    for i , j in combi :
        visited[i][j] = 1
    time = 0
    blk = blank
    Qlen = M
    while Qlen and blk :
        time += 1
        for k in range(Qlen) :
            i, j = queue.popleft()
            Qlen -= 1
            for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
                ni, nj  = i + di, j + dj
                if 0<= ni < N and 0<= nj < N and lab[ni][nj] != 1 and visited[ni][nj] == 0 :
                    queue.append((ni,nj))
                    Qlen += 1
                    visited[ni][nj] = 1
                    if lab[ni][nj] == 0 :
                        blk -= 1
    if not blk :
        if time < ans :
            ans = time
    
if ans != 1<<30 :
    print(ans)
else :
    print(-1)
