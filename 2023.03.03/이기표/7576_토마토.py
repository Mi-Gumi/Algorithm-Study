import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    while q:
        si, sj = q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)): # 상하 좌우로 이동
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = arr[si][sj] + 1 # 위치를 이동할 때마다 증가
                    q.append((ni, nj))

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque() # 덱 사용 -> 시간초과 방지
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: # 토마토가 있는 경우 위치 추가
            q.append((i,j))
bfs() # 탐색 시작

flag = 0
for lst in arr:
    if lst.count(0): # 0이 아직 남아있는 경우
        flag = 1 # 안 익은 토마토 존재
        break

ans = 0
for lst in arr: # 이동한 위치의 값을 도출
    ans = max(ans, max(lst))

if flag:
    print(-1) # 안 익은 토마토 존재
else:
    print(ans-1) # 처음 위치 포함하기때문에 -1