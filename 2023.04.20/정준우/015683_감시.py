from sys import stdin
from copy import deepcopy


# cctv가 볼 수 있는 방향 중 하나로 뻗어나가며 감시 가능 구역 체크
def watch(temp_office, cctv_y, cctv_x, direction):

    new_y = cctv_y + check[direction][0]
    new_x = cctv_x + check[direction][1]

    while 0 <= new_y < office_row_size and 0 <= new_x < office_col_size and temp_office[new_y][new_x] != 6:

        if temp_office[new_y][new_x] == 0:
            temp_office[new_y][new_x] = 'watching'

        new_y += check[direction][0]
        new_x += check[direction][1]

    return


# cctv 방향 하나씩 설정해보는 함수
def setting(office, cctv_no):

    global min_blind_spots

    # cctv 전부 방향 설정 해봤으면 사각지대가 몇 개인지 체크하고 이전 결과와 비교
    if cctv_no == len(cctv_list):

        blind_spots = 0

        for row in range(office_row_size):
            for col in range(office_col_size):

                if office[row][col] == 0:
                    blind_spots += 1

        min_blind_spots = min(min_blind_spots, blind_spots)

        return

    cctv_y, cctv_x, cctv_type = cctv_list[cctv_no]

    # 각 cctv마다 바라볼 수 있는 방향 모두로 watch 함수 수행
    if cctv_type == 1:
        for direction in range(4):
            temp_office = deepcopy(office)
            watch(temp_office, cctv_y, cctv_x, direction)
            setting(temp_office, cctv_no + 1)

    elif cctv_type == 2:
        for direction in range(2):
            temp_office = deepcopy(office)
            watch(temp_office, cctv_y, cctv_x, direction)
            watch(temp_office, cctv_y, cctv_x, direction + 2)
            setting(temp_office, cctv_no + 1)

    elif cctv_type == 3:
        for direction in range(4):
            temp_office = deepcopy(office)
            watch(temp_office, cctv_y, cctv_x, direction)
            watch(temp_office, cctv_y, cctv_x, (direction + 1) % 4)
            setting(temp_office, cctv_no + 1)

    elif cctv_type == 4:
        for direction in range(4):
            temp_office = deepcopy(office)
            watch(temp_office, cctv_y, cctv_x, direction)
            watch(temp_office, cctv_y, cctv_x, (direction + 1) % 4)
            watch(temp_office, cctv_y, cctv_x, (direction + 2) % 4)
            setting(temp_office, cctv_no + 1)

    elif cctv_type == 5:
        temp_office = deepcopy(office)
        watch(temp_office, cctv_y, cctv_x, 0)
        watch(temp_office, cctv_y, cctv_x, 1)
        watch(temp_office, cctv_y, cctv_x, 2)
        watch(temp_office, cctv_y, cctv_x, 3)
        setting(temp_office, cctv_no + 1)


office_row_size, office_col_size = map(int, stdin.readline().split())

office = [list(map(int, stdin.readline().split())) for _ in range(office_row_size)]

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cctv_list = []

for row in range(office_row_size):
    for col in range(office_col_size):
        if office[row][col] not in (0, 6):
            cctv_list.append((row, col, office[row][col]))

min_blind_spots = office_row_size * office_col_size

setting(office, 0)

print(min_blind_spots)
