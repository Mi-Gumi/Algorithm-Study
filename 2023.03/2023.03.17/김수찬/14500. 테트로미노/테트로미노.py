N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

from itertools import combinations # 조합을 활용하여 문제를 풀 예정

dx = (0,0,-1,1)
dy = (1,-1,0,0)
def check(tetromino):
  '''
  테트로미노를 보게 되면 메트릭스와 메트릭스가 연결되는 지점은 3개 이상이다.
  완전탐색을 하게될 때 ,3*2 보다 많은 연결이 찾아지면 테트로미노라 볼 수 있다.
  '''
  cnt = 0
  for a,b in tetromino:
    for k in (0,1,2,3):
      na = a+dx[k]
      nb = b+dy[k]
      if na<0 or nb<0 or na>=N or nb>=M: continue
      if (na,nb) in tetromino:
        cnt += 1
  return True if cnt >= 6 else False


tetromino = set()

result = 0
mx_col = 0
mx_row = 0
for items in combinations(range(0,8), 4): 
  '''
  Idea : 
  0,1,2,3,4,5,6,7 번의 숫자 가 있을 때
  2 로 나누었을 때 몫과 나머지로 4*2 matrix를 만들 수 있다
  (0,0), (0,1)
  (1,0), (1,1)
  (2,0), (2,1)
  (3,0), (3,1)

  4로 나누었을 때는 몫과 나머지로 2*4 matrix를 만들 수 있다.
  (0,0), (0,1), (0,2), (0,3)
  (1,0), (1,1), (1,2), (1,3)
  이 중에서 4가지를 뽑아 테트로미노를 만들 수 있을 때 계산을 하여
  최대값을 찾는다
  '''
  tet_col = tuple() # column 방향의 matrix를 생성
  tet_row = tuple() # row 방향의 matrix 생성
  
  ## 테트로미노 찾기
  for idx in items:
    ## col_case
    r_r = idx // 2
    r_c = idx % 2
    tet_col += ((r_r,r_c),)
    ## row_case
    c_r = idx//4
    c_c = idx%4
    tet_row += ((c_r,c_c),)
  

  ## col 방향 테트로미노에 대해서
  if check(tet_col): 
    for i in range(N - 3):
      for j in range(M - 1):
        _sum = 0
        for x,y in tet_col:
          _sum += matrix[i+x][j+y]
        mx_col = _sum if _sum > mx_col else mx_col # col 방향의 테트로미노 중 큰 것 찾기
    
  ## row 방향 테트로미노에 대해서
  if check(tet_row): 
    for i in range(N - 1):
      for j in range(M - 3):
        _sum = 0
        for x,y in tet_row:
          _sum += matrix[i+x][j+y]
        mx_row = _sum if _sum > mx_row else mx_row # row 방향의 테트로미노 중 큰 것 찾기
  
  result = max(result,mx_col,mx_row) # 큰 것들 중에서 가장큰것을 찾으면 정답이 나온다.
print(result)
