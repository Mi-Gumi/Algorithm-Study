from sys import stdin


# 사다리를 타고 내려가서 시작 지점과 도착 지점이 같은 세로선에 있는지 확인하는 함수
def rig_success():

    # 모든 시작 지점 탐색
    for start_idx in range(num_of_vertical_lines):

        current_y, current_x = 0, start_idx

        # 마지막에 시작 지점과 도착 지점을 비교하기 위한 것
        for_check = current_x

        while True:
            # 내려감
            current_y += 1

            # 도착하면 반복 중단
            if current_y == num_of_dashed_lines + 1:
                break

            # 왼쪽에 가로선 있는지 확인하고 있다면 이동
            if current_y - 1 >= 0 and current_x - 1 >= 0 and ladder[current_y - 1][current_x - 1] == 1:
                current_x -= 1
                continue

            # 오른쪽에 가로선 있는지 확인하고 있다면 이동
            if current_y - 1 >= 0 and current_x < num_of_vertical_lines - 1 and ladder[current_y - 1][current_x] == 1:
                current_x += 1
                continue

        # 도착 후 시작 지점과 도착 지점이 같은 세로선 상에 있지 않다면 실패
        if current_x != for_check:
            return False

    # 아니면 성공
    return True


# 가로선 추가해보는 함수
def add_line(add_count, start_searching_y, add_limit):

    global min_add

    # 최대로 추가 가능한 수만큼 가로선을 추가했다면,
    # 조작 성공했는지 판단 후 결과 반환
    if add_count == add_limit:
        if rig_success():
            if min_add > add_limit:
                min_add = add_limit

            return True

        else:
            return False

    # 이전에 가로선을 추가한 줄 위로는 볼 필요 없으므로, start_searching_y를 통해 탐색 범위 줄이기
    for current_row in range(start_searching_y, num_of_dashed_lines):
        for col in range(num_of_vertical_lines - 1):

            # 이미 가로선이 그어져있는 곳이라면 추가 불가능
            if ladder[current_row][col] == 1:
                continue

            # 가로선을 그었을 경우 연속으로 이어지는 가로선이 있는지 판단
            if ladder[current_row][col] == 0:
                if col - 1 >= 0 and ladder[current_row][col - 1] == 1:
                    continue

                if col + 1 < num_of_vertical_lines - 1 and ladder[current_row][col + 1] == 1:
                    continue

            # 가로선 그어보고 백트래킹
            ladder[current_row][col] = 1

            add_line(add_count + 1, current_row, add_limit)

            ladder[current_row][col] = 0


num_of_vertical_lines, num_of_horizontal_lines, num_of_dashed_lines = map(int, stdin.readline().split())

ladder = [[0] * (num_of_vertical_lines - 1) for _ in range(num_of_dashed_lines)]

min_add = 1e9

for _ in range(num_of_horizontal_lines):

    dashed_line, connected_line = map(int, stdin.readline().split())

    ladder[dashed_line - 1][connected_line - 1] = 1

# 추가한 가로선이 4개 이상이라면 조건에 맞지 않으므로
# 0 ~ 3개까지만 그어보도록 설정
for limit in range(4):
    success = add_line(0, 0, limit)

    # 조작 성공한 경우가 있다면 더 탐색할 필요 없음
    if success:
        break

if min_add == 1e9:
    print(-1)

else:
    print(min_add)
