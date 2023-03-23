import sys


def useless():

    global num_of_passed_cell

    # 이미 봤던 좌표는 탐색에서 제외
    stack = set([(0, 0, board[0][0])]

    while stack:
        current_y, current_x, visited = stack.pop()

        num_of_passed_cell = max(num_of_passed_cell, len(visited))

        for y, x in check:
            new_y = current_y + y
            new_x = current_x + x

            if 0 <= new_y < row_size and 0 <= new_x < col_size and board[new_y][new_x] not in visited:
                stack.add((new_y, new_x, visited + board[new_y][new_x]))


row_size, col_size = map(int, sys.stdin.readline().split())

board = [list(map(str, sys.stdin.readline().strip())) for _ in range(row_size)]

num_of_passed_cell = 0

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

useless()

print(num_of_passed_cell)
