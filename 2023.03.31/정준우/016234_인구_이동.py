import sys
from collections import deque


def check_unite(country_y, country_x):

    country = deque([[country_y, country_x]])
    united_country = [(country_y, country_x)]

    while country:

        current_y, current_x = country.popleft()

        for y, x in check:
            new_y = current_y + y
            new_x = current_x + x

            if 0 <= new_y < land_size and 0 <= new_x < land_size and visited[new_y][new_x] == 'not visited':
                if min_population_diff <= abs(land[new_y][new_x] - land[current_y][current_x]) <= max_population_diff:

                    visited[new_y][new_x] = 'visited'

                    country.append([new_y, new_x])
                    united_country.append((new_y, new_x))

    return united_country


land_size, min_population_diff, max_population_diff = map(int, sys.stdin.readline().split())

land = [list(map(int, sys.stdin.readline().split())) for _ in range(land_size)]

check = ((-1, 0), (0, 1), (1, 0), (0, -1))

days = 0

while True:

    visited = [['not visited'] * land_size for _ in range(land_size)]

    united = False

    for row in range(land_size):
        for col in range(land_size):

            if visited[row][col] == 'not visited':
                visited[row][col] = 'visited'
                unite = check_unite(row, col)

                if len(unite) >= 2:

                    united = True

                    after_moved_population = sum([land[y][x] for y, x in unite]) // len(unite)

                    for y, x in unite:
                        land[y][x] = after_moved_population

    if not united:
        break

    days += 1

print(days)
