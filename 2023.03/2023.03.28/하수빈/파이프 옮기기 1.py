import sys
input = sys.stdin.readline


def dfs(r, c, dir):
    if r == N - 1 and c == N - 1:
        return 1
    
    visited[r][c][dir] = 0

    if dir == 0:
        for i in range(2):
            for dr, dc in d[i]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N and not home[nr][nc]):
                    break
            else:
                if visited[nr][nc][i] == -1:
                    visited[r][c][dir] += dfs(nr, nc, i)
                else:
                    visited[r][c][dir] += visited[nr][nc][i]
    elif dir == 1:
        for i in range(3):
            for dr, dc in d[i]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N and not home[nr][nc]):
                    break
            else:
                if visited[nr][nc][i] == -1:
                    visited[r][c][dir] += dfs(nr, nc, i)
                else:
                    visited[r][c][dir] += visited[nr][nc][i]
    else:
        for i in range(1, 3):
            for dr, dc in d[i]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N and not home[nr][nc]):
                    break
            else:
                if visited[nr][nc][i] == -1:
                    visited[r][c][dir] += dfs(nr, nc, i)
                else:
                    visited[r][c][dir] += visited[nr][nc][i]
    return visited[r][c][dir]
    

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
visited = [[[-1, -1, -1] for _ in range(N)] for _ in range(N)]
d = [[[0, 1]], [[0, 1], [1, 0], [1, 1]], [[1, 0]]]
dfs(0, 1, 0)
print(visited[0][1][0])