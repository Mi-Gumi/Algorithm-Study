import sys

def goin_mul():

    total_water = 0

    # 좌우 끝 블록에는 물이 고일 수 없으므로 탐색 범위에서 제외
    for block in range(1, len(blocks) - 1):
        # 현재 탐색 중인 블록의 왼쪽 / 오른쪽에서 블록이 가장 높게 쌓인 위치 찾기
        the_highest_in_left = max(blocks[:block])
        the_highest_in_right = max(blocks[block:])

        # 현재 탐색 중인 블록에서 고일 수 있는 물의 최대량은 좌우 최고 높이 중 낮은 것과 같음
        max_water_height = min(the_highest_in_left, the_highest_in_right)

        # 현재 탐색 중인 블록의 높이가 더 낮아 물이 고인다면 높이 차이가 더해진다
        # 현재 탐색 중인 블록의 높이가 더 높아 물이 고일 수 없다면 0이 더해진다
        total_water += max(max_water_height - blocks[block], 0)

    return total_water


height, width = map(int, sys.stdin.readline().split())

blocks = list(map(int, sys.stdin.readline().split()))

print(goin_mul())
