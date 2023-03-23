import sys
from collections import deque


# 문제 조건에 맞게 숫자를 바꿔주는 과정 후 주사위 윗 면의 숫자 출력
def moving_number(rolled_y, rolled_x):

    if dice_map[rolled_y][rolled_x] == 0:
        dice_map[rolled_y][rolled_x] = dice[5]

    else:
        dice[5] = dice_map[rolled_y][rolled_x]
        dice_map[rolled_y][rolled_x] = 0

    print(dice[0])


row_size, col_size, dice_y, dice_x, num_of_commands = map(int, sys.stdin.readline().split())

dice_map = [list(map(int, sys.stdin.readline().split())) for _ in range(row_size)]

commands = deque(map(int, sys.stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0]

rolled_y, rolled_x = dice_y, dice_x

# 먼저 입력된 명령부터
while commands:
    command = commands.popleft()

    # 주사위의 인덱스는 문제에 그려진 주사위 그림의 숫자 순서 기준
    dice_top, dice_back, dice_right, dice_left, dice_front, dice_bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 굴렸을 때 범위를 벗어나는지부터 판단 후, 현재 놓인 좌표 조정해주고 굴린 방향에 맞게 주사위의 값 수정
    # 동쪽
    if command == 1:
        if 0 <= rolled_y < row_size and 0 <= rolled_x + 1 < col_size:
            rolled_x = rolled_x + 1

            dice[0] = dice_left
            dice[1] = dice_back
            dice[2] = dice_top
            dice[3] = dice_bottom
            dice[4] = dice_front
            dice[5] = dice_right

            # 주사위를 굴려진 상태로 만든 후 지도와 주사위 밑면의 숫자 교환
            moving_number(rolled_y, rolled_x)

    # 서쪽
    if command == 2:
        if 0 <= rolled_y < row_size and 0 <= rolled_x - 1 < col_size:
            rolled_x = rolled_x - 1

            dice[0] = dice_right
            dice[1] = dice_back
            dice[2] = dice_bottom
            dice[3] = dice_top
            dice[4] = dice_front
            dice[5] = dice_left

            moving_number(rolled_y, rolled_x)

    # 북쪽
    if command == 3:
        if 0 <= rolled_y - 1 < row_size and 0 <= rolled_x< col_size:
            rolled_y = rolled_y - 1

            dice[0] = dice_front
            dice[1] = dice_top
            dice[2] = dice_right
            dice[3] = dice_left
            dice[4] = dice_bottom
            dice[5] = dice_back

            moving_number(rolled_y, rolled_x)

    # 남쪽
    if command == 4:
        if 0 <= rolled_y + 1 < row_size and 0 <= rolled_x< col_size:
            rolled_y = rolled_y + 1

            dice[0] = dice_back
            dice[1] = dice_bottom
            dice[2] = dice_right
            dice[3] = dice_left
            dice[4] = dice_top
            dice[5] = dice_front

            moving_number(rolled_y, rolled_x)
