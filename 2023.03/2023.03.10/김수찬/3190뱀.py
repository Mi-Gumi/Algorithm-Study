import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())


apples = [[False for _ in range(N)] for _ in range(N)] # 사과에 대한 matrix 설정
for _ in range(K):
    x, y = map(int,sys.stdin.readline().split())
    apples[x-1][y-1] = True # 사과가 있는 영역을 True로 설정함

L = int(sys.stdin.readline())
move = deque([list(map(str,sys.stdin.readline().split())) for _ in range(L)])
# 이동하는 영역에 대한 정보를 받아옴

d = [(0,1),(1,0),(0,-1),(-1,0)] # 나의 방향 기준 왼쪽(-1) 오른쪽(+1) 이 되도록 방향 설정
#    오른    아래   위     왼
def Dummy():
    snake = deque()
    snake.append((0,0)) # snake 시작위치 
    direction = 0

    time = 0
    while True:
        time += 1
        
        x, y = snake[-1] # 뱀의 머리 탐색
        
        # 뱀이 이동하는 다음영역 탐색
        nx = x + d[direction][0]
        ny = y + d[direction][1]

        ## 뱀이 밖으로 나가거나 자기자신이랑 부딛힐 경우 break
        if nx < 0 or ny < 0 or nx>= N or ny >= N:
            break
        if (nx,ny) in snake : 
            break

        # 머리를 부분 append
        snake.append((nx,ny))
        if apples[nx][ny]: # 사과가 있으면 먹고 가만히
            apples[nx][ny] = False
        else: # 사과가 없으면 꼬리를 당김
            snake.popleft()

        if move: # move에 이동하는 cmd가 있다면
            t, D = move[0]
            t = int(t)
            if t == time: # 시간을 비교한 후 사용
                move.popleft()

                D = -1 if D == 'L' else 1 # 이동시키는 cmd
                direction = (direction + D + 4) % 4 # (현재방향 + 이동할 방향 +4)%4
    return time

print(Dummy())