from sys import stdin
from heapq import *

# heap을 사용하는 것으로 노드 사이의 최단 거리를 쉽게 뽑아낼 수 있게 함

# 시작 지점에서 각 노드로 향하는 최단 거리를 갱신하는 함수
def find_shortest_route(start_node):

    distance[start_node] = 0

    queue_for_dijkstra = []

    queue_for_dijkstra.append((0, start_node))

    while queue_for_dijkstra:

        # queue에서 distance가 제일 작은 요소를 가져옴
        current_distance, current_node = heappop(queue_for_dijkstra)

        # 다익스트라 알고리즘을 수행하면 이미 처리된 간선의 가중치는 다음에 나올 가중치보다 클 수 없음
        if distance[current_node] < current_distance:
            continue

        for next_node, next_distance in adj_list[current_node]:

            # 다음 노드로 가는 간선들을 모두 탐색해보며 가장 짧은 것을 찾아 거리 리스트에 넣어주고 heap에 추가

            # shortest_route 관련 조건은 일반적인 다익스트라 구현 코드에는 없으나
            # 문제 조건에 따라 최단 거리가 아닌 경로를 따라가야 하므로 구분하기 위해 추가
            # 처음 이 함수가 수행될 때는 모든 값이 False 이므로 영향을 미치지 않음
            if current_distance + next_distance < distance[next_node] and not shortest_route[current_node][next_node]:
                distance[next_node] = current_distance + next_distance
                heappush(queue_for_dijkstra, (distance[next_node], next_node))


# 최단 경로를 표시하기 위한 함수
# 시간 절약을 위해 마지막 노드에서 처음 노드로 되돌아가며 최단 경로인지 판단
def delete_shortest_route(end_node):

    queue_for_delete = []

    queue_for_delete.append((distance[end_node], end_node))

    while queue_for_delete:

        current_distance, current_node = heappop(queue_for_delete)

        if current_node == start_node:
            continue

        for previous_node, previous_distance in reversed_adj_list[current_node]:

            # 이미 최단 경로라고 판단됐다면 과정 생략
            if shortest_route[previous_node][current_node]:
                continue

            # 현재 보는 노드까지의 최단 경로 + 다음 노드까지의 거리 == 다음 노드에 최단 경로로 지정된 값
            # 위 조건을 만족해야 최단 경로에 포함된 간선
            # 최단 경로에 포함된다고 판단된 간선은 shortest_route 에 표시해주며 진행
            if distance[previous_node] == distance[current_node] - previous_distance:
                shortest_route[previous_node][current_node] = True
                heappush(queue_for_delete, (distance[previous_node], previous_node))


while True:

    num_of_nodes, num_of_edges = map(int, stdin.readline().split())

    if num_of_nodes == 0 and num_of_edges == 0:
        break

    start_node, end_node = map(int, stdin.readline().split())

    # 정방향 그래프의 인접 리스트, 역방향 그래프의 인접 리스트 모두 필요
    adj_list = [[] for _ in range(num_of_nodes)]
    reversed_adj_list = [[] for _ in range(num_of_nodes)]

    for _ in range(num_of_edges):
        depart_node, arrive_node, distance_between = map(int, stdin.readline().split())

        adj_list[depart_node].append((arrive_node, distance_between))
        reversed_adj_list[arrive_node].append((depart_node, distance_between))

    distance = [1e9] * num_of_nodes

    shortest_route = [[False] * num_of_nodes for _ in range(num_of_nodes)]

    # 우선 최단 거리를 모두 갱신해주고, 최단 경로에 포함된 간선을 True 로 표현한 인접 행렬 생성
    find_shortest_route(start_node)
    delete_shortest_route(end_node)

    # 거리를 모두 초기화
    distance = [1e9] * num_of_nodes

    # shortest_route 관련 조건으로 인해 최단 거리를 제외하고 탐색하는 함수가 됨
    find_shortest_route(start_node)

    if distance[end_node] == 1e9:
        print(-1)
    else:
        print(distance[end_node])
