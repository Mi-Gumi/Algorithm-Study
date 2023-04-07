import sys
from collections import deque
input = sys.stdin.readline


# 빙산 녹이는 함수
def melt():
    # 녹을 위치 기억
    melting = [[0] * M for _ in range(N)]
    for r, c in iceberg:
        cnt = 0
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not sea[nr][nc]:
                cnt += 1
        melting[r][c] = cnt
    
    # 제거 할 얼음 배열
    remove_ice = []

    for r, c in iceberg:
        # 얼음 크기가 녹는 양 보다 크다면
        if sea[r][c] > melting[r][c]:
            sea[r][c] -= melting[r][c]
        # 얼음 크기가 녹는 양보다 작다면
        else:
            sea[r][c] = 0
            remove_ice.append([r, c])
    
    # 제거 할 얼음 제거
    for r, c in remove_ice:
        iceberg.remove([r, c])
            

# 얼음 덩이 수 체크
def check():
    # 첫 얼음 부분 부터 체크
    q = deque([[iceberg[0][0], iceberg[0][1]]])
    visited = [[0] * M for _ in range(N)]
    visited[iceberg[0][0]][iceberg[0][1]] = 1
    # 첫 얼음과 이어진 얼음 모두 방문 체크
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and sea[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append([nr, nc])
    
    for r, c in iceberg:
        # 방문하지 않은 얼음이 남아 있다면 0 반환
        if not visited[r][c]:
            return 0
    
    # 얼음이 한 덩이라면 1 반환
    return 1


N, M = map(int, input().split())
sea = []
iceberg = []
# 빙산 위치 저장
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j]:
            iceberg.append([i, j])
    sea.append(tmp)
ans = 0
d = ((1, 0), (0, 1), (-1, 0), (0, -1))

# 아직 한덩이라면 반복
while check():
    ans += 1
    melt()
    # 빙산이 동시에 모두 녹았다면 ans = 0 으로 설정
    if not iceberg:
        ans = 0
        break

print(ans)