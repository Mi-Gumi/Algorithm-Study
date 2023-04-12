import sys
input = sys.stdin.readline


def dijkstra(s, e):
    D = [INF] * (N + 1)
    D[s] = 0
    visited = [0] * (N + 1)

    for _ in range(N - 1):
        min_V = INF
        for v in range(1, N + 1):
            # 확정되지 않았고 현재 최소비용보다 낮다면 교체
            if not visited[v] and D[v] < min_V:
                min_V = D[v]
                u = v

        # 확정
        visited[u] = 1

        for v in range(1, N + 1):
            # v가 확정되지 않았고 현재 v의 값보다 u에서 uv경로의 비용을 더한 값이 더 작다면 교체
            if not visited[v] and D[v] > D[u] + adj_mat[u][v]:
                D[v] = D[u] + adj_mat[u][v]
    
    return D[e]
    

N = int(input())
M = int(input())
INF = 10 ** 9
adj_mat = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    # 같은 곳으로 가는 다른 비용의 길이 있을 수 있으므로 min처리
    adj_mat[s][e] = min(adj_mat[s][e], d)
for i in range(N + 1):
    adj_mat[i][i] = 0
s, e = map(int, input().split())

print(dijkstra(s, e))