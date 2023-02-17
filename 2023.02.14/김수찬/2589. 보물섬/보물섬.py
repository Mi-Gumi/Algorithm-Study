from collections import deque


N, M = map(int,input().split())

mapp = []
for _ in range(N):
  mapp.append(list(input()))


def fnd_L():
  temp = 0
  for i in range(N):
    for j in range(M):
      if mapp[i][j] == 'W': continue
      m = bfs(i,j)
      if temp < m:
        temp = m
  return temp

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  is_travel = [[False for _ in range(M)] for _ in range(N)]
  que = deque()
  que.append((x,y,0))
  Max = 0
  while que:
    now = que.popleft()
    i,j,d = now[0], now[1],now[2]
    if Max < d: 
      Max = d
    if is_travel[i][j]: 
      continue
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if nx < 0 or ny < 0 or nx >= N or ny >= M: 
        continue
      if mapp[nx][ny] == 'W': 
        continue
      is_travel[i][j] = True
      que.append((nx,ny,d+1))
  return Max-1


print(fnd_L())