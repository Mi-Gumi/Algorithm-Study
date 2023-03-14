import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    # 방문 리스트
    visited = [[0] * M for _ in range(N)]
    # 방문할 큐
    q = deque([[x, y]])
    # 처음 지역 방문 처리
    visited[x][y] = 1
    max_t = 0
    # 큐에 요소가있다면
    while q:
        # x, y 재설정
        x, y = q.popleft()
        # dx, dy 설정
        for dx, dy in direction:
            # nx, ny 설정
            nx, ny = x + dx, y + dy
            # nx와 ny가 0과 N, 0과 M사이에 있고 nx, ny좌표가 육지이고 방문한적이 없다면
            if 0 <= nx < N and 0 <= ny < M and island[nx][ny] == 'L' and not visited[nx][ny]:
                # 방문 경로 횟수 + 1
                visited[nx][ny] = visited[x][y] + 1
                # 최댓값 교체
                if max_t < visited[nx][ny]:
                    max_t = visited[nx][ny]
                # 방문할 큐에 nx, ny 추가
                q.append([nx, ny])

    # 최댓값 - 1 반환
    return max_t - 1



N, M = map(int, input().split())

island = []
ans = 0
# 오른쪽, 아래쪽, 왼쪽, 위쪽
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(N):
    # 문자열보다 리스트가 처리속도 빠름
    island.append(list(input()))

for i in range(N):
    for j in range(M):
        if island[i][j] == 'L':
            t = bfs(i, j)
            if ans < t:
                ans = t

print(ans)

