import sys
input = sys.stdin.readline


def dfs(s, nxt, cost, cnt):
    global ans
    if cost > ans:
        return

    if cnt == n-1:
        if adj_mat[nxt][s] != 0:
            ans = min(ans, cost + adj_mat[nxt][s])
        return
    for i in range(n):
        if adj_mat[nxt][i] != 0 and not visited[i]:
            visited[i] = 1
            dfs(s, i, cost + adj_mat[nxt][i], cnt+1)
            visited[i] = 0


n = int(input())

adj_mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = sys.maxsize

for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 0)
    visited[i] = 0

print(ans)
