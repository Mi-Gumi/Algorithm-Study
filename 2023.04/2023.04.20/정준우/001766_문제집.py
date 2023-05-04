# 위상정렬 사용
# 순서가 정해져 있는 일들을 차례대로 수행해야 할 때 사용하는 알고리즘
# 진입차수[특정 노드로 들어오는 간선의 수]가 0인 노드를 큐에 넣고, 큐가 빌 때까지 아래 과정 반복

# 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거하고,
# 새롭게 진입차수가 0이 된 노드를 큐에 삽입

# 현재 풀 수 있는 것 중에서는 가장 쉬운 문제를 풀기 위해 heap 사용
from sys import stdin
from heapq import *


def solve():

    solving_queue = []

    solving_build = []

    # 현재 진입차수가 0이라 풀 수 있는 문제를 solving_queue에 추가
    for problem_no in range(1, len(in_degree)):
        if in_degree[problem_no] == 0:
            heappush(solving_queue, problem_no)

    # 문제를 다 풀 때까지 반복
    while solving_queue:
        current_problem = heappop(solving_queue)
        solving_build.append(current_problem)

        # 현재 문제와 이어져 있는 문제의 진입차수 감소
        for next_problem in build[current_problem]:
            in_degree[next_problem] -= 1

            # 진입차수가 감소 후 0이 되었다면 solving_queue에 추가
            if in_degree[next_problem] == 0:
                heappush(solving_queue, next_problem)

    return solving_build


num_of_problems, num_of_info = map(int, stdin.readline().split())

build = [[] for _ in range(num_of_problems + 1)]

in_degree = [0 for _ in range(num_of_problems + 1)]

for _ in range(num_of_info):
    proceding, trailing = map(int, stdin.readline().split())

    build[proceding].append(trailing)
    # 진입차수 증가
    in_degree[trailing] += 1

print(*solve())
