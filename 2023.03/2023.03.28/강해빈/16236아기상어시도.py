
# import sys
# input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치

dx = [0, 1, 0,-1]
dy = [1, 0,-1, 0]

# 아기 상어 크기 2      1초에 상하좌우로 인접한 한 칸씩 이동 
# n <= 2 칸 지나갈 수 있음
# n < 2 먹을 수 있음

# 물고기가 공간에 없으면 종료
cnt = 0
def second():
    global eat_cnt, cnt
    cnt += 1
    
    if eat_cnt == 0:
        return
    if eat_cnt >= 1:
        # 물고기 먹으러간다
        for f in range(4):
            nx = x + dx[f]
            ny = y + dy[f]
            if 0 <= nx < N and 0 <= ny < N:
                if fish[0][0] == nx and fish[0][1] == ny:
                    arr[nx][ny] = 0
                    fish.popleft(0)
                    eat_cnt -= 1
                    second(nx, ny)
                    
    # if eat_cnt > 1:
    #     pass # 거리 가까운 물고기 위 -> 왼 먹으러간다


from collections import deque
eat_cnt = 0
fish = deque()
for x in range(N):
    for y in range(N):
        if 0 < arr[x][y] < 2:
            eat_cnt += 1
            fish.append([x, y])    
            
print(fish, eat_cnt)
second()
print(cnt)
