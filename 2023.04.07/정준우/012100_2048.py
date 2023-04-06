from sys import stdin
from itertools import product
from copy import deepcopy

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(matrix[::-1])
# print(*matrix[::-1])
# print(list(zip(*matrix[::-1])))
# print(list(map(list, zip(*matrix[::-1]))))


# 행렬 90도 회전시키는 함수
def rotate_board_90():

    global board

    board = list(map(list, zip(*board[::-1])))


# 행렬 -90도 회전시키는 함수
def rotate_board_minus_90():

    global board

    board = list(map(list, zip(*board)))[::-1]


# 왼쪽으로 모든 숫자를 이동시키고 합칠 수 있는 숫자는 합치는 함수
def left_push():

    global board

    # 한 줄 단위로 탐색
    for row in range(board_size):

        # 0이 아닌 숫자를 왼쪽으로 다 몰아주기 위해 0을 일단 빼주고 그 숫자만큼 오른쪽에 다시 더해주기
        if 0 in board[row]:
            removed_zero_count = 0

            while 0 in board[row]:
                board[row].remove(0)
                removed_zero_count += 1

            for _ in range(removed_zero_count):
                board[row].append(0)

        # 이미 합쳐진 블록인지 아닌지 판단하기 위한 리스트
        combined_check = ['not combined'] * board_size

        for col in range(board_size - 1):

            # 이어져있는 블록의 숫자가 같다면 합쳐주기
            if board[row][col] == board[row][col + 1]:
                if combined_check[col] == 'not combined' and combined_check[col + 1] == 'not combined':

                    board[row][col] += board[row][col + 1]
                    board[row][col + 1] = 0

                    combined_check[col] = 'combined'
                    combined_check[col + 1] = 'combined'

        # 합쳐지고 나면 오른쪽 보드가 0이 되므로, 0을 제거하는 과정 다시 수행
        if 0 in board[row]:
            removed_zero_count = 0

            while 0 in board[row]:
                board[row].remove(0)
                removed_zero_count += 1

            for _ in range(removed_zero_count):
                board[row].append(0)

    return


# 보드를 회전시켜 왼쪽으로 이동시키는 작업을 수행해도 오른쪽으로 이동시킨 것처럼
def right_push():

    rotate_board_90()
    rotate_board_90()
    left_push()
    # 작업 후 보드 복구
    rotate_board_minus_90()
    rotate_board_minus_90()

    return


# 위
def up_push():

    rotate_board_minus_90()
    left_push()
    rotate_board_90()

    return


# 아래
def down_push():

    rotate_board_90()
    left_push()
    rotate_board_minus_90()

    return


board_size = int(stdin.readline())

origin_board = [list(map(int, stdin.readline().split())) for _ in range(board_size)]

direction = ['left', 'right', 'up', 'down']

# 중복 순열, product(iterable, 순열의 길이)
# product(A, B) == ((x, y) for x in A for y in B)
able_directions = list(product(direction, repeat = 5))

sums = []

for able_direction in able_directions:

    board = deepcopy(origin_board)

    for direction in able_direction:

        if direction == 'left':
            left_push()

        elif direction == 'right':
            right_push()

        elif direction == 'up':
            up_push()

        elif direction == 'down':
            down_push()

    # 각 줄의 최대값을 뽑아낸 후, 그 중에서의 최대값을 sums에 추가
    sums.append(max(map(max, board)))

# 진짜진짜 최대값
print(max(sums))
