def bfs(v) :
    visited = [0] * (N+1)
    queue = [v]
    visited[v] = 1

    while queue :
        s = queue.pop(0)

        for w in adjL[s] :
            if visited[w] == 0 :
                # 현재 노드가 인접 노드의 부모
                parents[w] = s
                queue.append(w)
                visited[w] = 1

N = int(input())
edge = [list(map(int,input().split())) for _ in range(N-1)]
# 부모만 저장하는 리스트
parents = [0]*(N+1)
# 인접리스트
adjL = [[] for _ in range(N+1)]

for a, b in edge:
    adjL[a].append(b)
    adjL[b].append(a)
# 1을 루트로 bfs 시작
bfs(1)
# 알아낸 부모 정보를 print
for s in range(2,N+1) :
    print(parents[s])