from collections import deque


def bfs(_map, ii, jj):
    # 좌표값과 거리를 덱에 튜플로 저장
    de = deque([(ii, jj, 0)])
    visited[ii][jj] = True

    while de:
        ci, cj, distance = de.popleft()

        for i in range(4): # 네방향 탐색
            ni = ci + di[i]
            nj = cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if _map[ni][nj] == 'L' and visited[ni][nj] == False:
                    de.append((ni, nj, distance + 1))
                    visited[ni][nj] = True
    return distance  # 마지막으로 탐색한 육지의 거리


N, M = map(int, input().split())

Map = [list(input()) for _ in range(N)]

di = [0, -1, 0, 1]  # R, D, L, U
dj = [1, 0, -1, 0]
dd = []     # 가장 먼 육지까지의 최단거리 배열
for i in range(N):
    for j in range(M):
        d = 0
        if Map[i][j] == 'L':    # 육지 체크
            visited = [[False] * M for i in range(N)] # 방문 초기화
            d = bfs(Map, i, j)  # 너비우선탐색
        if d:
            dd.append(d)        # 1 이상이면 추가

ans = max(dd) # 최단거리들의 최대값

print(ans)
