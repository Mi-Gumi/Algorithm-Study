N = int(input()) # N 보드 크기
K = int(input()) # K 사과 개수
apple = [list(map(int, input().split())) for _ in range(K)] # 사과 위치
L = int(input()) # L 뱀 방향 변환 횟수
xc = [list(map(str, input().split())) for _ in range(L)] # 게임 시작 시간으로부터 X초가 끝난 뒤, 왼L 오D 90도 회전

board = [[1] * (N+2)] + [[1] + [0 for _ in range(N)] + [1] for _ in range(N)] + [[1] * (N+2)]
for k in range(K):
    board[apple[k][0]][apple[k][1]] = 2

s = []
lr = []
for i in range(len(xc)):
    s.append(int(xc[i][0])) # [3, 15, 17]
    lr.append(xc[i][1]) # ['D', 'L', 'D']

d = 0 # 0 오른  1 아래  2 왼  3위 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
second = 0 # 초
snake = [[1, 1]] # 처음 위치 저장

while True:
    second += 1 # 초마다 이동
    # 현재 꼬리 위치 설정
    sx = snake[0][0]
    sy = snake[0][1]
    board[sx][sy] = 3 # 꼬리 위치 처리
    # 방향 따라 다음칸 머리 위치 설정
    nx = sx + dx[d]
    ny = sy + dy[d]

    if board[nx][ny] == 3 or board[nx][ny] == 4 or board[nx][ny] == 1:
        break

    if board[nx][ny] == 2: # 이동한 칸에 사과가 있다면
        board[nx][ny] = 4 # 그 자리에 사과 없애고 머리 위치 처리

    if board[nx][ny] == 0: # 이동한 칸에 사과가 없다면
        # 새로운 꼬리 위치 설정
        # sx = snake[0][0]
        # sy = snake[0][1]
        board[sx][sy] = 0 # 꼬리 비움
        sx += dx[d]
        sy += dy[d]
        snake.append([sx, sy])
        board[sx][sy] = 3  # 새로운 꼬리 위치 처리
        snake.pop(0) # 이전 꼬리 제거

    for j in range(L):
        if second == s[j]:  # X초가 끝난 뒤에 왼쪽 또는 오른쪽 90도 방향 회전
            if lr[j] == 'L':
                d = (d + 3) % 4
            else:
                d = (d + 1) % 4

print(second) # 게임이 몇 초뒤에 끝나는지
