def clean(y, x, direction):

    global cleaned_cell

    while True:
        dirty = False

        # 반시계로 돌며 주변 네 방향에 청소할 칸이 있는지 탐색
        for _ in range(4):
            new_direction = turn(direction)
            new_y = y + check[new_direction][0]
            new_x = x + check[new_direction][1]

            direction = new_direction

            # 청소해야할 칸이 있다면 아래쪽 조건문으로 들어가지 않도록 dirty 변수 변경 후 청소한 칸 +1, 현재 위치 갱신
            if room[new_y][new_x] == 0:
                room[new_y][new_x] = 'c'
                dirty = True
                cleaned_cell += 1
                y, x = new_y, new_x
                break

        # 주변 4칸에 청소할 칸이 없다면 후진
        # 후진하다가 벽에 닿으면 종료 후 청소한 칸 수 반환
        if not dirty:
            backward_y, backward_x = y - check[direction][0], x - check[direction][1]

            if room[backward_y][backward_x] == 1:
                return cleaned_cell
            else:
                y, x = backward_y, backward_x


def turn(direction):
    if direction == 0:
        return 3
    else:
        return direction - 1


row_size, col_size = map(int, input().split())
cleaner_y, cleaner_x, cleaner_direction = map(int, input().split())

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

room = [list(map(int, input().split())) for _ in range(row_size)]

# 처음 놓인 칸 바로 청소
room[cleaner_y][cleaner_x] = 'c'
cleaned_cell = 1

print(clean(cleaner_y, cleaner_x, cleaner_direction))
