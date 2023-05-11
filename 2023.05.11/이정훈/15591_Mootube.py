from collections import deque
from sys import maxsize
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    p, q, r = map(int,input().split())

    graph[p].append((r, q))
    graph[q].append((r, p))


for _ in range(m) :
    k, video = map(int, input().split())
    
    visited = [0] * (n+1)
    visited[video] = 1
    ans = 0

    Q = deque()
    # 최솟값을 구하기 위해 최대값으로 설정
    Q.append((video, maxsize))

    while Q : 
        now, w  = Q.popleft()
        for nextw, next in graph[now]:
            if not visited[next] :
                usado = min(w, nextw)
                if usado >= k  :
                    Q.append((next, usado))
                    ans += 1
                    visited[next] = 1
    print(ans)
