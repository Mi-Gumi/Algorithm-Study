from collections import deque
def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k] 
            if 0 <= ni < n and 0<= nj <n and v[ni][nj] == 0:
                if l<=abs(arr[ni][nj]-arr[i][j])<=r:
                    v[ni][nj] = 1
                    q.append((ni,nj))
                    temp.append((ni,nj))
    
    return temp


n,l,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = 0

while 1:
    v = [[0] * (n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                v[i][j] = 1
                country = bfs(i,j)
                if len(country) > 1:
                    flag = 1
                    num = sum([arr[x][y] for x,y in country]) // len(country)
                    for x,y in country:
                        arr[x][y] = num
    
    if flag == 0:
        break
    
    ans += 1

print(ans)