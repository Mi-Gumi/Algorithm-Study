import sys
import heapq
def dijkstra(start):
    heap = []
    
    heapq.heappush(heap, (0,start,0))

    while heap:
        d, start, k = heapq.heappop(heap)

        if visited[start][k] < d :
            continue
        if k + 1 <= K:
            for nw, nx in adj_mat[start]:

                if visited[nx][k+1] > d:                  
                    visited[nx][k+1] = d
                    heapq.heappush(heap, (d,nx,k+1))
                    
        for nw, nx in adj_mat[start]:
                nd = d + nw
                if visited[nx][k] > nd:       
                    visited[nx][k] = nd
                    heapq.heappush(heap, (nd,nx,k))

V,E,K = map(int,input().split())
adj_mat = [[] for _ in range(V+1)]
visited = [[sys.maxsize]*(K+1) for _ in range(V+1)]

for i in range(E):
    s, e, d = map(int,input().split())
    adj_mat[s].append((d,e))
    adj_mat[e].append((d,s))

for i in range(K+1):
    visited[1][i] = 0

dijkstra(1)
print(min(visited[-1]))
