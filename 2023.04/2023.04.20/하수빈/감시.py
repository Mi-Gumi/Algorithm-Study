import sys
input = sys.stdin.readline


def check(n):
    global ans
    # 모든 cctv의 방향을 지정했다면
    if n == len(cctv):
        tmp = 0
        # 사각지대 탐색
        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    tmp += 1
        # 최소 사각지대 교체
        ans = min(ans, tmp)
        return

    # cctv의 값에 따라 어떤 방향으로 회전할 지 결정
    r, c = cctv[n][0], cctv[n][1]
    if office[r][c] == 1:
        dir_n = DIR_1
    elif office[r][c] == 2:
        dir_n = DIR_2
    elif office[r][c] == 3:
        dir_n = DIR_3
    elif office[r][c] == 4:
        dir_n = DIR_4
    elif office[r][c] == 5:
        dir_n = DIR_5
    
    # 현재위치 감시 하는 배열에 표시
    visited[r][c] += 1
    for d in dir_n:
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            while 0 <= nr < N and 0 <= nc < M:
                # 방향에 따라 감시하는 범위 배열에 표시
                if office[nr][nc] != 6:
                    visited[nr][nc] += 1
                    nr, nc = nr + dr, nc + dc
                else:
                    break
        # 다음 cctv 방향 결정
        check(n + 1)
        # 감시 하는 범위 해제
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            while 0 <= nr < N and 0 <= nc < M:
                if office[nr][nc] != 6:
                    visited[nr][nc] -= 1
                    nr, nc = nr + dr, nc + dc
                else:
                    break
    # 현재 위치 감시 해제
    visited[r][c] -= 1
    

# 감시카메라 모양 마다 감시 가능한 범위
DIR_1 = (((0, 1),), ((1, 0),), ((0, -1),), ((-1, 0),))
DIR_2 = (((0, 1), (0, -1)), ((1, 0), (-1, 0)))
DIR_3 = (((-1, 0), (0, 1)), ((0, 1), (1, 0)), ((0, -1), (1, 0)), ((-1, 0), (0, -1)))
DIR_4 = (((0, -1), (-1, 0), (0, 1)), ((-1, 0), (0, 1), (1, 0)), ((0, -1), (1, 0), (0, 1)), ((-1, 0), (0, -1), (1, 0)))
DIR_5 = (((0, 1), (1, 0), (0, -1), (-1, 0)),)


N, M = map(int, input().split())
office = []
cctv = []
# 감시 하는 범위를 표시할 배열
visited = [[0] * M for _ in range(N)]
ans = 10 ** 9
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j]:
            # 벽의 위치는 10000으로 표시
            if tmp[j] == 6:
                visited[i][j] = 10000
            # cctv의 위치는 저장
            else:
                cctv.append([i, j])
    office.append(tmp)

check(0)

print(ans)