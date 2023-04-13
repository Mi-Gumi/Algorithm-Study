def prim(s):

    D[s] = 0
    
    for i in range(V+1):
        min_v = INF
        for v in range(V+1):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v
        
        visited[u] = 1

        for v in range(V+1):
            if adj_mat[u][v] and not visited[v]:
                if D[v] > adj_mat[u][v]:
                    D[v] = adj_mat[u][v]
                    PI[v] = u




INF = 9876543521
V = int(input())
E = int(input())
adj_mat = [[0]*(V+1) for _ in range(V+1)]
D = [INF]*(V+1)
PI = list(range(V+1))
visited = [0]*(V+1)
for i in range(E):
    s,e,d = map(int,input().split())
    adj_mat[s][e] = adj_mat[e][s] = d

total = 0
D[0] = 0
prim(1)
print(sum(D))

