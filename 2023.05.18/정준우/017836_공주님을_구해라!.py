from sys import stdin
from collections import deque


def rescue(start_y, start_x):

    time = [[-1] * col_size for _ in range(row_size)]
    time[start_y][start_x] = 0

    q = deque([(start_y, start_x)])

    time_with_gram = 0

    while q:
        row, col = q.popleft()

        if (row, col) == (row_size - 1, col_size - 1):    # 목적지까지 정상 도달
            if time_with_gram:
                return min(time[row][col], time_with_gram)

            return time[row][col]

        for y, x in check:
            new_y = row + y
            new_x = col + x

            # 범위 밖으로 나가거나 / 벽이거나 / 이미 방문한 곳이라면 중단
            if not (0 <= new_y < row_size and 0 <= new_x < col_size):
                continue

            if castle[new_y][new_x] == 1 or time[new_y][new_x] > -1:
                continue

            time[new_y][new_x] = time[row][col] + 1
            q.append((new_y, new_x))

            # 그램 구한 시점에서 직선으로 뚫고 가는 시간 구하기
            if castle[new_y][new_x] == 2:
                time_with_gram = time[new_y][new_x] + (abs(row_size - 1 - new_y) + abs(col_size - 1 - new_x))

    # 일반적으로는 끝까지 도달 못 하고 그램은 얻은 상태라면 그램을 사용한 시간만 반환
    if time_with_gram:
        return time_with_gram

    # 완전 실패 시 제한 시간보다 더 큰 숫자를 반환
    return limit + 1


row_size, col_size, limit = map(int, stdin.readline().split())

castle = [list(map(int, stdin.readline().split())) for _ in range(row_size)]

check = ((-1, 0), (0, 1), (1, 0), (0, -1))

rescue_time = rescue(0, 0)

if rescue_time <= limit:
    print(rescue_time)

else:
    print("Fail")
