from collections import deque
parent = dict()

def bfs(start):
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        is_visited[now] = True
        for item in nodes[now]:
            if is_visited[item] == True: continue
            parent[item] = now
            que.append(item)


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