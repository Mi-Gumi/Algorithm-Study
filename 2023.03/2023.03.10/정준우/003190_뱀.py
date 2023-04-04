from collections import deque


def dummy():

    global board

    current_direction = 0
    time = 0

    snake = deque([(0, 0)])

    next_y = next_x = 0

    while True:

        time += 1

        # 시간이 흐르면 현재 방향대로 진행
        next_y += direction[current_direction][0]
        next_x += direction[current_direction][1]

        # 보드 범위를 넘어가거나 몸에 부딪히면 종료
        if next_y < 0 or next_y >= board_size or next_x < 0 or next_x >= board_size or (next_y, next_x) in snake:
            return time

        # 사과를 먹으면 pop 없이 진행하므로 몸 길이는 +1
        # 먹은 사과는 제거
        if board[next_y][next_x] == 'apple':
            board[next_y][next_x] = 0

        # 다음 위치에 사과가 없었다면 꼬리가 위치한 칸 비워주기
        else:
            snake.popleft()

        # 사과 유무에 상관없이 머리는 다음칸에 위치
        snake.append((next_y, next_x))

        # 방향 전환
        if time in turn_info.keys():
            if turn_info[time] == 'L':
                current_direction -= 1
            else:
                current_direction += 1

            # 방향 전환 리스트를 순환시키기 위한 조건
            if current_direction < 0:
                current_direction += 4
            if current_direction >= 4:
                current_direction -= 4


board_size = int(input())
num_of_apples = int(input())

apple = [tuple(map(int, input().split())) for _ in range(num_of_apples)]

board = [[0] * board_size for _ in range(board_size)]

# y와 x는 행과 열 정보기 때문에, 인덱스로 활용하기 위해 -1
for y, x in apple:
    board[y - 1][x - 1] = 'apple'

turns = int(input())

turn_info = {}

# 방향 전환 딕셔너리에 정보 추가
# 받을 때 str 형태로 받았으므로 key값은 int 형태로 변환 필요
for _ in range(turns):
    trigger_time, turn_direction = input().split()
    turn_info[int(trigger_time)] = turn_direction

# 첫 시작인 오른쪽 방향부터 시작해 시계방향으로
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(dummy())
