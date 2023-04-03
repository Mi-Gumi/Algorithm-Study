'''
빈 공간 위치 저장 and Combination 진행
안정 영역 빈공간의 최대 크기 출력
bfs 후 0의 영역 count(0)
'''
from itertools import combinations
from collections import deque
import copy

def bfs(i, j): # bfs를 통해 바이러스 감염
    que = deque()
    que.append((i, j))

    while que:
        si, sj = que.popleft()
        for di, dj in ((1,0), (-1, 0), (0, 1), (0, -1)):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < M and new_arr[ni][nj] == 0:
                que.append((ni, nj))
                new_arr[ni][nj] = 2

    return new_arr



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

wall = [] # 벽이 위치할 수 있는 리스트
covid = [] # 현재 바이러스가 있는 위치
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            wall.append((i, j))

        if arr[i][j] == 2:
            covid.append((i, j))
max_cnt = 0
for c in combinations(wall, 3):
    new_arr = copy.deepcopy(arr)
    for x, y in c: # 벽 세우기
        new_arr[x][y] = 1
    for lst in covid: # 바이러스 감염
        bfs(lst[0], lst[1])
    cnt = 0
    for lst in new_arr: # 감염 후 안전 구역 찾기
        cnt += lst.count(0)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)

