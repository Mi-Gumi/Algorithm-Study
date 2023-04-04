def dfs(k, last) :
    global ans
    if ans == 1 :
        return
    if k == 4 :
        ans = 1
        return 
    for i in friend[last] :
        if visit[i] == 0 :
            visit[i] = 1
            dfs(k+1, i)
            visit[i] = 0

n, m = map(int,input().split())

friend = [[] for _ in range(n)]

for i in range(m) :
    a, b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

ans = 0
visit = [0]*n
for start in range(n) :
    visit[start] = 1
    dfs(0,start)
    visit[start] = 0

# for p in permutations(range(n), 5) :
#     for i in range(4) :
#         if p[i] not in friend[p[i+1]] :
#             break
#     else :
#         ans = 1
#         break
print(ans)