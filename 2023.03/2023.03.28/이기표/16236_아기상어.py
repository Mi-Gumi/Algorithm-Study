'''
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
'''
from collections import deque
import pprint
def bfs(i, j):
    global size
    que = deque()
    que.append((0, i, j))
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    while que:
        sd, si, sj = que.popleft()
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if 1 <= arr[ni][nj] < size: # 먹이를 먹을 수 있는 곳
                    target.append((sd+1, ni, nj))
                    que.append((sd+1, ni, nj))
                elif 0 <= arr[ni][nj] <= size: # 이동만 가능한 곳
                    que.append((sd+1, ni, nj))
    if target:
        # 가까운 곳부터 탐색
        return sorted(target)[0]

def find():
# 초기 상어위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y = find()
size = 2
ans = cnt = 0
while 1:
    target = []
    target = bfs(x, y)
    if target == None: # 더 이상 먹을 수 있는 먹이가 없는 경우
        break
    # 이동 횟수
    else:
        d, i, j = target
        arr[i][j] = 0
        cnt += 1 # 먹은 횟수
        ans += d # 이동거리
        # 아기 상어 거리
        x, y = i, j
        if cnt == size:
            size += 1
            cnt = 0
print(ans)

