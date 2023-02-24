import sys

def set_queen(current_row):

    global able_count

    # 모든 퀸이 제대로 놓아져서 마지막 행까지 탐색되면 놓을 수 있는 경우의 수 +1
    if current_row == size:
        able_count += 1
        return

    # [행 - 해당 행에 퀸을 놓은 열] 관계만 필요하기 때문에, 이차원 배열을 사용할 필요까지는 없음
    # queened의 인덱스는 행, 각 행의 값은 해당 행에 퀸을 놓은 열의 인덱스
    else:
        for col in range(size):
            queened[current_row] = col

            # 놓을 수 있는 곳에 퀸을 놓았다면, 다음 행으로 가서 퀸을 놓는 과정 반복
            if possible(current_row):
                set_queen(current_row + 1)


def possible(current_row):
    # 현재 판단 중인 행 전의 행에서 같은 열에 퀸이 있는지, 대각선 방향에 퀸이 있는지 판단
    # 현재 행 이후로는 놓여진 퀸이 없으니 현재 행 전까지만 탐색하도록 범위 설정
    # (현재 행 - 비교하려는 행) 과 [현재 열 - 비교하려는 열] 의 값이 같다면, 두 지점은 대각선상에 놓인 것
    for prev_row in range(current_row):
        if queened[current_row] == queened[prev_row]:
            return False
        elif abs(queened[current_row] - queened[prev_row]) == current_row - prev_row:
            return False

    return True


size = int(sys.stdin.readline())

able_count = 0

queened = [0] * size

set_queen(0)

print(able_count)
