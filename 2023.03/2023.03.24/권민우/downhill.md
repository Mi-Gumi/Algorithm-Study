```python
import sys
input = sys.stdin.readline

def dfs(x,y, visited):
    global cnt
    visited[x][y] = 1

    if x == M-1 and y == N-1:
        cnt += 1
        return

    for dr, dc in d:
        nx = x + dr
        ny = y + dc

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[x][y] > arr[nx][ny]:
            dfs(nx,ny, visited)
            visited[nx][ny] = 0

d = [(-1,0),(1,0),(0,-1),(0,1)]
M, N = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
visited = [[0]*N for _ in range(M)]
dfs(0,0,visited)

print(cnt)
```

시간초과...^^
