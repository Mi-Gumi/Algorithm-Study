import sys
input = sys.stdin.readline


def dfs(r, c):
    # 열 끝에 도달하면 1 반환
    if c == C - 1:
        return 1
    
    for dr in d:
        nr = r + dr
        # 진행할 수 있다면
        if 0 <= nr < R and road[nr][c + 1] == '.':
            # 방문처리
            road[nr][c + 1] = 'x'
            # 끝까지 도달할 수 있다면 1 반환
            if dfs(nr, c + 1):
                return 1
    
    return 0


R, C = map(int, input().split())
road = [list(input().strip()) for _ in range(R)]
# 윗 방향부터 탐색
d = (-1, 0, 1)
ans = 0

for i in range(R):
    ans += dfs(i, 0)

print(ans)