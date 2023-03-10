from collections import deque

N = int(input())

K = int(input())

apple = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
turn = [input().split() for _ in range(L)]
turn.reverse()
# pop하기 위함

d = ((0,1),(1,0),(0,-1),(-1,0))
LR = {
    'L' : 3, # 3을 더해주고 4로 나머지를 취하면 -1한 것과 같다
    'D' : 1
}

board = [[0]*N for _ in range(N)] 
# 사과 마킹
for i in range(K) :
    row, col = apple[i]
    board[row-1][col-1] = 1
# 뱀
snake = deque()
snake.append((0,0))
# 머리 좌표와 방향
head_row = head_col = 0
direction = 0
time = 1
while True :
    # 일단 머리 이동
    head_row = head_row + d[direction][0]
    head_col = head_col + d[direction][1]
    # 머리 인덱스 체크
    if 0 <= head_row < N and 0 <= head_col < N :
        # 머리 위치
        next_pos = (head_row,head_col)
        # 몸이랑 겹친다면 break
        if next_pos in snake :
            break
        snake.append(next_pos)
        # 사과 먹었으면 pop하지 않음
        if board[head_row][head_col] == 1 :
            board[head_row][head_col] = 0 
        else :
            snake.popleft()
    else :
        break
    # 회전이 남았고 시간이 같다면
    if turn and time == int(turn[-1][0]) :
        direction = (direction + LR[turn[-1][1]]) % 4
        turn.pop()
    time += 1
    
print(time)
