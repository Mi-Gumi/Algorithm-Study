# [Silver II] 트리의 부모 찾기 - 11725 

[문제 링크](https://www.acmicpc.net/problem/11725) 

### 성능 요약

메모리: 65844 KB, 시간: 376 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 트리(trees), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.</p>

### 출력 

 <p>첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.</p>

---
### Solution
```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 부모 찾기용 dfs
def dfs(x):
    visited[x] = 1
    
    for i in V_lst[x]:
        # 방문을 이미 했으면 해당 node의 부모는 i
        if visited[i] == 1:
            result_lst[x] = i
        else:
            dfs(i)

N = int(input())
V_lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result_lst = [0] * (N+1)

# 트리 만들어주기
for _ in range(N-1):
    a, b = map(int, input().split())

    V_lst[a].append(b)
    V_lst[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(result_lst[i])
