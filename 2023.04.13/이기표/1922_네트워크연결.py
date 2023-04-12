'''
컴퓨터를 모두 연결해야하고 이때의 비용을 최소로 한다.
1. 최소신장트리 알고리즘을 활용하여 모든 노드(컴퓨터)가 연결되었을 때의 최소 시간 확인
2. 힙큐를 사용하여 프림 알고리즘 구현
'''
import heapq
import sys
input = sys.stdin.readline

def prim(s):
    heap = []
    heapq.heappush(heap, (0, s))
    ans = 0
    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node]: continue
        visited[node] = 1
        ans += dist
        for v, w in graph[node]:
            heapq.heappush(heap, (w, v))
    return ans

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

print(prim(1))
