# 위상정렬 사용
# 순서가 정해져 있는 일들을 차례대로 수행해야 할 때 사용하는 알고리즘
# 진입차수[특정 노드로 들어오는 간선의 수]가 0인 노드를 큐에 넣고, 큐가 빌 때까지 아래 과정 반복

# 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거하고,
# 새롭게 진입차수가 0이 된 노드를 큐에 삽입
from sys import stdin
from collections import deque


def mine():

    build_queue = deque()

    # 시작하기 전 진입차수가 0인 건물 찾아서 큐에 추가
    for building_no in range(1, num_of_buildings + 1):
        if in_degree[building_no] == 0:
            build_queue.append(building_no)

    while build_queue:

        current_building = build_queue.popleft()

        # 건설을 완성하는 시간은 시작한 시간 + 완성하는 데 드는 시간
        build_complete_time = build_start_time[current_building] + time_need[current_building]

        # 목표 건물이 지어졌다면 종료
        if current_building == target_building:
            return build_complete_time

        # 완성한 건물을 그래프에서 제거하며 이어진 노드들의 진입 차수 갱신
        for next_building in build[current_building]:
            in_degree[next_building] -= 1

            # 다음 건물을 짓기 위해 선행되어야 하는 작업 중 더 오래 걸리는 시간을 건설 시작 시간으로 지정
            build_start_time[next_building] = max(build_start_time[next_building], build_complete_time)

            # 진입차수가 새롭게 0이 된 노드가 있다면 큐에 삽입
            if in_degree[next_building] == 0:
                build_queue.append(next_building)


T = int(stdin.readline())

for test_case in range(1, T+1):

    num_of_buildings, num_of_builds = map(int, stdin.readline().split())

    # 각 건물 별로 짓는 데 필요한 시간
    time_need = [0] + list(map(int, stdin.readline().split()))

    # 진입차수
    in_degree = [0 for _ in range(num_of_buildings + 1)]

    # 연결 관계
    build = [[] for _ in range(num_of_buildings + 1)]

    for _ in range(num_of_builds):
        proceding, trailing = map(int, stdin.readline().split())

        build[proceding].append(trailing)

        in_degree[trailing] += 1

    target_building = int(stdin.readline())

    # 각 건물 별 건설을 시작하는 시간을 의미하는 리스트
    build_start_time = [0 for _ in range(num_of_buildings + 1)]

    print(mine())
