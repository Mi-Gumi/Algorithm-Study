N = int(input())
edge = list(map(int,input().split()))
node = list(map(int,input().split()))


min_N = node[0]
ans = min_N*edge[0]
for i in range(1,N-1):
  
  if node[i] < min_N:
    min_N = node[i]
  ans += min_N*edge[i]
print(ans)