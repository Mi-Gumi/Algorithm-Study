from collections import deque

N = int(input())

K = int(input())


apple = [list(map(int,input().split())) for _ in range(K)]

L = int(input())
turn = [input().split() for _ in range(L)]
turn.reverse()

d = ((0,1),(1,0),(0,-1),(-1,0))
LR = {
    'L' : 3,
    'D' : 1
}
board = [[0]*N for _ in range(N)] 

for i in range(K) :
    row, col = apple[i]
    board[row-1][col-1] = 1

snake = deque()
snake.append((0,0))
head_row = head_col = 0
direction = 0
time = 1
while True :
    head_row = head_row + d[direction][0]
    head_col = head_col + d[direction][1]

    if 0 <= head_row < N and 0 <= head_col < N :
        next_pos = (head_row,head_col)
        if next_pos in snake :
            break
        snake.append(next_pos)
        if board[head_row][head_col] == 1 :
            board[head_row][head_col] = 0 
        else :
            snake.popleft()
    else :
        break
    if turn and time == int(turn[-1][0]) :
        direction = (direction + LR[turn[-1][1]]) % 4
        turn.pop()
    time += 1
    
print(time)
