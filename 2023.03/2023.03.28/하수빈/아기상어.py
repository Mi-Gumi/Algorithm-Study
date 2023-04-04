import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global r, c, size, eat, ans
    q = deque([[r, c]])
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    cnt = 0
    # 최단 거리 먹이 배열
    food = []
    while q:
        cnt += 1
        for _ in range(len(q)):
            sr, sc = q.popleft()
            for dr, dc in d:
                nr, nc = sr + dr, sc + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    # 비었거나 상어와 같은 사이즈의 물고기가 있다면 방문처리
                    if sea[nr][nc] == 0 or sea[nr][nc] == size:
                        visited[nr][nc] = 1
                        q.append([nr, nc])
                    # 물고기의 사이즈가 상어보다 작다면 먹이 배열에 추가
                    elif sea[nr][nc] < size:
                        food.append([nr, nc])
        if food:
            # 이동 횟수 ans에 추가
            ans += cnt
            # 먹은 물고기 갯수 추가
            eat += 1
            # 최단 거리 왼쪽 위 물고기 삭제
            food.sort(key=lambda x:x[1])
            food.sort(key=lambda x:x[0])
            r, c = food[0][0], food[0][1]
            sea[r][c] = 0
            return 1
    return 0



N = int(input())
sea = []
r = 0
c = 0
size = 2
eat = 0
ans = 0
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            r, c = i, j
            tmp[j] = 0
    sea.append(tmp)

while bfs():
    # 먹이를 사이즈만큼 먹었다면 사이즈++
    if eat == size:
        eat = 0
        size += 1

print(ans)
