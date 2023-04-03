N = int(input())
pap = [list(map(int,input().split())) for _ in range(N)]
ans = { -1:0, 0:0, 1:0 }

def checker(row, col, size):
  global pap  
  target = pap[row][col]
  for i in range(row, row + size):
    for j in range(col, col + size):
      if target != pap[i][j]:
        return False
  return True

def solution(row, col, size):
  global ans
  if checker(row, col, size):
    ans[pap[row][col]] += 1
    return

  n_size = size//3  
  for i in range(3):
    for j in range(3):
      # node = (row + i * n_size, col + j * n_size, n_size)
      solution(row + i * n_size, col + j * n_size, n_size)
  # node1 = (row, col, n_size)
  # node2 = (row, col + n_size , n_size)
  # node3 = (row, col + 2 * n_size , n_size)
  # node4 = (row + n_size, col, n_size)
  # node5 = (row + n_size, col + n_size , n_size)
  # node6 = (row + n_size, col + 2 * n_size , n_size)
  # node7 = (row + 2 * n_size, col, n_size)
  # node8 = (row + 2 * n_size, col + n_size , n_size)
  # node9 = (row + 2 * n_size, col + 2 * n_size , n_size)  


solution(0,0,N)
print(*ans.values(), sep='\n')
