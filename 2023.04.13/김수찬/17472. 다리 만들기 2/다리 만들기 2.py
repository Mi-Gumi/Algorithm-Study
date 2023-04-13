N,M = map(int,input().split())

from collections import deque

matrix = [list(map(int,input().split())) for _ in range(N)]
is_travel = [[False for _ in range(M)] for _ in range(N)]

dx = (0,0,-1,1)
dy = (1,-1,0,0)

def bfs(start):
    global group, groups
    que = deque()
    que.append(start)

    groups[group] = [(start[0],start[1])]
    
    while que:
        x, y = que.popleft() 
        for d in (0,1,2,3):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny <0 or nx >= N or ny >= M: continue
            if is_travel[nx][ny] : continue
            if matrix[nx][ny] == 0 : continue
            is_travel[nx][ny] = True
            matrix[nx][ny] = group
            groups[group] += [(nx,ny)]
            que.append((nx,ny))
    return
edges = []
def find_route(X,Y,K):
    que2 = deque()
    for d in (0,1,2,3):
        que2.append((X,Y))
        # is_visited = [[False for _ in range(M)] for _ in range(N)]
        # is_visited[X][Y] = True
        bridge = [[0 for _ in range(M)] for _ in range(N)]

        while que2:
            x, y = que2.popleft()
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny <0 or nx >= N or ny >= M: continue
            # if is_visited[nx][ny] : continue
            if matrix[nx][ny] == 0:
                bridge[nx][ny] = bridge[x][y] + 1
                que2.append((nx,ny))
            elif matrix[nx][ny] != K and bridge[x][y] >= 2:
                edges.append((bridge[x][y], K, matrix[nx][ny])) # weight start end
group = 0
groups = dict()
for i in range(N):
    for j in range(M):
        if not is_travel[i][j] and matrix[i][j] == 1:
            group += 1
            is_travel[i][j] = True
            matrix[i][j] = group
            bfs((i,j))
# print(groups)


for k, island in groups.items():
    for x, y in island:
        find_route(x,y,k)


# print("내꺼",edges)
edges.sort()
parent = [i for i in range(group+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

answer= 0
cnt = 0

for w, s, e in edges:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            parent[sRoot] = eRoot
        else:
            parent[eRoot] = sRoot
        cnt += 1
        answer += w
        if cnt == group-1 : break
if cnt == group-1 : print(answer)
else : print(-1)
