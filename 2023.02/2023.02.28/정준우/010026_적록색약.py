import sys
sys.setrecursionlimit(10 ** 9)

def search(start_y, start_x):
    visited[start_y][start_x] = 'v'

    for y, x in check:
        new_y = start_y + y
        new_x = start_x + x

        if 0 <= new_y < size and 0 <= new_x < size:
            if grid[new_y][new_x] == grid[start_y][start_x] and visited[new_y][new_x] == 0:
                search(new_y, new_x)


size = int(input())

grid = [list(input()) for _ in range(size)]
visited = [[0] * size for _ in range(size)]

ncw_count = 0
cw_count = 0

check = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for row in range(size):
    for col in range(size):
        if visited[row][col] == 0:
            search(row, col)
            ncw_count += 1

# 색약이 보는 그리드를 만들기 위해 값 변경
for row in range(size):
    for col in range(size):
        if grid[row][col] == 'G':
            grid[row][col] = 'R'

# 방문 체크용 배열 초기화
visited = [[0] * size for _ in range(size)]

for row in range(size):
    for col in range(size):
        if visited[row][col] == 0:
            search(row, col)
            cw_count += 1

print(ncw_count, cw_count)
