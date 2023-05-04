from sys import stdin
from collections import deque


# 파이어볼의 위치 찾는 함수
def find_fireballs():

    fireball_positions = []

    for row in range(grid_size):
        for col in range(grid_size):
            if len(grid[row][col]):
                fireball_positions.append((row, col))

    return fireball_positions


# 파이어볼을 움직이는 함수
def move_fireballs():

    global grid

    # 현재 파이어볼의 위치들을 찾은 후 진행
    positions = find_fireballs()

    moving_fireballs = []

    for current_y, current_x in positions:

        # 파이어볼이 분리되고 난 후에는 같은 칸에 모두 들어가있기 때문에 해당 칸의 요소 수만큼 반복
        for _ in range(len(grid[current_y][current_x])):

            mass, speed, direction = grid[current_y][current_x].popleft()

            new_y, new_x = (current_y + check[direction][0] * speed) % grid_size, (current_x + check[direction][1] * speed) % grid_size

            moving_fireballs.append([new_y, new_x, mass, speed, direction])

    # 이동 후의 파이어볼 정보를 grid에 적용
    for new_y, new_x, mass, speed, direction in moving_fireballs:
        grid[new_y][new_x].append((mass, speed, direction))


# 합쳐진 파이어볼을 나누는 함수
def divide_fireballs():

    global grid

    positions = find_fireballs()

    dividing_fireballs = []

    for current_y, current_x in positions:

        # 합쳐진 질량, 합쳐진 스피드, 같은 칸에 있는 파이어볼의 수, 방향이 짝수인지, 방향이 홀수인지
        mass_sum, speed_sum, fireballs_count, is_direction_is_even, is_direction_is_odd = 0, 0, 0, False, False

        # 같은 칸에 2개 이상의 파이어볼이 있어 합칠 수 있는 경우
        if len(grid[current_y][current_x]) > 1:

            # 파이어볼 하나씩 판단
            for _ in range(len(grid[current_y][current_x])):

                mass, speed, direction = grid[current_y][current_x].popleft()

                mass_sum += mass
                speed_sum += speed

                fireballs_count += 1

                # 방향이 짝수인지 홀수인지 판단
                if direction % 2 == 0:
                    is_direction_is_even = True

                else:
                    is_direction_is_odd = True

            # 조건에 맞게 질량과 속도 갱신
            mass_after_divided = mass_sum // 5
            speed_after_divided = speed_sum // fireballs_count

            # 질량이 0이 아니라 소멸되지 않았다면
            if mass_after_divided != 0:

                # 방향이 홀수와 짝수가 섞여 있다면
                if is_direction_is_even == True and is_direction_is_odd == True:

                    direction_of_divided_fireballs = [1, 3, 5, 7]

                # 방향이 모두 홀수이거나 모두 짝수라면
                else:
                    direction_of_divided_fireballs = [0, 2, 4, 6]

                for direction in direction_of_divided_fireballs:
                    dividing_fireballs.append([current_y, current_x, mass_after_divided, speed_after_divided, direction])

    # 합쳐진 후 다시 나눠진 파이어볼의 정보를 grid에 갱신
    for row, col, mass, speed, direction in dividing_fireballs:
        grid[row][col].append((mass, speed, direction))


grid_size, num_of_first_fireballs, num_of_move_orders = map(int, stdin.readline().split())

# 한 칸에 여러 파이어볼을 넣기 위해 deque로 칸을 구성
grid = [[deque() for _ in range(grid_size)] for _ in range(grid_size)]

check = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

# 첫 파이어볼의 위치와 정보 지정
for _ in range(num_of_first_fireballs):
    fireball_y, fireball_x, mass, speed, direction = map(int, stdin.readline().split())
    grid[fireball_y - 1][fireball_x - 1].append((mass, speed, direction))

# 이동 명령만큼 함수 수행
for _ in range(num_of_move_orders):
    move_fireballs()
    divide_fireballs()

# 모든 과정을 마친 후의 파이어볼 위치와 정보 파악
positions = find_fireballs()

mass_of_remain_fireballs = 0

# 남아있는 파이어볼의 질량 합
for row, col in positions:

    for _ in range(len(grid[row][col])):
        mass, speed, direction = grid[row][col].popleft()
        mass_of_remain_fireballs += mass

print(mass_of_remain_fireballs)
