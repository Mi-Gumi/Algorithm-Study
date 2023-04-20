import sys
import heapq


n, m = map(int, input().split())
mat = [[] for _ in range(n+1)]
indegree = [0 for i in range(n+1)]
heap = []
result = []


for _ in range(m):
    s, e = map(int, input().split())
    mat[s].append(e)
    indegree[e] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
    
while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for j in mat[temp]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(heap, j)
    
for i in result:
    print(i, end=' ')