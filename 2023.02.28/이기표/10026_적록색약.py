def bfs(i, j, C):
    que = []
    que.append((i, j)) # 큐에 추가
    visited[i][j] = 1 # 방문체크

    while que:
        si, sj = que.pop(0) # pop
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)): # 상하좌우 델타 이동
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == C and visited[ni][nj] == 0:
                que.append((ni, nj)) # 해당컬러에 만족하는 경우
                visited[ni][nj] = 1 # 방문체크

before_cnt = 0 # 적록색약 전 카운트
after_cnt = 0 # 적롤색약 후 카운트
N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N): # before 적록색약
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            before_cnt += 1
        elif arr[i][j] == 'G' and visited[i][j] == 0:
            bfs(i, j, 'G')
            before_cnt += 1
        elif arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            before_cnt += 1

        if arr[i][j] == 'G': arr[i][j] = 'R' # 초록색 -> 빨간색 변경

visited = [[0] * N for _ in range(N)]
for i in range(N): # 적록색약 탐색
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            after_cnt += 1
        elif arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            after_cnt += 1

print(before_cnt, after_cnt)



