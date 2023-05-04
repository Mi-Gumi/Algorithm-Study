from collections import deque
import sys


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    time = [0]+list(map(int, input().split()))
    mat = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]
    
    for i in range(K):
        s,e = map(int,input().split())
        mat[s].append(e)
        indegree[e] += 1
   
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i]=time[i]
    
    while q:
        a=q.popleft()
        for i in mat[a]:
            indegree[i] -= 1
            dp[i] = max(dp[a]+time[i],dp[i])
            if indegree[i] == 0:
                q.append(i)
    W = int(input())
    print(dp[W])
