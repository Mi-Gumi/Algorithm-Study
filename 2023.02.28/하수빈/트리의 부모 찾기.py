import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(v):
    for next in tree[v]:
        if not visited[next]:
            visited[next] = v
            dfs(next)

N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[1] = -1
# 양방향 그래프 설정
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 방문 처리하며 dfs 하면 tree와 동일
dfs(1)

for i in range(2, N + 1):
    print(visited[i])