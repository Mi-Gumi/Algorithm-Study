# [Silver II] DFS와 BFS - 1260 

[문제 링크](https://www.acmicpc.net/problem/1260) 

### 성능 요약

메모리: 34184 KB, 시간: 72 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

### 출력 

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

---
### Solution
```python
import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(graph, start, visited = []):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        # graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# dfs
def dfs(graph, start, visited = []):
    visited[start] = True
    
    print(start, end=' ')
    # graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

for i in range(M):
    one, two = map(int, input().split())

    graph[one].append(two)
    graph[two].append(one)

# 왜,,, why...? ... 하...
for i in graph:
    i.sort()
    
dfs(graph,V, visited1)
print()
bfs(graph,V, visited2)
