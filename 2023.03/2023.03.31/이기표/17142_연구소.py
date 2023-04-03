from collections import deque

def change(order, visited):
    for i, j in order:
        visited[i][j] = 0
    for i, j in wall:
        visited[i][j] = 0

def bfs(que, visited):
    time = 0
    while que:
        si, sj = que.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1 and arr[ni][nj] != 1:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[si][sj] + 1
                    if arr[ni][nj] == 0: # 실제 이동 횟수 / 바이러스가 존재하는 2는 제외
                        time = visited[si][sj] + 1

    flag = 0
    for v in visited: # 아직 이동 안 한 곳이 남아있으면 종료
        if v.count(-1):
            flag = 1
            break
    if flag:
        return 9999999
    else:
        return time

def comb(n, r, k, s): # 바이러스를 위치시키는 조합
    global ans
    if r == k:
        visited = [[-1] * N for _ in range(N)]
        change(order, visited) # 벽이나 바이러스일 경우 방문 체크
        data = deque(order)
        rst = bfs(data, visited)
        ans = min(rst, ans) # 최소경로를 찾기
        return
    else:
        for i in range(s, n - r + 1 + k):
            order[k] = covid[i]
            comb(n, r, k + 1, i + 1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
covid = []
wall = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            covid.append([i,j])
        if arr[i][j] == 1:
            wall.append([i,j])
order = [[0, 0] for _ in range(M)]
ans = 9999999
comb(len(covid), M, 0, 0)

if ans == 9999999: # 값이 바뀌지 않으면 탐색 실패
    print(-1)
else:
    print(ans)

