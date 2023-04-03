import sys
from itertools import combinations
from collections import deque


def spread(num_of_empty_cells):

    global min_time

    activated_viruses = deque(list(combination))

    time_spent = 0

    visited = [['not visited'] * lab_size for _ in range(lab_size)]

    for y, x in activated_viruses:
        visited[y][x] = 'visited'

    while activated_viruses:

        if num_of_empty_cells == 0:
            break

        time_spent += 1

        if time_spent >= min_time:
            return 1e9

        for _ in range(len(activated_viruses)):
            current_y, current_x = activated_viruses.popleft()

            for y, x in check:
                new_y = current_y + y
                new_x = current_x + x

                if 0 <= new_y < lab_size and 0 <= new_x < lab_size:
                    if lab[new_y][new_x] != 1 and visited[new_y][new_x] == 'not visited':

                        visited[new_y][new_x] = 'visited'
                        activated_viruses.append((new_y, new_x))

                        if lab[new_y][new_x] == 0:
                            num_of_empty_cells -= 1

    if num_of_empty_cells == 0:
        return time_spent

    else:
        return 1e9


lab_size, can_activate_at_once = map(int, sys.stdin.readline().split())

lab = [list(map(int, sys.stdin.readline().split())) for _ in range(lab_size)]

check = ((-1, 0), (0, 1), (1, 0), (0, -1))

min_time = 1e9

entire_viruses = []

num_of_empty_cells = 0

for row in range(lab_size):
    for col in range(lab_size):

        if lab[row][col] == 2:
            entire_viruses.append((row, col))

        elif lab[row][col] == 0:
            num_of_empty_cells += 1

for combination in combinations(entire_viruses, can_activate_at_once):
    min_time = min(min_time, spread(num_of_empty_cells))

if min_time == 1e9:
    min_time = -1

print(min_time)
