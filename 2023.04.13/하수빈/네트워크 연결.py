import sys
import heapq
input = sys.stdin.readline

def prim():
    global ans
    while heap:
        # 연결된 경로 중 우선 순위가 낮은 경로부터 선택
        d, s = heapq.heappop(heap)
        if not visited[s]:
            visited[s] = 1
            # ans에 합산
            ans += d
            for v in graph[s]:
                heapq.heappush(heap, v)

        
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
heap = []
visited = [0] * (N + 1)
ans = 0
heapq.heappush(heap, (0, 1))

#양방향 연결이기 때문에 양쪽 모두 연결
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))
    graph[e].append((d, s))

prim()

print(ans)