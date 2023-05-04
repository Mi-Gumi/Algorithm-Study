N, M, K = map(int,input().split())

fire_balls = dict()
distances = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
for i in range(M):
  r, c, m, s, d = map(int,input().split())
  fire_balls[i] = [(r-1,c-1),s,d, m] # 파이어볼을 저장

  

def step1(idx, F_ball):
  # 같은 위치에 있는 파이어볼 탐색을 위해 diction선언
  
  # 파이어볼을 이동시킴
  (x,y), s, d, m = fire_balls[F_ball]
  nx = (x + distances[d][0] * s)%N
  ny = (y + distances[d][1] * s)%N
  
  # 이동시킨 파이어볼을 저장
  fire_balls[idx] = [(nx,ny),s,d, m]
  
  # 어느 위치에 중복되어 들어가있는지 확인하기 위해 다른 dictionary에 저장
  if not at_same_pos.get((nx,ny)):
    at_same_pos.setdefault((nx,ny), [])
  at_same_pos[(nx,ny)] += [idx]
  
  return at_same_pos


def check_d(s):                               # 방향을 탐색하는 function
    all_even = all(element % 2 == 0 for element in s)
    all_odd = all(element % 2 != 0 for element in s)
    return all_even or all_odd


def step2(position):
  
  cnt = 0                                     # 파이어볼을 저장하기 위해 cnt 변수 등록
  new_fire_balls = dict()                     # 새로운 파이어볼을 저장하기 위해 dictionary 등록
  
  for x, y in position:                       # 겹친 포지션에 대하여 파이어볼들을 탐색
    total_mass = 0
    total_speed = 0
    total_direct = set()                      # 방향의 중복을 줄이기위해 set로 설정
    items = position[(x,y)]                   # x,y 위치에 있는 파이어볼들의 목록을 가져옴
    
    for item in items:                        # 각정보들을 모두 저장
      (r,c),s,d,m = fire_balls[item]
      total_mass += m
      total_speed += s
      total_direct.add(d)
    
    if len(items) == 1:                       # 겹친 파이어볼이 없을 경우 그대로 저장
      new_fire_balls[cnt] = [(x,y), s, d, m]
      cnt += 1
    else:                                     # 겹친 파이어볼이 있을 경우 문제의 조건을 수행
      new_mass = total_mass//5 
      if new_mass == 0 : continue 
      new_speed = total_speed//len(items)
      new_d = (0,2,4,6) if check_d(total_direct) else (1,3,5,7)

      for a in range(4):
        new_fire_balls[cnt] = [(x,y), new_speed, new_d[a], new_mass]
        cnt += 1
  
  return new_fire_balls



for _ in range(K):
  if len(fire_balls) == 0: break              # 파이어볼이 없을 경우 종료 
  
  at_same_pos = dict()
  for idx, fire_ball in enumerate(fire_balls): # 파이어볼에 대하여 파이어볼의 위치를 이동시킴
    step1(idx, fire_ball)
    
  fire_balls = step2(at_same_pos)              # 파이어볼이 합치는 경우를 계산
  
ans = 0
for key, value in fire_balls.items():
  ans += value[-1]
print(ans)
