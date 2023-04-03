import sys
import copy
from itertools import combinations


# 적이 내려오는 것이 아니라, 궁수들이 올라가는 것으로 생각
def look_around(game_map, archer_row, archer_col):

    shoot_area = []

    global kill_list

    # 궁수가 위치한 열 바로 위부터 적 위치 탐색
    for row in range(archer_row - 1, -1, -1):
        for col in range(col_size):
            # 적이 있으면, 거리 판단해서 사정거리 안이면서 이전 결과보다 거리가 짧으면 리스트에 추가
            if game_map[row][col] == 1:
                shoot_distance = distance(archer_row, row, archer_col, col)

                if shoot_distance <= archer_range:
                    shoot_area.append((shoot_distance, col, row))

    # 거리, 열 오름차순으로 정렬 후 조건에 적합한 제일 앞 요소 뽑아내기
    if shoot_area:
        shoot_area.sort()
        kill_list.append((shoot_area[0][2], shoot_area[0][1]))
        return True

    # 쏠 수 있는 적이 없을 때
    return False


def distance(archer_row, row, archer_col, col):
    return abs(archer_row - row) + abs(archer_col - col)


row_size, col_size, archer_range = map(int, sys.stdin.readline().split())

game_map = [list(map(int, sys.stdin.readline().split())) for _ in range(row_size)]
# 궁수의 위치를 넣어줄 행
game_map.append([0] * col_size)

# 궁수가 들어갈 수 있는 열 인덱스 중 크기가 3인 조합 뽑아내기
deployable_col = [i for i in range(col_size)]
deployments = list(combinations(deployable_col, 3))

max_kill_count = 0
archer_who_shot = 0

kill_list = []

for deployment in deployments:
    kill_count = 0
    # 궁수 위치 바뀔때마다 배열 새로 만들지 않고, 원래 있던 맵 깊은 복사해서 사용
    temp_map = copy.deepcopy(game_map)

    # 한 턴이 끝날 때마다 궁수들이 위로 한 줄씩 올라가게 범위 지정
    for archer_row in range(row_size, 0, -1):
        for archer_col in deployment:
            # 세 명의 궁수가 다 쏠 때까지
            if archer_who_shot < 3:
                if look_around(temp_map, archer_row, archer_col):
                    archer_who_shot += 1

        # 턴 끝나면 쏜 횟수 초기화
        archer_who_shot = 0

        # 같은 곳을 동시에 쏠 수도 있으므로, 궁수가 쏘는 위치 모두 얻은 후에 한번에 적 처리
        for enemy in kill_list:
            if temp_map[enemy[0]][enemy[1]] == 1:
                kill_count += 1
                temp_map[enemy[0]][enemy[1]] = 0

        # 이전 턴에 죽인 적은 초기화
        kill_list.clear()

        if max_kill_count < kill_count:
            max_kill_count = kill_count

print(max_kill_count)
