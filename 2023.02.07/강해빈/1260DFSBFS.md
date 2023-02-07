# [Silver II] DFS와 BFS - 1260 

[문제 링크](https://www.acmicpc.net/problem/1260) 

### 성능 요약

메모리: 35232 KB, 시간: 1036 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

### 출력 

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

---
```
N, M, V = map(int,input().split()) # N 정점 수, M 간선 수, V 탐색 시작 정점
g = [[] for _ in range(N+1)] # 그래프
visited1 = [False]*(N+1) # dfs 방문 여부
visited2 = [False]*(N+1) # bfs 방문 여부

for i in range(M): # 간선수만큼 for문 돌려
    start, end = map(int,input().split()) # 양방향 연결된 노드까지 넣어 그래프 만들기
    g[start].append(end) # start에 연결되어 있는 노드
    g[end].append(start) # end에 연결되어 있는 노드
# print(g) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
# print(g) # [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]

def dfs(graph, v, visited): # dfs(그래프, 탐색 정점, 방문) # 3
    stack = [] # 후입선출 스택 (가장 깊은 정점 먼저 뽑기)
    visited[v] = True # 탐색 정점 방문 처리
    print(v, end=' ') # 방문된 점 출력 # 3
    for i in sorted(graph[v]): # 방문할 정점 여러개면 오름차순 정렬 # [1, 4]
        if not visited[i]: # i 방문하지 않았으면 # 1
            stack.append(i) # 스택에 추가
            dfs(graph, stack.pop(), visited) # 바로 뽑고 dfs함수로 다시 탐색 고
            # dfs(graph, i, visited) # dfs함수로 다시 탐색 고

dfs(g,V,visited1) # 깊은 부분 우선 탐색 # 3 1 2 5 4 

print() # 줄바꿈

from collections import deque # 선입선출
def bfs(graph, v, visited): # bfs(그래프, 탐색 정점, 방문) 
    queue = deque([v]) # 양쪽 삽입 삭제 연산 덱 자료구조 사용 
    visited[v] = True # 방문 처리
    while queue: # 큐에 값이 있는 동안 계속 돌려
        v = queue.popleft() # 탐색 정점에 큐의 먼저 들어가고 뽑힌 값 할당
        print(v, end=' ') # 방문된 점 출력 
        for i in sorted(graph[v]): # 방문할 정점 여러개면 오름차순 정렬
            if not visited[i]: # i 방문하지 않았으면 
                queue.append(i) # 큐에 추가하고
                visited[i] = True # 방문 처리
           
bfs(g,V,visited2) # 가까운 노드부터 우선 탐색 # 3 1 4 2 5

```
