from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    visited = [0] * (n + 1)
    q = deque([1])
    visited[1] = 1
    while q:
        answer = 0
        for _ in range(len(q)):
            now = q.popleft()
            answer += 1
            for v in graph[now]:
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
    return answer