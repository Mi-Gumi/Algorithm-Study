from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 치즈가 존재하는지 체크
def check(arr):
    for lst in arr:
        if lst.count(1):
            return True
    return False

# 치즈를 제외한 외부 공기를 표시
def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    arr[i][j] = 9
    while que:
        si, sj = que.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = si + di
            nj = sj + dj
            if 0<=ni<N and 0<=nj<M:
                # 외부 공기를 9로 표시
                if (arr[ni][nj] == 0 or arr[ni][nj] == 9) and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    arr[ni][nj] = 9
                    que.append((ni, nj))
time = 0
while check(arr): # 치즈가 존재할 때까지 반복
    # 가장자리는 무조건 공기이므로 0,0 에서 탐색 시작
    bfs(0, 0)
    melting = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt = 0
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni = i + di
                    nj = j + dj
                    if 0<= ni < N and 0<= nj < M and arr[ni][nj] == 9:
                        cnt += 1
                if cnt >= 2: # 공기가 2변이상 노출되는지 판단
                    melting.append((i, j))
    for mi, mj in melting:
        arr[mi][mj] = 0 # 치즈를 변환
    time += 1 # 시간 체크
print(time)



