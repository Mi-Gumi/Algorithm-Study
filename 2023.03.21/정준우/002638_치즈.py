import sys
sys.setrecursionlimit(10**9)


def find_melting_cheese(outside_air_y, outside_air_x):

    for y, x in check:
        new_y = outside_air_y + y
        new_x = outside_air_x + x

        # 주변 칸의 값이 0이 아니면 (=치즈) +1 해주고 내부 공간을 탐색에서 제외하기 위해 다시 함수에 넣지는 않음
        if 0 <= new_y < row_size and 0 <= new_x < col_size and visited[new_y][new_x] == 0:
            if cheese_plate[new_y][new_x] != 0:
                cheese_plate[new_y][new_x] += 1

            # 주변 칸이 치즈가 아니면 방문 처리 해주고 함수에 위치를 넣어 반복
            else:
                visited[new_y][new_x] = 1
                find_melting_cheese(new_y, new_x)


# 외부 공기 탐색이 끝나면 각 칸의 값에 따라 치즈가 녹는지 아닌지 판단
# 공기에 두 면 이상 닿아있다면 1 + 2 가 되어 값이 최소 3이 되어있을 것이고, 한 면만 닿아있다면 2가 되어있을 것
# 조건에 따라 값이 2인 칸은 다시 치즈를 의미하는 1로 돌려주고, 3 이상이라면 녹아 없어졌으므로 0으로 지정
def prepare_next_hour():

    for row in range(row_size):
        for col in range(col_size):
            if cheese_plate[row][col] == 2:
                cheese_plate[row][col] = 1
            elif cheese_plate[row][col] >= 3:
                cheese_plate[row][col] = 0

# 전체 범위에 치즈가 남아있다면, 반복하기 위해 False 반환
def melting_end():

    for row in range(row_size):
        for col in range(col_size):
            if cheese_plate[row][col] == 1:
                return False

    return True


row_size, col_size = map(int, sys.stdin.readline().split())

cheese_plate = [list(map(int, sys.stdin.readline().split())) for _ in range(row_size)]

hours = 0

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 언제 끝날지 모르니 계속 반복
while True:
    # 치즈가 모두 녹았으면 지금까지 지난 시간을 출력하고 중단
    if melting_end():
        print(hours)
        break

    visited = [[0] * col_size for _ in range(row_size)]

    find_melting_cheese(0, 0)

    prepare_next_hour()

    hours += 1

    visited[0][0] = 1
