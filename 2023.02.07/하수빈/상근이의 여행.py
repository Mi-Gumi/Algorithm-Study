import sys
input = sys.stdin.readline

# bfs 탐색 함수
def bfs(graph, V):
    # 탐색할 노드 큐
    find_list = [V]
    # 방문한 노드 리스트
    visited = [V]
    # 사용한 비행기의 갯수
    count = 0
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
                # 비행기의 갯수 + 1
                count += 1
    # 비행기의 갯수 반환
    return count

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 그래프 선언
    location = [[] for _ in range(N + 1)]

    # 시작 여행지와 끝 여행지를 받아서
    for _ in range(M):
        start, end = map(int, input().split())
        # 시작 여행지에 끝 여행지 연결
        location[start].append(end)
        # 끝 여행지에 시작 여행지 연결
        location[end].append(start)
    
    # bfs한 결과로 나온 비행기의 갯수 반환
    print(bfs(location, 1))


# import sys
# input = sys.stdin.readline

# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         input()
#     print(N - 1)