import heapq
import sys
input = sys.stdin.readline


def prim(s):
    global total
    Q = []
    heapq.heappush(Q, (0, s))
    while Q:
        d, u = heapq.heappop(Q)

        if not visited[u] :
            visited[u] = 1
            total += d

            for w in range(1,n+1) :
                if adj_mat[u][w] :
                    heapq.heappush(Q,(adj_mat[u][w], w))

n = int(input())
m = int(input())

adj_mat = [[0]*(n+1) for _ in range(n + 1)]
visited = [0]*(n+1)
for _ in range(m):
    s, e, w = map(int, input().split())
    adj_mat[s][e] = w
    adj_mat[e][s] = w

total = 0
prim(1)

print(total)
