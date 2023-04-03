from collections import deque

def bfish (ci,cj) :
    search = deque()
    search.append((ci, cj, 0 ))
    time = 0
    size = 2
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    visited[ci][cj] = 1
    while search :
        bob = []
        for k in range(len(search)) :
            i , j , distance= search.popleft()
            if 0< space[i][j] < size :
                bob.append((i,j,distance))
            
            for di, dj in d :
                ni, nj = i + di, j + dj
                if 0<= ni < N and 0<= nj < N and space[ni][nj] <= size and visited[ni][nj] == 0:
                    search.append((ni,nj,distance+1))
                    visited[ni][nj] = 1
        if bob :
            bob.sort()
            i, j , distance = bob[0]
            space[i][j] = 0
            cnt += 1
            if cnt == size :
                size += 1
                cnt = 0
            time += distance
            ci , cj = i, j
            search = deque([(ci,cj, 0)])
            visited = [[0]*N for _ in range(N)]
            visited[ci][cj] = 1
    return time

d = ((-1,0),(0,-1),(0,1),(1,0))
N = int(input())

space = [list(map(int,input().split())) for _ in range(N)]
for c in range(N) :
    for x in range(N) :
        if space[c][x] == 9 :
            space[c][x] = 0
            ans = bfish(c,x)
            break
print(ans)