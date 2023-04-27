import sys
input = sys.stdin.readline


A, B = map(int, input().split())
# 9로 초기화
land = [[9] * A for _ in range(B)]
N, M = map(int, input().split())
# 로봇 위치 배열
robot = [0]
_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(N):
    c, r, d = input().split()
    r, c = int(r) - 1, int(c) - 1
    # 방향에 따라 로봇 방향 숫자로 표시
    if d == 'N':
        new_d = 0
    elif d == 'E':
        new_d = 1
    elif d == 'S':
        new_d = 2
    elif d == 'W':
        new_d = 3
    # 로봇 위치 저장
    robot.append([r, c])
    # 지도에 표시
    land[r][c] = new_d

for _ in range(M):
    n, o, c = input().split()
    n, c = int(n), int(c)
    if o == 'L':
        # 왼쪽으로 돌면 -c
        land[robot[n][0]][robot[n][1]] = (land[robot[n][0]][robot[n][1]] - c) % 4
    elif o == 'R':
        # 오른쪽으로 돌면 +c
        land[robot[n][0]][robot[n][1]] = (land[robot[n][0]][robot[n][1]] + c) % 4
    elif o == 'F':
        dr, dc = _dir[land[robot[n][0]][robot[n][1]]]
        nr, nc = robot[n][0], robot[n][1]
        for _ in range(c):
            nr, nc = nr + dr, nc + dc
            # 벽에 부딫히면 종료
            if not (0 <= nr < B and 0 <= nc < A):
                print(f'Robot {n} crashes into the wall')
                sys.exit()
            # 다른 로봇을 만나면 종료
            if land[nr][nc] != 9:
                print(f'Robot {n} crashes into robot {robot.index([nr, nc])}')
                sys.exit()
        # 종료되지 않았다면 로봇 이동
        land[nr][nc] = land[robot[n][0]][robot[n][1]]
        land[robot[n][0]][robot[n][1]] = 9
        robot[n][0], robot[n][1] = nr, nc

print('OK')