from sys import stdin
from collections import defaultdict


def dragon_curve(start_x, start_y, direction, generation):

    direction_accumulation = [direction]

    dots[(start_x, start_y)] = 1

    next_x = start_x + check[direction][0]
    next_y = start_y + check[direction][1]

    dots[(next_x, next_y)] = 1

    for _ in range(generation):

        temp_line = []

        for i in range(len(direction_accumulation) - 1, -1, -1):

            next_direction = (direction_accumulation[i] + 1) % 4

            next_x += check[next_direction][0]
            next_y += check[next_direction][1]

            dots[(next_x, next_y)] = 1

            temp_line.append(next_direction)

        direction_accumulation.extend(temp_line)


dots = defaultdict(int)

num_of_curves = int(stdin.readline())

check = ((1, 0), (0, -1), (-1, 0), (0, 1))

for _ in range(num_of_curves):
    start_x, start_y, direction, generation = map(int, stdin.readline().split())

    dragon_curve(start_x, start_y, direction, generation)

num_of_squares = 0

for x, y in list(dots.keys()):

    if dots[x + 1, y] and dots[x, y + 1] and dots[x + 1, y + 1]:
        num_of_squares += 1

print(num_of_squares)
