import heapq
def dijkstra(start):
    # 1. 출발점 세팅
    heap = []
    
    heapq.heappush(heap, (0,start))
    visited[start] = 0
    # 2. 반복(NXN)
    while heap:
        d, start = heapq.heappop(heap)

        if visited[start] < d :
            continue
        
        for nw, nx in adj_mat[start]:
            nd = d + nw

            if visited[nx] > nd:
                heapq.heappush(heap, (nd,nx))
                visited[nx] = nd
        

V = int(input())
E = int(input())
adj_mat = [[] for _ in range(V+1)]
visited = [1e9]*(V+1)

for i in range(E):
    s, e, d = map(int,input().split())
    adj_mat[s].append((d,e))

start, end = map(int,input().split())

dijkstra(start)
print(visited[end])
