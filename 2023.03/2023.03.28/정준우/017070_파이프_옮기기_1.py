import sys


# 파이프의 한 쪽 끝만 생각
def move_pipe(end_y, end_x, direction):

    global cases

    if end_y == house_size - 1 and end_x == house_size - 1:
        cases += 1

    else:
        # 가로 방향으로 이동하는 경우
        if direction == 'horizontal' or direction == 'diagonal':
            if end_x + 1 < house_size and house[end_y][end_x + 1] == 0:
                move_pipe(end_y, end_x + 1, 'horizontal')

        # 세로 방향으로 이동하는 경우
        if direction == 'vertical' or direction == 'diagonal':
            if end_y + 1 < house_size and house[end_y + 1][end_x] == 0:
                move_pipe(end_y + 1, end_x, 'vertical')

        # 대각선 방향으로 이동하는 경우
        if end_y + 1 < house_size and end_x + 1 < house_size:
            if house[end_y + 1][end_x] == 0 and house[end_y][end_x + 1] == 0 and house[end_y + 1][end_x + 1] == 0:
                move_pipe(end_y + 1, end_x + 1, 'diagonal')


house_size = int(sys.stdin.readline())

house = [list(map(int, sys.stdin.readline().split())) for _ in range(house_size)]

cases = 0

move_pipe(0, 1, 'horizontal')

print(cases)
