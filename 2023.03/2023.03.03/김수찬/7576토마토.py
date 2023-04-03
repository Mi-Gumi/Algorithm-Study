from collections import deque


def check():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True


M, N = map(int,input().split())

result = 0
box = [list(map(int,input().split())) for _ in range(N)]
is_visited = [[False for _ in range(M)] for _ in range(N)]

dx = (1,-1,0,0)
dy = (0,0,-1,1)

def bfs(lst):
    que = deque()
    depth = 0
    for domado in lst:
        que.append((domado[0],domado[1],depth))
        is_visited[domado[0]][domado[1]] = True

    while que:
        x,y,depth = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
            if box[nx][ny] == -1 or box[nx][ny] == 1: continue
            if is_visited[nx][ny] : continue
            is_visited[nx][ny] = True
            box[nx][ny] = 1

            que.append((nx,ny,depth+1))

    return depth

domados = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1 and not is_visited[i][j]:
            domados.append((i,j))
            # result = max(bfs(i,j),result)

result = bfs(domados)

if check():
    print(result)
else:
    print(-1)