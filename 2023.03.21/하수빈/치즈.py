import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    # 0, 0은 무조건 공기이기 때문에 여기서 시작
    q = deque([[0, 0]])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    target = []
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                # 방문한 곳이 공기이고 방문한적이 없다면 방문 체크한 후 큐에 추가
                if not ref[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append([nr, nc])
                # 방문한 곳이 치즈라면
                elif ref[nr][nc]:
                    # visited + 1
                    visited[nr][nc] += 1
                    # 두번 방문했다면(두 변이 공기에 닿아있다면)
                    if visited[nr][nc] == 2:
                        # 삭제할 대상에 추가
                        target.append([nr, nc])
    
    # 타겟이 있다면
    if target:
        # 삭제하고 1반환
        for r, c in target:
            ref[r][c] = 0
        return 1
    # 타겟이 없다면 0반환
    else:
        return 0


N, M = map(int, input().split())
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ref = [list(map(int, input().split())) for _ in range(N)]
count = 0

# target 치즈가 남아있다면 반복
while bfs():
    count += 1

print(count)