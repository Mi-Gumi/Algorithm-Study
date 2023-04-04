def dfs(n, check):
    global ans
    if ans == 1: # 정답이 나왔으면 중단
        return
    if check == 4: # 친구관계를 만족하면 정답
        ans = 1
        return
    for i in graph[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, check+1)
            visited[i] = 0

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

ans = 0
for num in range(N): # 모든 수에 대해 친구 탐색
    visited = [0] * N
    visited[num] = 1
    dfs(num, 0)
    if ans: # 정답이 나오면 종료
        break
print(ans)

