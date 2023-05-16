import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque([[0, 0, 0]])
    visited[0][0] = 1
    visited_s = [[0] * M for _ in range(N)]
    cnt = 0
    
    while q:
        # T 이상 시간이 걸린다면 Fail 반환
        if cnt >= T:
            return 'Fail'
        for _ in range(len(q)):
            r, c, s = q.popleft()
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                # 공주에 도달헀다면 cnt + 1 반환
                if nr == N - 1 and nc == M - 1:
                    return cnt + 1
                if 0 <= nr < N and 0 <= nc < M:
                    # 검을 들었다면 새로운 visited에 방문처리
                    if s and not visited_s[nr][nc]:
                        visited_s[nr][nc] = 1
                        q.append([nr, nc, 1])
                    # 검이 없다면
                    else:
                        # 검이 없을 때 검을 만났다면 기존 visited와 새로운 visited에 모두 방문처리
                        if castle[nr][nc] == 2 and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            visited_s[nr][nc] = 1
                            q.append([nr, nc, 1])
                        # 벽이 없는 길이라면 방문처리후 이동
                        elif castle[nr][nc] == 0 and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q.append([nr, nc, 0])
        cnt += 1
    
    # 공주에게 갈 수 있는 길이 없다면 Fail 반환
    return 'Fail'


N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))

print(bfs())