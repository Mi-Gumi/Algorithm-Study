from collections import deque
N = int(input())


matrix = [list(map(int,input().split())) for _ in range(N)]
S = N//2

def sandblow(sands):
  _10 = int(sands*0.1)
  _7 = int(sands*0.07)
  _5 = int(sands*0.05)
  _2 = int(sands*0.02)
  _1 = int(sands*0.01)
  
  return{
    10:_10, 
    7: _7 , 
    5: _5 , 
    2: _2 , 
    1: _1 ,
    0: sands - 2*(_10 + _7 + _2 + _1) - _5 
    }

def check(target):
  return True if (0<= target < N) else False

def bfs(S):
  
  que = deque()
  que.append([S,S])
  
  cnt = 1
  movement = 1
  total = 0
  
  direction = ((0,-1),(1,0),(0,1),(-1,0))
  d= 0
  while que:
    x, y  = que.popleft()
    
    if (x,y) == (0,-1):
      return total
    
    dx, dy = direction[d]
    for i in range(movement):
      nx = x + dx
      ny = y + dy
      sand = matrix[nx][ny]
      matrix[nx][ny] = 0
      
      send_ = sandblow(sand)
      
      ###############################################
      if check(nx + dx) and check(ny + dy):
        matrix[nx + dx][ny + dy] += send_[0]
      else:
        total += send_[0]
      
      if check(nx + 2*dx) and check(ny + 2*dy):
        matrix[nx + 2*dx][ny + 2*dy] += send_[5]
      else:
        total += send_[5]
      
      if check(nx + dy) and check(ny + dx):
        matrix[nx + dy][ny + dx] += send_[7]
      else:
        total += send_[7]
        
      if check(nx - dy) and check(ny - dx):
        matrix[nx - dy][ny - dx] += send_[7]
      else:
        total += send_[7]
        
        
      if check(nx + 2*dy) and check(ny + 2*dx):
        matrix[nx + 2*dy][ny + 2*dx] += send_[2]
      else:
        total += send_[2]
        
      if check(nx - 2*dy) and check(ny - 2*dx):
        matrix[nx - 2*dy][ny - 2*dx] += send_[2]
      else:
        total += send_[2]
      
      
      if check(nx + dx+dy) and check(ny + dy+dx):
        matrix[nx + dx+dy][ny + dy+dx] += send_[10]
      else:
        total += send_[10]
        
      if check(nx + dx-dy) and check(ny + dy-dx):
        matrix[nx + dx-dy][ny + dy-dx] += send_[10]
      else:
        total += send_[10]
      
      
      if check(nx - dx+dy) and check(ny - dy+dx):
        matrix[nx - dx+dy][ny - dy+dx] += send_[1]
      else:
        total += send_[1]
        
      if check(nx - dx-dy) and check(ny - dy-dx):
        matrix[nx - dx-dy][ny - dy-dx] += send_[1]
      else:
        total += send_[1]
      ###############################################
      x, y = nx, ny
    que.append([x,y])
    
    d = (d+1)%4
    cnt = 1 if cnt == 0 else 0
    movement = movement + cnt
  return total

print(bfs(S))