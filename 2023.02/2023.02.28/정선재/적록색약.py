
                
def bfs(arr):
    global ans
    for x in range(N):
        for y in range(N):
            if visited[x][y] != 'x':
                ans += 1
                n, m = x,y
            for K in range(4):
                nx = n + dx[K]
                ny = m + dy[K]
                if 0 <= nx < N and N > ny >= 0 and visited[x][y] != 'x':
                    if arr[x][y] == arr[nx][ny]:    
                        visited[nx][ny] = 'x'
                        n,m = nx, ny
        

def bfs2(arr):
    global ans2
    for x in range(N):
        for y in range(N):
            if visited2[x][y] != 'x':
                ans2 += 1
                if arr[x][y] =='R':
                    arr[x][y] = 'G'
                    n, m = x,y
                for i in range(4):
                    nx = n + dx[i]
                    ny = m + dy[i]
                    if 0 <= nx < N and N > ny >= 0:
                        if arr[nx][ny] == 'R':
                            arr[nx][ny] = 'G'
                        if arr[x][y] == arr[nx][ny]:  
                            visited2[nx][ny] = 'x'
                            n,m = nx, ny
                



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
ans = 0
ans2 = 0
bfs(arr)
bfs2(arr)

print(ans)
print(ans2)