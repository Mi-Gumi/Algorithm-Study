import sys


def set_tetromino(y, x):

    global max_score

    for i in range(19):
        score = 0
        for j in range(4):
            new_y = y + tetrominos[i][j][0]
            new_x = x + tetrominos[i][j][1]

            if new_y < 0 or new_x < 0 or new_y >= row_size or new_x >= col_size:
                break

            score += paper[new_y][new_x]

        max_score = max(max_score, score)


row_size, col_size = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(row_size)]

tetrominos = [
    # ㅡ
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # ㅁ
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # ㄴ
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    # └┐
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (-1, 1)],
    [(0, 0), (0, 1), (1, 0), (1, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    # ㅗ
    [(0, 0), (1, 0), (1, 1), (1, -1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)]
    ]

max_score = 0

for row in range(row_size):
    for col in range(col_size):
        set_tetromino(row, col)

print(max_score)
