
import sys
N = int(input())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

from itertools import permutations

ans = float('inf')
for items in permutations(range(N), N):
  
  target = 0
  for i in range(N):
    target += matrix[items[i]][items[(i+1)%N]]
    if target > ans:
      break
    if matrix[items[i]][items[(i+1)%N]] == 0:
      break
  else:
    ans = min(target, ans)
print(ans)