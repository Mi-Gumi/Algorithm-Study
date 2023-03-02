import sys
input = sys.stdin.readline

# bfs 탐색 함수
def bfs(graph, V):
    # 탐색할 노드 큐
    find_list = [V]
    # 방문한 노드 리스트
    visited = [V]
    # 탐색할 노드가 있다면
    while find_list:
        # 가장 먼저 들어온 노드를 현재 노드로 설정
        now = find_list.pop(0)
        # 현재 노드와 연결된 노드들에 대해
        for next in graph[now]:
            # 연결된 노드가 방문한 노드에 없다면
            if next not in visited:
                # 방문한 노드에 연결된 노드 추가
                visited.append(next)
                # 탐색할 노드에 연결된 노드 추가
                find_list.append(next)
    # 방문한 노드 리스트 반환
    return visited

# dfs 탐색 함수
def dfs(graph, V):
    # 탐색할 노드 스택
    find_list = [V]
    # 방문한 노드 리스트
    visited = []
    # 탐색할 노드가 있다면
    while find_list:
        # 가장 나중에 들어온 노드를 현재노드로 설정
        now = find_list.pop()
        # 현재 노드가 방문한 노드에 없다면
        if now not in visited:
            # 방문한 노드에 현재노드 추가
            visited.append(now)
            # 현재 노드와 연결된 노드들을 역순으로 탐색할 노드에 추가
            find_list.extend(graph[now][::-1])
    # 방문한 노드 리스트 반환
    return visited


N, M, V = map(int, input().split())

# 그래프 선언
graph = [[] for _ in range(N + 1)]

# 시작 노드와 끝 노드를 받아서
for _ in range(M):
    start, end = map(int, input().split())
    # 시작 노드에 끝노드 연결
    graph[start].append(end)
    # 끝 노드에 시작 노드 연결
    graph[end].append(start)

# 오름차순으로 연결된 노드들 정렬
for vtx in graph:
    vtx.sort()

# bfs dfs 실행
bfs_list = bfs(graph, V)
dfs_list = dfs(graph, V)

for num in dfs_list:
    print(num, end=' ')
print()

for num in bfs_list:
    print(num, end=' ')
print()