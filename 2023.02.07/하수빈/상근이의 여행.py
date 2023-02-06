import sys
input = sys.stdin.readline

def bfs(graph, root):
    find_list = [root]
    visited = [root]
    count = 0
    while find_list:
        now = find_list.pop(0)
        for vtx in graph[now]:
            if vtx not in visited:
                visited.append(vtx)
                find_list.append(vtx)
                count += 1
    return count

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    location = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end = map(int, input().split())
        
        location[start].append(end)
        location[end].append(start)
        
    print(bfs(location, 1))


# import sys
# input = sys.stdin.readline

# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         input()
#     print(N - 1)