import sys

def diffusion():

    # 퍼져나간 미세먼지의 양을 저장하고 원래 배열에 더하기 위한 임시 배열
    # 확산할 때마다 초기화
    array_for_spread_dust = [[0] * house_col_size for _ in range(house_row_size)]

    # 미세먼지가 있는 칸이라면, 해당 칸 주변에 퍼져나갈 수 있는 공간에 1/5만큼 분배
    for row in range(house_row_size):
        for col in range(house_col_size):
            if house[row][col] > 0:
                spread_out_dust = 0

                for y, x in check:
                    new_y = row + y
                    new_x = col + x

                    if 0 <= new_y < house_row_size and 0 <= new_x < house_col_size:
                        # 공기청정기가 있는 공간 제외
                        if house[new_y][new_x] != -1:
                            array_for_spread_dust[new_y][new_x] += house[row][col] // 5
                            spread_out_dust += house[row][col] // 5

                # 퍼져나간 만큼 가운데에서는 미세먼지 제거
                house[row][col] -= spread_out_dust

    # 원래 리스트에 미세먼지 양 갱신
    for row in range(house_row_size):
        for col in range(house_col_size):
            house[row][col] += array_for_spread_dust[row][col]


def circulation():
    def top_circulation():
        direction = 1

        just_before_cell = 0

        # 위쪽 공기청정기의 오른쪽에서 시작
        start_y, start_x = top_air_purifier, 1

        while True:
            new_y = start_y + check[direction][0]
            new_x = start_x + check[direction][1]

            if new_y == -1 or new_y == house_row_size or new_x == -1 or new_x == house_col_size:
                direction = (direction - 1) % 4
                continue

            # 한 바퀴 돌고 다시 공기청정기로 왔을 때
            if start_y == top_air_purifier and start_x == 0:
                break

            # 바로 직전의 칸 안의 미세먼지를 흐름에 따라 옮김
            house[start_y][start_x], just_before_cell = just_before_cell, house[start_y][start_x]

            start_y, start_x = new_y, new_x


    def bottom_circulation():
        direction = 1

        just_before_cell = 0

        start_y, start_x = bottom_air_purifier, 1

        while True:
            new_y = start_y + check[direction][0]
            new_x = start_x + check[direction][1]

            if new_y == -1 or new_y == house_row_size or new_x == -1 or new_x == house_col_size:
                # 위쪽 공기청정기와 진행 방향이 다르니 주의
                direction = (direction + 1) % 4
                continue

            if start_y == bottom_air_purifier and start_x == 0:
                break

            house[start_y][start_x], just_before_cell = just_before_cell, house[start_y][start_x]

            start_y, start_x = new_y, new_x


    top_circulation()
    bottom_circulation()


house_row_size, house_col_size, working_time = map(int, sys.stdin.readline().split())

house = [list(map(int, sys.stdin.readline().split())) for _ in range(house_row_size)]

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for row in range(house_row_size):
    if house[row][0] == -1:
        top_air_purifier = row
        bottom_air_purifier = row + 1
        break

for _ in range(working_time):
    diffusion()
    circulation()

# 공기청정기의 값이 -1이므로 초기값 2로 설정
remain_fine_dust = 2

for row in range(house_row_size):
    remain_fine_dust += sum(house[row])

print(remain_fine_dust)
