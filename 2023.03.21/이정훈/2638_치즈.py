import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())

arr = [list(map(int,input().rstrip().split())) for _ in range(N) ]

cnt = 0
time = 0

# 치즈 개수 count
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            cnt += 1
# 치즈가 녹을 때까지
while cnt> 0 :
    visited = [[0]*M for i in range(N)]
    queue = deque()
    # 0,0 은 무조건 공기이므로 밖만을 탐색
    queue.append((0,0))
    while queue :
        ci, cj = queue.popleft()
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
            ni,nj = ci + di, cj + dj
            if 0<=ni<N and 0<= nj < M : 
                # 1이 아닐 시 queue에 push
                if arr[ni][nj] != 1 and visited[ni][nj] == 0 :
                    queue.append((ni,nj))
                    visited[ni][nj] = 5
                # 1이면 visited에 += 1
                elif arr[ni][nj] == 1 :
                    visited[ni][nj] += 1
    for i in range(N) :
        for j in range(M) :
            # 2이상 5미만인 경우 녹아야 하는 치즈
            if 1 < visited[i][j] < 5 :
                arr[i][j] = 0
                cnt -= 1
    time +=1
print(time)