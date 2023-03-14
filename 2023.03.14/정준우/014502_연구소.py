import sys
from collections import deque

# 빈 자리에 순서대로 벽을 세워보고 3개의 벽이 세워지면 탐색 시작
# 벽 최대 개수는 3개이므로 벽을 없애고 다른 자리에 놓아보며 반복
def anivia(num_of_walls):
    if num_of_walls == 3:
        virus_spread()
        return

    for row in range(lab_row_size):
        for col in range(lab_col_size):
            if lab[row][col] == 0:
                lab[row][col] = 1
                anivia(num_of_walls + 1)
                lab[row][col] = 0


# BFS
def virus_spread():

    global max_safe_cell

    check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    already_spread = [[0] * lab_col_size for _ in range(lab_row_size)]

    queue = deque()

    for row in range(lab_row_size):
        for col in range(lab_col_size):
            if lab[row][col] == 2:
                queue.append((row, col))
                already_spread[row][col] = 'v'

    while queue:
        virus_y, virus_x = queue.popleft()

        for y, x in check:
            new_y = virus_y + y
            new_x = virus_x + x

            if 0 <= new_y < lab_row_size and 0 <= new_x < lab_col_size:
                if lab[new_y][new_x] == 0 and already_spread[new_y][new_x] == 0:
                    queue.append((new_y, new_x))
                    already_spread[new_y][new_x] = 'v'

    safe_cell = 0

    for row in range(lab_row_size):
        for col in range(lab_col_size):
            if lab[row][col] == 0 and already_spread[row][col] == 0:
                safe_cell += 1

    max_safe_cell = max(max_safe_cell, safe_cell)


lab_row_size, lab_col_size = map(int, sys.stdin.readline().split())

lab = [list(map(int, sys.stdin.readline().split())) for _ in range(lab_row_size)]

max_safe_cell = 0

anivia(0)

print(max_safe_cell)
