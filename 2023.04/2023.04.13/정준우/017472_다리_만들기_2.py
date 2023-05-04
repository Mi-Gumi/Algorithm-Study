from sys import stdin
from collections import deque


# BFS를 통해 섬마다 다른 숫자로 땅을 지정해줘 구분하는 함수
def island_divide(island_y, island_x, island_no):

    queue_for_divide = deque()
    queue_for_divide.append((island_y, island_x))

    country[island_y][island_x] = island_no

    visited[island_y][island_x] = 'visited'

    while queue_for_divide:

        current_y, current_x = queue_for_divide.popleft()

        for y, x in check:
            new_y = current_y + y
            new_x = current_x + x

            if 0 <= new_y < country_row_size and 0 <= new_x < country_col_size:
                if country[new_y][new_x] != 0 and visited[new_y][new_x] == 'not visited':

                    country[new_y][new_x] = island_no

                    visited[new_y][new_x] = 'visited'

                    queue_for_divide.append((new_y, new_x))


# 네 방향으로 뻗어나가며 다리를 지어보고, 조건에 맞는 다리만 bridge_case 에 넣는 함수
def set_bridges(island_y, island_x, current_island_no):

    queue_for_set_bridges = deque()

    for direction in range(4):
        queue_for_set_bridges.append((island_y, island_x, 0, check[direction]))

    while queue_for_set_bridges:

        current_y, current_x, bridge_length, current_direction = queue_for_set_bridges.popleft()

        if country[current_y][current_x] != 0 and country[current_y][current_x] != current_island_no:

            if bridge_length > 2:
                bridge_case.add((bridge_length - 1, current_island_no, country[current_y][current_x]))

            continue

        new_y = current_y + current_direction[0]
        new_x = current_x + current_direction[1]

        if new_y < 0 or new_y >= country_row_size or new_x < 0 or new_x >= country_col_size or country[new_y][new_x] == current_island_no:
            continue

        queue_for_set_bridges.append((new_y, new_x, bridge_length + 1, current_direction))


# 크루스칼
def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


country_row_size, country_col_size = map(int, stdin.readline().split())

country = [list(map(int, stdin.readline().split())) for _ in range(country_row_size)]

visited = [['not visited'] * country_col_size for _ in range(country_row_size)]

# 같은 다리 지우기 위한 set
bridge_case = set()

check = [(-1, 0), (0, 1), (1, 0), (0, -1)]

island_no = 1

for row in range(country_row_size):
    for col in range(country_col_size):

        # 새로 찾는 섬마다 번호 +1 해서 구분
        if country[row][col] != 0 and visited[row][col] == 'not visited':
            island_divide(row, col, island_no)
            island_no += 1

for row in range(country_row_size):
    for col in range(country_col_size):

        if country[row][col] != 0:

            # 겹치는 다리도 탐색해주기 위해 이 위치에서 visited 초기화
            visited = [['not visited'] * country_col_size for _ in range(country_row_size)]

            set_bridges(row, col, country[row][col])

# 서로 다른 섬을 잇는 다리 중 가장 짧은 것을 우선으로 사용하기 위한 정렬
bridge_case = sorted(list(bridge_case))

parent = [i for i in range(island_no)]

min_bridge_length = 0

num_of_bridges = 0

for bridge_length, island_no_1, island_no_2 in bridge_case:

    if find_parent(parent, island_no_1) != find_parent(parent, island_no_2):
        num_of_bridges += 1
        union(parent, island_no_1, island_no_2)
        min_bridge_length += bridge_length

# 안 이어진 섬이 있을 경우
if num_of_bridges != island_no - 2:
    print(-1)
else:
    print(min_bridge_length)
