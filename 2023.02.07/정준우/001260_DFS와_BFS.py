num_of_vertex, num_of_edge, start_vertex = map(int, input().split())

# 주어진 입력값을 딕셔너리 형태로 바꾸기 위한 작업
graph = {i: [] for i in range(1, num_of_vertex + 1)}

for i in range(1, num_of_edge + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()


def dfs(graph, root, visited=[]):
    # 방문 기록에 시작 정점 추가
    visited.append(root)

    # 시작 정점의 하위 노드들에 대해, 방문 기록에 없다면 추가하고
    # 하위 노드의 하위 노드들에 대해 다시 위 과정 반복

    for node in graph[root]:
        if node not in visited:
            dfs(graph, node, visited)

    # 탐색 종료 후 방문 기록 반환
    return visited



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

for _ in dfs(graph, start_vertex):
    print(_, end = ' ')
print('')
for _ in bfs(graph, start_vertex):
    print(_, end = ' ')