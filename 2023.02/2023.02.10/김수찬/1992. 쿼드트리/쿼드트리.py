T = int(input())

matrix = []

for _ in range(T):
  row = list(map(int,list(input().strip())))
  matrix.append(row)

def is_full(mat: list, n): ## 색종이가 Full 인지 아닌지 탐색
  target = mat[0][0] 
  for i in range(n):
    for j in range(n):
      if mat[i][j] != target: return (False, -1)
  return (True, target)

def slc(mat, row:tuple, col:tuple): ## 어디서부터 어디까지 행렬을 만들지 구하는 함수
  node = []
  for i in range(row[0],row[1]): # (row 처음, row 끝)
    node.append(mat[i][col[0]:col[1]]) # (col 처음, col 끝)
  return node

def quad_tree(mat, N):
  check = is_full(mat,N)
  if check[0]: # 만약 탐색을 했을 때 모두 참이라면,
    print(check[1],end="")
    return check[1] # print 하기
  root = mat
  n = N//2
  # root 를 4방향으로 분할
  V = (slc(root,(0,n),(0,n)), slc(root,(0,n),(n,N)), slc(root,(n,N),(0,n)), slc(root,(n,N),(n,N)))
  print("(",end="")
  for node in V:  # 분할한 V 의 node들을 탐색
    quad_tree(node,n) ## quad_tree 재귀 진행
  print(")",end="")


quad_tree(matrix,T)