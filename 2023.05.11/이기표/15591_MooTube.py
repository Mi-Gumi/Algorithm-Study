'''
1. 동영상들이 서로 연결되어 있으니 양방향 그래프 생성
2. BFS 탐색을 통해 연결된 USADO를 판별(최소값 찾기)
3. USADO가 K보다 크거나 같은 경우는 추천 가능이므로 횟수 증가
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(k, r):
    que = deque()
    visited = [0] * (N+1)
    cnt = 0
    visited[r] = 1
    # 인접한 정점을 큐에 추가
    for node, dis in graph[r]:
        visited[node] = 1
        que.append([node, dis])

    while que:
        node, dis = que.popleft()
        # K 보다 크거나 같은 USADO는 횟수 체크
        if dis >= k:
            cnt += 1
        for n, d in graph[node]:
            # 방문 안한 경우에 최소 USADO를 찾아 큐에 추가
            if visited[n] == 0:
                visited[n] = 1
                que.append([n, min(dis, d)])

    return cnt

N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
# 양방향 그래프 생성
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

# 해당 질문에 따른 bfs탐색 진행
for _ in range(Q):
    k, r = map(int, input().split())
    print(bfs(k, r))