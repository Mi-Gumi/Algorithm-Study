from collections import deque
parent = dict()

def bfs(start):
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        if is_visited[now] : continue   # 두번 연산 되는 것을 계속 까먹음;; -> 이렇게 해서 방지
        is_visited[now] = True
        for item in nodes[now]:
            if is_visited[item] == True: continue
            parent[item] = now ## 각노드들의 부모노드를 저장해주면 
            que.append(item)

## 이번문제는 탐색 문제로 Root 노드를 1이라 가정을 하였을 때 각 노드들에 대한 
## 부모노드를 찾는 문제
## 1번 노드를 기준으로 탐색을 시작을 해서 is_visited를 활용하여 이전에 탐색한
## 노드들을 지우게 되면 이것은 부모를 탐색한 것과 같은 것이다.
## 따라서 탐색을 진행하고 나서 -- 해주면, 결과를 출력해 줄 수 있다. 
N = int(input())

is_visited = [False for _ in range(N+1)]
nodes = [list() for _ in range(N+1)]
for i in range(N-1):
    s, e = map(int,input().split())
    nodes[s].append(e)
    nodes[e].append(s)
bfs(1)
    
n = sorted(list(parent.items()),key= lambda x: x[0])
for key, value in n:
    print(value)