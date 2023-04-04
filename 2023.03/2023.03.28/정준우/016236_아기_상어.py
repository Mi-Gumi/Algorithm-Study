import sys
from collections import deque


def ddururudduru(baby_shark_y, baby_shark_x):

    # 상어가 움직일 예정인 좌표
    moving_plan = deque()
    # 첫 위치
    moving_plan.append((0, baby_shark_y, baby_shark_x))

    # 일단 먹을 수 있는 물고기 목록 전부 넣어줄 예정
    edible_fish = []

    visited = [['not_visited'] * area_size for _ in range(area_size)]
    visited[baby_shark_y][baby_shark_x] = 'visited'

    while moving_plan:
        current_time, current_y, current_x = moving_plan.popleft()

        for y, x in check:
            new_y = current_y + y
            new_x = current_x + x

            if 0 <= new_y < area_size and 0 <= new_x < area_size:
                if visited[new_y][new_x] == 'not_visited':
                    visited[new_y][new_x] = 'visited'

                    # 움직일 수 있는 칸과 먹을 수 있는 물고기가 있는 칸 구분해서 넣어주기
                    if area[new_y][new_x] == 0 or area[new_y][new_x] == shark_size:
                        moving_plan.append((current_time + 1, new_y, new_x))
                    elif area[new_y][new_x] < shark_size:
                        edible_fish.append((current_time + 1, new_y, new_x))

    # 먹을 수 있는 물고기가 있으면, 문제 조건에 따라 선택하기 위해 거리, 행, 열 순서로 정렬
    if edible_fish:
        edible_fish.sort(key = lambda x: (x[0], x[1], x[2]))
        return edible_fish[0]
    # 도움!
    else:
        return 'help'


# 상어의 처음 위치 찾기
def find_baby_shark():

    global start_y, start_x

    for row in range(area_size):
        for col in range(area_size):
            if area[row][col] == 9:
                start_y = row
                start_x = col
                return


area_size = int(sys.stdin.readline())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(area_size)]

check = ((-1, 0), (0, 1), (1, 0), (0, -1))

time_record = 0

ate_count = 0

shark_size = 2

start_y, start_x = 0, 0
find_baby_shark()

while True:
    do_it_yourself = ddururudduru(start_y, start_x)
    if do_it_yourself == 'help':
        break
    else:
        time_spent, fished_y, fished_x = do_it_yourself

    time_record += time_spent

    # 상어 성장 조건
    ate_count += 1
    if ate_count == shark_size:
        shark_size += 1
        ate_count = 0

    # 물고기 먹고 나서의 상어 위치 갱신
    area[fished_y][fished_x] = 9
    area[start_y][start_x] = 0

    start_y = fished_y
    start_x = fished_x

print(time_record)
