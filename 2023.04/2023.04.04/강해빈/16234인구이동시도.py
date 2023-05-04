
N, L, R = map(int, input().split()) # N 배열 크기 L <= 인구차 <= R
P = [list(map(int, input().split())) for _ in range(N)] # 각 나라 인구수
visited = [[0 for _ in range(N)] for _ in range(N)]
union = [[0 for _ in range(N)] for _ in range(N)]
union_xy = []
num = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

from collections import deque

def share(i, j):
    global num
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    num += 1
    union[i][j] = num
    while q:
        x, y = q.popleft()

        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= P[nx][ny] - P[x][y] <= R:
                    union[nx][ny] = num
                    q.append([nx, ny])
share(0,0)                
print(union)
# while True:
    
#     for x in range(N):
#         for y in range(N):
#             share(x, y)

#     pprint(union)
#     hap = 0
#     union_cnt = 0
#     for x in range(N):
#         for y in range(N):
#             hap += union[x][y]
#             if union[x][y] != 0:
#                 union[x][y] 

#     print(hap)

#     move = hap // union_cnt

#     print(move)
