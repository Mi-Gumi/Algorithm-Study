import sys
input = sys.stdin.readline


def dfs(s, now, k, v):
    global ans
    
    # 가중치가 이미 ans를 넘었다면 종료
    if v >= ans:
        return
    
    # 모든 마을을 돌았다면
    if k == N - 1:
        # 마지막 마을에서 시작 마을로 가는 길이 있다면
        if W[now][s]:
            # 마지막 마을에서 시작 마을로 가는 가중치 추가
            v += W[now][s]
            # ans 교체 후 종료
            ans = min(ans, v)
        return
    
    for next in range(N):
        if W[now][next] and not visited[next]:
            visited[next] = 1
            dfs(s, next, k + 1, v + W[now][next])
            visited[next] = 0


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans = 10 ** 9

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 0)
    visited[i] = 0

print(ans)