import sys
input = sys.stdin.readline
from collections import deque
import copy

def make_wall(cnt):
    # 벽을 세개 만들었다면 bfs
    if cnt == 3:
        bfs()
        return
    
    # 현재 자리가 빈 땅이라면 벽 세우고 다시 make_wall
    for i in range(N):
        for j in range(M):
            if not _map[i][j]:
                _map[i][j] = 1
                make_wall(cnt + 1)
                _map[i][j] = 0


def bfs():
    global ans
    tmp = copy.deepcopy(_map)
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not tmp[nr][nc]:
                tmp[nr][nc] = 2
                q.append([nr, nc])
    
    result = 0
    for i in range(N):
        for j in range(M):
            if not tmp[i][j]:
                result += 1

    ans = max(ans, result)

N, M = map(int, input().split())
ans = 0
_map = []
virus = []
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 2:
            virus.append([i, j])
    _map.append(tmp)

make_wall(0)

print(ans)