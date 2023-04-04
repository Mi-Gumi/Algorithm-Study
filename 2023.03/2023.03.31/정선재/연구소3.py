import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def find():
    global wall
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                vi.append((i,j))
            if arr[i][j] == 1:
                wall += 1

def bfs(comb):
    q = deque()
    q += comb
    while q:  
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] != 1:
                if arr[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni,nj))
                


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

min_time = []
wall = 0
vi = []
di = [1,0,-1,0]
dj = [0,1,0,-1]
find()
for comb in combinations(vi,m):
    visited = [[0]*n for _ in range(n)]
    for p,w in comb:
        visited[p][w] = 1
    bfs(comb)

    cnt = 0
    max_val = 0
    flag = 1
    for i in range(n):
        if flag == 0:
            break
        for j in range(n):
            if visited[i][j] > max_val:
                max_val = visited[i][j]
            if visited[i][j] == 0:
                cnt += 1
                if cnt > wall:
                    flag = 0
                    max_val =2
                    break
    if max_val != 2:
        min_time.append(max_val)

if len(min_time) == 0:
    print(-1)
else:
    print(min(min_time)-1)