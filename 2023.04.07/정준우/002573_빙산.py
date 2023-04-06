from sys import stdin
from collections import deque
from copy import deepcopy


# 빙산이 있는 칸 주변의 0 수를 세어주는 함수
def check_around_zero(iceberg_y, iceberg_x):
    around_zero_count = 0

    for y, x in check:
        new_y, new_x = iceberg_y + y, iceberg_x + x

        if 0 <= new_y < ocean_row_size and 0 <= new_x < ocean_col_size and ocean[new_y][new_x] == 0:
            around_zero_count += 1

    return around_zero_count


# 현재 바다 위에 떠 있는 빙산 덩어리의 수를 세어주는 함수
def iceberg_count(iceberg_y, iceberg_x):
    checking = deque()
    checking.append((iceberg_y, iceberg_x))

    while checking:
        current_y, current_x = checking.popleft()

        for y, x in check:
            new_y = current_y + y
            new_x = current_x + x

            if 0 <= new_y < ocean_row_size and 0 <= new_x < ocean_col_size:
                if next_year_ocean[new_y][new_x] != 0:

                    # 이미 확인한 빙산은 다시 세지 않도록 0으로 바꿔주기
                    next_year_ocean[new_y][new_x] = 0

                    checking.append((new_y, new_x))


# 빙산이 모두 녹아 없어졌는지 확인하는 함수
def check_all_melted():
    for row in range(ocean_row_size):
        for col in range(ocean_col_size):

            if ocean[row][col] != 0:
                return 'remain'

    return 'all melted'


ocean_row_size, ocean_col_size = map(int, stdin.readline().split())

ocean = [list(map(int, stdin.readline().split())) for _ in range(ocean_row_size)]

check = ((-1, 0), (0, 1), (1, 0), (0, -1))

years = 0

while True:

    years += 1

    # 다 녹았으면 0 출력 후 중단
    if check_all_melted() == 'all melted':
        print(0)
        break

    # 1년 뒤의 바다 상태를 표시할 리스트
    next_year_ocean = [[0] * ocean_col_size for _ in range(ocean_row_size)]

    for row in range(ocean_row_size):
        for col in range(ocean_col_size):

            # 빙산이 있으면
            if ocean[row][col] != 0:

                # 주변의 0 수만큼 빼주기
                after_melt = ocean[row][col] - check_around_zero(row, col)

                # 녹고 나서 해당 칸의 값이 0 이상이라면 그대로 값 부여
                if after_melt >= 0:
                    next_year_ocean[row][col] = after_melt

                # 음수면 0으로 부여
                else:
                    next_year_ocean[row][col] = 0

    # 1년 뒤의 바다 상태를 현재 바다 상태로 복사
    ocean = deepcopy(next_year_ocean)

    icebergs = 0

    for row in range(ocean_row_size):
        for col in range(ocean_col_size):

            # 빙산 덩어리의 개수를 세어
            if next_year_ocean[row][col] != 0:
                iceberg_count(row, col)
                icebergs += 1

    # 빙산이 2덩어리 이상이면 년수 출력하고 중단
    if icebergs >= 2:
        print(years)
        break
