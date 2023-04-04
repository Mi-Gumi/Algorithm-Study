N, M = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
Map_ = [[-1 for _ in range(M)] for _ in range(N)]
Map_[-1][-1] = 1

dx = (0,0,-1,1)
dy = (1,-1,0,0)
ans = 0

def dfs(start):
  global ans
  x,y = start
  if Map_[x][y] != -1:
    # print(Map_[x][y])
    return Map_[x][y]
  
  Map_[x][y] = 0
  for k in (0,1,2,3):
    nx = x + dx[k]
    ny = y + dy[k]
    
    if nx<0 or ny<0 or nx>=N or ny>=M : continue
    if Map[x][y] <= Map[nx][ny] : continue
    
    Map_[x][y] += dfs((nx,ny))
    
    # if Map_[nx][ny] != 0: 
    #   for i, j in is_travel:
    #     Map_[i][j] += Map_[nx][ny]
    #   continue    
    # is_travel.append((nx,ny))
    # dfs((nx,ny))
    # is_travel.pop()
    
  return Map_[x][y]


is_travel = [(0,0)] # is_travel 을 이용해 dp를 추가하면 시간초과가 뜸
dfs((0,0))
print(Map_[0][0])
