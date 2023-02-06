import sys
input = sys.stdin.readline

T = int(input())
link = int(input())
graph = [[] for i in range(T+1)]
visited = [False] * (T+1)  # 노드 방문을 체크

for i in range(link):
    N, E = map(int, input().split())
    graph[N].append(E) # 그래프 추가
    graph[E].append(N) # 그래프 추가


def dfs(v):
    visited[v] = True # 방문 처리

    for i in graph[v]:
        if not visited[i]: # 방문 안했으면 dfs 탐색
            dfs(i)

dfs(1)

ans = -1 # 1을 제외해야하기 때문에 초기값 -1로 설정
for i in visited:
    if i == True:
        ans += 1
print(ans)

