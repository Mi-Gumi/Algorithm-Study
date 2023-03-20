import sys
input = sys.stdin.readline

def dfs(r, c, cnt):
    global ans
    # 각 알파벳에 맞는 위치에 visited
    visited[ord(board[r][c]) - ord('A')] = 1
    # 다시 dfs
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and not visited[ord(board[nr][nc]) - ord('A')]:
            dfs(nr, nc, cnt + 1)
    # visited 해제
    visited[ord(board[r][c]) - ord('A')] = 0
    # ans 교체
    ans = max(ans, cnt)

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# 알파벳 숫자만큼 visited
visited = [0] * 26
ans = 0

# 0, 0에서 1칸 부터 시작
dfs(0, 0, 1)

print(ans)