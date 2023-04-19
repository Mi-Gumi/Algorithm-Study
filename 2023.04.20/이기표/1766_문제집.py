'''
1. 순서가 있는 싸이클이 없는 그래프이기 때문에 위상정렬 적용
2. 문제 난이도에 따라 앞 번호부터 해결해야하기 때문에 우선순위 큐사용
'''
import heapq, sys
input = sys.stdin.readline

def t_sort(): # 위상 정렬
    heap = []
    rst = []
    for i in range(1, N+1): # 진입차수가 0인 값을 push
        if in_d[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        node = heapq.heappop(heap)
        rst.append(node)
        for v in graph[node]:
            in_d[v] -= 1 # 진입차수 감소
            if in_d[v] == 0: # 진입차수가 0이면 push
                heapq.heappush(heap, v)
    print(*rst)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_d = [0] * (N+1) # 진입차수 리스트
# 기본 문제집 연결
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    in_d[v2] += 1 # 진입차수 증가

t_sort()