import sys
from collections import deque
input = sys.stdin.readline

# 바이러스 조합 생성
def comb(r, s):
    if r == 0:
        comb_virus.append(tmp_virus[:])
        return

    for i in range(s, len(virus)):
        tmp_virus.append(virus[i][:])
        comb(r - 1, i + 1)
        tmp_virus.pop()

# bfs실행
def bfs(v):
    q = deque(v)
    visited = [[-1] * N for _ in range(N)]
    for r, c in q:
        visited[r][c] = 0
    cnt = 1
    result = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            # 현재위치가 바이러스가 아니라면 result값 변경
            if lab[r][c] == 0:
                result = max(result, visited[r][c])
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1 and lab[nr][nc] != 1: 
                    q.append([nr, nc])
                    visited[nr][nc] = cnt
        cnt += 1

    # 감염 안된 부분이 남아있다면 10 ** 9 반환
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and lab[i][j] == 0:
                return 10 ** 9

    return result


N, M = map(int, input().split())
lab = []
virus = []
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = 10 ** 9
# 바이러스 위치 기억
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            virus.append([i, j])
    lab.append(tmp)
comb_virus = []
tmp_virus = []
# 조합 생성
comb(M, 0)
# bfs한 결과와 ans중 작은값 선택
for v in comb_virus:
    ans = min(bfs(v), ans)

# ans가 변하지 않았다면 -1 출력
if ans == 10**9:
    print(-1)
# 변했다면 ans 출력
else:
    print(ans)
