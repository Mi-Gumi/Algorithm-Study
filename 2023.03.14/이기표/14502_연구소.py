'''
빈 공간 위치 저장 and Combination 진행
안정 영역 빈공간의 최대 크기 출력
bfs 후 0의 영역 count(0)
'''
from itertools import combinations
from collections import deque
import copy

def bfs(i, j):
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

wall = []
covid = []
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
    for lst in covid: # 바이러스
        bfs(lst[0], lst[1])
    cnt = 0
    for lst in new_arr:
        cnt += lst.count(0)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)

