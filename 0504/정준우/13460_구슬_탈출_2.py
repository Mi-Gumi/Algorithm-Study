from sys import stdin
from collections import deque


# 기울였을 때 구슬을 움직이게 하는 함수
def marble_move(current_y, current_x, direction_y, direction_x):

    move_count = 0

    # 벽에 닿기 전이나 구멍에 들어갈 때 까지
    while board[current_y + direction_y][current_x + direction_x] != "#" and board[current_y][current_x] != 'O':

        # 구슬을 기울인 방향에 따라 이동시켜주며 움직인 칸 수도 저장
        current_y += direction_y
        current_x += direction_x

        move_count += 1

    # 구슬의 최종 위치와 움직인 칸 수 반환
    return current_y, current_x, move_count


# 보드를 기울여보는 함수
def turn_board():

    marble_location.append((red_y, red_x, blue_y, blue_x, 1))

    visited[red_y][red_x][blue_y][blue_x] = 'visited'

    while marble_location:

        current_red_y, current_red_x, current_blue_y, current_blue_x, turn_count = marble_location.popleft()

        # 10번 넘게 기울였으면 종료
        if turn_count > 10:
            break

        for direction_y, direction_x in check:

            new_red_y, new_red_x, red_move_count = marble_move(current_red_y, current_red_x, direction_y, direction_x)
            new_blue_y, new_blue_x, blue_move_count = marble_move(current_blue_y, current_blue_x, direction_y, direction_x)

            # 파란 구슬은 구멍에 들어가지 않고, 빨간 구슬만 들어갔다면 기울인 횟수 출력 후 종료
            if board[new_blue_y][new_blue_x] != 'O':
                if board[new_red_y][new_red_x] == 'O':
                    print(turn_count)
                    return

                # 구슬들이 이동 후 같은 위치에 있으려 한다면
                if new_red_y == new_blue_y and new_red_x == new_blue_x:

                    # 더 많이 움직인 구슬이 해당 위치에 더 늦게 도착
                    # 먼저 도착한 구슬이 이미 자리를 차지 중이므로, 늦게 도착한 구슬의 위치 조정
                    if red_move_count > blue_move_count:
                        new_red_y -= direction_y
                        new_red_x -= direction_x

                    else:
                        new_blue_y -= direction_y
                        new_blue_x -= direction_x

                # 만들어본 적 없는 위치 조합이라면, 큐에 추가
                if visited[new_red_y][new_red_x][new_blue_y][new_blue_x] == 'not visited':
                    visited[new_red_y][new_red_x][new_blue_y][new_blue_x] = 'visited'
                    marble_location.append((new_red_y, new_red_x, new_blue_y, new_blue_x, turn_count + 1))
    print(-1)


board_row_size, board_col_size = map(int, stdin.readline().split())

board = [list(stdin.readline().rstrip()) for _ in range(board_row_size)]

check = ((-1, 0), (0, 1), (1, 0), (0, -1))

marble_location = deque()

visited = [[[['not visited'] * board_col_size for _ in range(board_row_size)] for _ in range(board_col_size)] for _ in range(board_row_size)]

red_y, red_x, blue_y, blue_x = 0, 0, 0, 0

for row in range(board_row_size):
    for col in range(board_col_size):

        if board[row][col] == 'R':
            red_y, red_x = row, col

        elif board[row][col] == 'B':
            blue_y, blue_x = row, col

turn_board()
