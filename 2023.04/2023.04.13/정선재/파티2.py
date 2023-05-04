# dijkstra
'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
9 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
def dijkstra(s):
    D = [INF] * (V+1)
    visited = [0] * (V+1)
    # 출발점 선택
    D[s] = 0

    # 모든 도시 선택
    for i in range(V+1):
        # 방문 안한 정점 and 가중치의 최소값
        min_v = INF
        for v in range(V+1):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v   # 선택된 정점
        # 정점선택 및 방문체크
        visited[u] = 1
        # 정점의 인접 정점의 가중치 갱신
        for v in range(V+1):
            if adj_mat[u][v] and not visited[v]:
                if D[v] > D[u] + adj_mat[u][v]:
                    D[v] = D[u] + adj_mat[u][v]

    return D

INF = 987654321
V, E, X = map(int, input().split())
adj_mat = [[0] * (V+1) for _ in range(V+1)]


for i in range(E):
    s, e, d = map(int, input().split())
    adj_mat[s][e] = adj_mat[e][s] = d

max_v = 0
for i in range(1,V+1):
    D = dijkstra(i)
    c = D[X]  
    D = dijkstra(X)
    if max_v < D[i] + c:
        max_v = D[i] + c

print(max_v)