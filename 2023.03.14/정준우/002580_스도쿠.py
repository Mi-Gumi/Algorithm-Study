import sys


# 1 ~ 9 까지의 수 중, 입력받은 좌표에 들어갈 수 없는 수를 제거하고 가능성 있는 수만 남겨두는 함수
def find_number(row, col):
    possible_number = [i for i in range(1, 10)]

    # 가로 판단
    for variable_col in range(9):
        if sudoku_board[row][variable_col] in possible_number:
            possible_number.remove(sudoku_board[row][variable_col])

    # 세로 판단
    for variable_row in range(9):
        if sudoku_board[variable_row][col] in possible_number:
            possible_number.remove(sudoku_board[variable_row][col])

    # 해당 좌표가 들어가있는 3x3칸 판단
    row_for_square = row // 3
    col_for_square = col // 3

    for variable_row in range(row_for_square * 3, row_for_square * 3 + 3):
        for variable_col in range(col_for_square * 3, col_for_square * 3 + 3):
            if sudoku_board[variable_row][variable_col] in possible_number:
                possible_number.remove(sudoku_board[variable_row][variable_col])

    return possible_number


def do_something(filled):
    # 하나씩 채워나가다가 채워넣은 수가 0의 개수와 같으면 결과 출력 후 종료
    if filled == len(zeros):
        print_this()
        return

    zero_row, zero_col = zeros[filled]

    # 해당 좌표에서 가능한 숫자들을 하나씩 넣어가보며 비교
    # 가능한 수가 없다면 해당 칸을 다시 0인 상태로 돌림
    for number in find_number(zero_row, zero_col):
        sudoku_board[zero_row][zero_col] = number
        do_something(filled + 1)
        sudoku_board[zero_row][zero_col] = 0


def print_this():
    for row in range(9):
        print(*sudoku_board[row])
    # 모든 칸이 0일 경우 숫자를 계속 뱉어내서 9줄 출력 후 종료
    # 문제 조건에서는 여러 경우가 있을 경우 하나만 출력하라고 함
    sys.exit()


sudoku_board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

zeros = []

for row in range(9):
    for col in range(9):
        if sudoku_board[row][col] == 0:
            zeros.append((row, col))

do_something(0)
