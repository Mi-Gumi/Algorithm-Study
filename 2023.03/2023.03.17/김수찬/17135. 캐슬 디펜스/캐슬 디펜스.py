
N,M,D = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)] # 게임판

animys = []
def is_finish():
  '''
  게임을 시작할 때, 적군을 탐색한다.
  # 이 때, 왼쪽부터 먼저 잡는다는 조건이 있기 때문에 열방향으로 우선 탐색하는 것이 아니라
  # 행방향으로 우선적으로 탐색을 하여 정렬을 한다.
  '''
  global animys
  animys = []
  Trigger = True
  for j in range(M):           
    for i in range(N-1,-1,-1): 
      if play[i][j] == 1:
        animys.append((i,j))
        Trigger = False
  return True if Trigger else False

from itertools import combinations # 이거도 조합을 사용할 예정 

new_line = [[0] * M] # 한턴이 끝날 때 마다 게임이 끝나는 걸 표시 // 탐색을 할 때 range를 계속 헤아리는 것 보다 좋다고 판단했었음
result = 0
for bows in combinations(range(M), 3): # 궁수의 자리 배치 결정
  play = [arr[:] for arr in matrix]    # 탐색을 위해 deepcopy 진행
  
  kill = 0   # 총 몇명의 적을 죽였나
  while not is_finish():
    
    targets = set() # 화살을 하나의 적이 같이 맞을 수 있다고 했으므로, set을 이용하여 적을 헤아린다.

    for bow in bows: # 모든 궁수에 대해서 적을 탐색한다.
      
      _min = N+M
      target = None
      
      for x,y in animys:
        length = abs(N-x) + abs(bow-y)
        if length <= D:
          if length < _min:           # 왼쪽부터 카운팅을 하기 때문에 중복은 고려하면 안된다.
            _min = length
            target = (x,y)

      if target : targets.add(target) # 잡을 녀석이 있으면 set에 더한다. 
    kill += len(targets) # target 길이만큼 적을 제거
    
    # 타겟들은 죽었습니다..
    for target in targets:
      if not target : continue
      play[target[0]][target[1]] = 0
    play = new_line + play
    play.pop()
  
  # result 중 큰 값을 찾아오자
  result = result if result > kill else kill

print(result)
      
    