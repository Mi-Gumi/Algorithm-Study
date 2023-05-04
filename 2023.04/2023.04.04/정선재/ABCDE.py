def dfs(idx,number):
    global flag
    visited[idx] = 1
    if number == 4:
        flag = 1
        return
    
    for i in arr[idx]:
        if visited[i] == 0 :
            dfs(i, number +1)
    visited[idx] = 0
            

n,m = map(int,input().split())
arr = [[] for _ in range(n)]
visited = [0]*n
flag = 0
for i in range(m):
    r,c = map(int,input().split())
    arr[r].append(c)
    arr[c].append(r)

for i in range(n):
    dfs(i,0)
    visited[i] = 0
    if flag == 1:
        break

print(flag)
