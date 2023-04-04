import sys

# dfs로 길을 찾은 후 경로의 수를 셀 예정
# 길을 찾은 후 되돌아가는 방식이라 목표 지점에서 탐색 지점까지 경로가 몇 개인지 계산하는 방식
def find_path_end_to_here(start_y, start_x):

    # 탐색 후 목표 지점에 다다르면 1 반환
    if start_y == row_size - 1 and start_x == col_size - 1:
        return 1

    # 경로 수를 세기 전 목표 지점에 도달 가능한 길을 만드는 과정
    # 갈 수 있는 길이라면 blocked 제거하고 값을 0으로 지정
    if path_count_plate[start_y][start_x] == 'blocked':
        path_count_plate[start_y][start_x] = 0

        for y, x in check:
            new_y = start_y + y
            new_x = start_x + x

            # 문제의 이동 가능 조건을 만족한다면, 목표 지점에서 해당 위치까지 올 수 있는 경로의 수를 더해주기
            if 0 <= new_y < row_size and 0 <= new_x < col_size and sejun_map[new_y][new_x] < sejun_map[start_y][start_x]:
                path_count_plate[start_y][start_x] += find_path_end_to_here(new_y, new_x)

    # 마지막에 목표 지점에서 시작 지점까지 갈 수 있는 경로의 수 반환
    return path_count_plate[start_y][start_x]


row_size, col_size = map(int, sys.stdin.readline().split())

sejun_map = [list(map(int, sys.stdin.readline().split())) for _ in range(row_size)]

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

path_count_plate = [['blocked'] * col_size for _ in range(row_size)]

print(find_path_end_to_here(0, 0))
