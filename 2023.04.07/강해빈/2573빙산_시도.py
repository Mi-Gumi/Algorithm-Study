import sys
from collections import deque


def bfs(x, y, visited): 
    q = deque([[x, y]]) # 빙산의 높이가 있고 방문하지 않은 좌표 저장
    melting_q = deque() # [각 빙산 좌표, 녹는 수] 저장하는 큐
    visited[x][y] = 1 # 방문 처리
    
    while q:
        x, y = q.popleft()
        sea_cnt = 0
        for i in range(4): # 사방탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 이어져있는 하나의 빙산 덩어리 체크
                # 빙산이면 방문체크 하고 q에 저장
                if arr[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                # 0이면 바다이므로 sea_cnt 카운트
                else:
                    sea_cnt += 1
                    
        # 탐색하는 빙산 주변에 바다가 있으면 녹일 큐에 저장
        if sea_cnt:
            melting_q.append([x, y, sea_cnt])
    return melting_q


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0 # 출력
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

while True: # 빙산 덩어리 개수 0 또는 2이면 종료
    cnt = 0 # 빙산 덩어리의 개수
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            # 빙산의 높이가 있고 방문하지 않았으면
            if arr[x][y] != 0 and visited[x][y] == 0:
                cnt += 1 # 빙산 덩어리 카운트
                # 이어져있는 하나의 빙산 덩어리 체크
                # 각 빙산 좌표와 얼마나 녹을지 반환되는 함수
                melting = bfs(x, y, visited) 
                while melting:
                    mx, my, melt_cnt = melting.popleft()
                    if arr[mx][my] >= melt_cnt:
                        arr[mx][my] -= melt_cnt
                    elif melt_cnt > arr[mx][my] > 0:
                        arr[mx][my] = 0
    if cnt == 0: # 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면
        year = 0
        break
    if cnt >= 2: # 두 덩어리 이상으로 분리되는 최초의 시간(년)
        break
    year += 1
    
print(year)


