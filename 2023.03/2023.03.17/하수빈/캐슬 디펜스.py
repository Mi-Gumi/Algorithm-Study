import sys
input = sys.stdin.readline
from collections import deque
import copy

def bfs(f, s, t):
    # 궁수의 위치와 궁수 번호를 큐에 추가
    q = deque([[N - 1, f, 0], [N - 1, s, 1], [N - 1, t, 2]])
    # 각 궁수의 visited
    visited = [[[0] * M for _ in range(N)] for _ in range(3)]
    # 각 궁수의 타겟
    target = [[], [], []]
    # 사정거리 만큼 반복
    for _ in range(D):
        for _ in range(len(q)):
            r, c, tower = q.popleft()
            # 적이 존재하고 궁수의 타겟이 정해지지 않았다면
            if new_castle[r][c]:
                if not target[tower]:
                    target[tower].append(r)
                    target[tower].append(c)
            # 적이 없다면 다음 탐색 위치 큐에 추가
            else:
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and not visited[tower][nr][nc]:
                        visited[tower][nr][nc] = 1
                        q.append([nr, nc, tower])

    # 타겟 반환
    return target


N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
# 왼쪽부터 3방 탐색
dir = [[0, -1], [-1, 0], [0, 1]]
ans = 0

# 순열 생성
for i in range(M - 2):
    for j in range(i + 1,  M - 1):
        for k in range(j + 1, M):
            # 새 필드 생성
            new_castle = copy.deepcopy(castle)
            tmp = 0
            for _ in range(N):
                # 목표 저장
                shoot = bfs(i, j, k)
                # 목표 제거
                for s in shoot:
                    if s and new_castle[s[0]][s[1]]:
                        # 이미 제거했다면 tmp 증가 x
                        new_castle[s[0]][s[1]] = 0
                        tmp += 1
                # 마지막 줄 제거
                new_castle.pop()
                # 0으로 된 첫 줄 추가
                new_castle.insert(0, [0] * M)
            # ans 변경
            ans = max(ans, tmp)

print(ans)