from collections import deque
def bfs(i, j, target):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1

    while que:
        si, sj = que.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                tmp = abs(arr[ni][nj] - arr[si][sj])
                if L <= tmp <= R: # 해당 조건에 만족하는 경우 나라 탐색
                    target.append([arr[ni][nj], ni, nj]) # 국경선 공유
                    que.append((ni, nj))
                    visited[ni][nj] = 1
    # 국경을 공유하는 나라간 평균과 그 값을 매핑
    avg = 0
    for i in range(len(target)):
        avg += target[i][0]
    avg //= len(target)
    for a, b, c in target:
        arr[b][c] = avg
    if len(target) == 1:
        return False
    else:
        return True

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while 1:
    visited = [[0] * N for _ in range(N)]
    flag = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                target = [[arr[i][j], i, j]]
                rst = bfs(i, j, target)
                if rst:
                    flag = 0
    # 국경을 공유하는 나라가 더 이상 없을 경우 종료
    if flag:
        break
    cnt += 1

print(cnt)