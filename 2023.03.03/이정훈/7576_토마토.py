from collections import deque
d = ((0, 1), (1, 0), (-1, 0), (0, -1))

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]  # 방문처리 & cnt

queue = deque()

# 첫 시작점들을 모두 큐에 push
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1

while queue:
    si, sj = queue.popleft()

    for di, dj in d:
        ni, nj = si + di, sj + dj
        if ni < 0 or ni > N - 1 or nj < 0 or nj > M - 1:
            continue
        if visited[ni][nj]:
            continue
        if box[ni][nj] != 0:
            continue
        # 방문하지 않은 0일 경우
        queue.append((ni, nj))
        box[ni][nj] = 1
        # 일수 count 함과 동시에 방문처리
        visited[ni][nj] = visited[si][sj] + 1

flag = True
_max = 0
for i in range(N):
    # 0이 남아 있으면
    if 0 in box[i]:
        flag = False
        break
    tmp_max = max(visited[i])
    if _max < tmp_max:
        _max = tmp_max
if flag:
    print(_max - 1)
else:
    print(-1)
