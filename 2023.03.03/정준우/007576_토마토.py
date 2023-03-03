from collections import deque


def to_ma_to():

    global day_needed

    check = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:

        day_needed += 1

        # 익은 토마토가 여러 개 있다면 동시에 진행되므로, 큐에 있는 모든 요소 탐색 후 소요 일수 늘려줌
        for _ in range(len(queue)):

            start_y, start_x = queue.popleft()

            for y, x in check:
                new_y = start_y + y
                new_x = start_x + x

                if 0 <= new_y < row_size and 0 <= new_x < col_size and storage[new_y][new_x] == 0:
                    storage[new_y][new_x] = 1

                    queue.append((new_y, new_x))

    # 반복문이 끝났는데도 익지 않은 토마토 있는지 탐색
    for row in range(row_size):
        for col in range(col_size):
            if storage[row][col] == 0:
                return -1

    # 다 익고 나서 한번 더 반복되므로 -1
    return (day_needed - 1)


col_size, row_size = map(int, input().split())

storage = [list(map(int, input().split())) for _ in range(row_size)]

queue = deque()

day_needed = 0

for row in range(row_size):
    for col in range(col_size):
        if storage[row][col] == 1:
            queue.append((row, col))

print(to_ma_to())
