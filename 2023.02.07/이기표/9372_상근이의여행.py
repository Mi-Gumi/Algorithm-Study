import sys
input = sys.stdin.readline

T = int(input())

def dfs(v):
    visited[v] = True # 방문 처리

    for i in graph[v]:
        if not visited[i]: # 방문 안했으면 dfs 탐색
            dfs(i)

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1) # 노드 방문을 체크

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b) # 그래프 추가
        graph[b].append(a) # 그래프 추가

    dfs(1)

    ans = -1 # 1을 제외해야하기 때문에 초기값 -1로 설정
    for true in visited:
        if true == True:
            ans += 1

    print(ans)


