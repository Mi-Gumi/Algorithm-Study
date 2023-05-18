from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]-1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 2:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    queue.append([nx, ny, 1])
                elif matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
                elif matrix[nx][ny] == 1 and z == 1 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])

    return "Fail"

n, m, t = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
res = bfs()

if res == "Fail":
    print(res)
else:
    print(res if res <= t else "Fail")