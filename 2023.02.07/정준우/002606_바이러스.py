num_of_computers = int(input())
num_of_edges = int(input())

# 주어진 입력값을 딕셔너리 형태로 바꾸기 위한 작업
graph = {i: [] for i in range(1, num_of_computers + 1)}

for i in range(1, num_of_edges + 1):
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

# 1번 컴퓨터에서 탐색을 시작했을 때 나오는 컴퓨터의 수에서 1번 컴퓨터 제외하기 위해 -1
print(len(dfs(graph, 1)) - 1)