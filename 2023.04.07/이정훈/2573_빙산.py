from collections import deque
import sys
input = sys.stdin.readline

# 섬하나의 ice개수를 count
def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = ans
    tmp_cnt = 1
    while queue:
        ci, cj = queue.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < row and 0 <= nj < col and arr[ni][nj] and visited[ni][nj] != ans:
                queue.append((ni, nj))
                visited[ni][nj] = ans
                tmp_cnt += 1
    return tmp_cnt

def land_check() :
    for i, j in ice_pos :
        if arr[i][j] and visited[i][j] != ans:
            land_cnt = bfs(i, j)
            break
    # 빙산 하나의 얼음이 남아있는 얼음의 개수와 다르다면 분리된 것
    if land_cnt != ice:
        return True
    return False


row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
visited = [[0]*col for _ in range(row)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))

ans = 1
# 0이 아닌 값을 카운트
ice = 0
ice_pos = []
for i in range(row):
    for j in range(col):
        if arr[i][j]:
            ice += 1
            ice_pos.append((i,j))
# 얼음이 남아있으면
while ice:
    # 녹을 얼음 계산
    melt = []
    for i, j in ice_pos :
        if arr[i][j]:
            cnt = 0
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col and not arr[ni][nj]:
                    cnt += 1
            if cnt:
                melt.append((i, j, cnt))
    # 얼음 녹음 , 0이 되는 얼음이 있는지 체크 
    tmp = ice
    if melt :
        for i, j, cnt in melt:
            next = arr[i][j] - cnt
            if next <= 0:
                arr[i][j] = 0
                ice -= 1
            else:
                arr[i][j] = next
    # 녹은 얼음이 있으면
    if tmp != ice :
        if land_check() :
            break
    ans += 1

if ice:
    print(ans)
else:
    print(0)
