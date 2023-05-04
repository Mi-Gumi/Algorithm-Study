import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline


def bfs(si, sj):
    Q = deque()
    Q.append((si, sj))
    visited[si][sj] = island

    while Q:
        ci, cj = Q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if country[ni][nj] and not visited[ni][nj]:
                    Q.append((ni, nj))
                    visited[ni][nj] = island
# 부모 찾기
def find_set(x) :
    while x != PI[x] :
        x = PI[x]
    return x
# y의 부모를 x의 부모로
def union(x, y) :
    PI[find_set(y)] = find_set(x)

# MST : Kruskal
def MST(graph) :
    cnt = 0 
    total = 0
    for u, v, w in graph :
        if find_set(u) != find_set(v) :
            cnt += 1
            total += w
            union(u, v)
            if cnt == island-1 :
                break
    if cnt != island-1 :
        return -1
    return total

# def prim(u):
#     Q = []
#     D[u] = 0
#     heappush(Q, (0, u))
#     total = 0
#     while Q:
#         d, u = heappop(Q)
#         if D[u] < d or visited[u]:
#             continue
#         visited[u] = 1
#         total += adj_mat[PI[u]][u]
#         for v in range(1, island+1):
#             if adj_mat[u][v]:
#                 if D[v] > adj_mat[u][v] and not visited[v]:
#                     D[v] = adj_mat[u][v]
#                     PI[v] = u
#                     heappush(Q, (D[v], v))

#     return total


n, m = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(n)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 섬 번호매기기
visited = [[0]*m for _ in range(n)]
island = 0
for i in range(n):
    for j in range(m):
        if country[i][j] and not visited[i][j]:
            island += 1
            bfs(i, j)

# print(*visited, sep='\n')

# 간선 구하기
graph = []

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            s = visited[i][j]
            # 네방향
            for di, dj in d:
                k = 1
                while True:
                    ni, nj = i + di*k, j + dj*k
                    # index check 및 같은 섬이 아니면
                    if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] != s:
                        # 0이면 다음으로
                        if not visited[ni][nj]:
                            k += 1
                            continue
                        # 0이 아니면
                        if visited[ni][nj]:
                            e = visited[ni][nj]
                            if k > 2:
                                # 인접행렬
                                # if not adj_mat[s][e] or adj_mat[s][e] > k-1:
                                #    adj_mat[s][e] = k-1

                                # 간선을 그냥 저장
                                graph.append((s, e, k-1))
                            break
                    # index over
                    else:
                        break
graph.sort(key=lambda x : x[2])

inf = 10**9

D = [inf] * (island+1)
D[0] = 1
visited = [0]*(island+1)
PI = list(range(island+1))

ans = MST(graph)
print(ans)

