import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(v, s):
    # 5명 연결된 친구를 찾았다면 종료
    if s == 5:
        print(1)
        sys.exit()

    # 현재 분기에서 연결되지 않은 친구와 연결되어 있는지 탐색
    for next in graph[v]:
        if not visited[next]:
            visited[next] = 1
            dfs(next, s + 1)
            visited[next] = 0

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [0] * N

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N):
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0

print(0)