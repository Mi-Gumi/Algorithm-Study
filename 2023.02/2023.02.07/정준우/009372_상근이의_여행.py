import sys

T = int(sys.stdin.readline())

# 모듈로 큐를 구현하기 쉬운 데크 사용
from collections import deque


def bfs(graph, root):
    # root가 포함된 큐 생성
    queue = deque([root])
    # 방문한 노드들을 기록할 빈 리스트 생성
    visited = []

    # 큐가 비어있지 않는 한 반복
    while queue:
        node = queue.pop()

        # 방문 기록에 없다면 추가, 위에서 node를 pop으로 반환하므로,
        # extendleft 를 통해 새 요소를 역순으로 왼쪽에 추가
        # pop 을 수행할 시 먼저 들어와있던 요소를 우선적으로 제거하기 위함
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])

    # 탐색이 끝나면 반복 기록 반환
    return visited


for test_case in range(1, T + 1):
    num_of_countries, num_of_lines = map(int, sys.stdin.readline().split())

    # 주어진 입력값을 딕셔너리 형태로 바꾸기 위한 작업
    graph = {i: [] for i in range(1, num_of_countries + 1)}

    for i in range(1, num_of_lines + 1):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    for key in graph:
        graph[key].sort()

    # 갈 수 있는 국가의 수를 모두 찾고 1을 빼서 경로의 수 찾기
    print(len(bfs(graph, 1)) - 1)

'''
# 모든 국가를 여행한다는 것은 모든 국가가 이어져있다는 말이므로
# 갈 수 있는 국가의 수는 곧 주어진 국가의 수

import sys

T = int(sys.stdin.readline())
for test_case in range(1, T+1):
    num_of_countries, num_of_lines = map(int, sys.stdin.readline().split())
    for _ in range(num_of_lines):
        meaningless_nums = list(map(int, sys.stdin.readline().split()))
        
    print(num_of_countries - 1)
'''