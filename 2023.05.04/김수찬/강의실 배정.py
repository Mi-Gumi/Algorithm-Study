import heapq
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort(key= lambda x: (x[0]))
heap = [lst[0][1]]
ans = 1
for s, e in lst[1:]:
  
  if heap[0] <= s:
    heapq.heappop(heap)
    ans -= 1

  heapq.heappush(heap, e)
  ans += 1
    
print(ans)