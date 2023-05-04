import sys
input = sys.stdin.readline


def move_ball(r, c, dr, dc):
    nr, nc = r + dr, c + dc
    while True:
        if board[nr][nc] == 'O':
            board[r][c] = '.'
            return 1, 0, 0
        if board[nr][nc] == '#' or board[nr][nc] == 'R' or board[nr][nc] == 'B':
            if nr - dr != r or nc - dc != c:
                board[nr - dr][nc - dc] = board[r][c]
                board[r][c] = '.'
            return 0, nr - dr, nc - dc
        nr, nc = nr + dr, nc + dc


def move(n, br, bc, rr, rc):
    global ans

    # 10번 이상 이동했거나 n이 이미 ans보다 크다면 종료
    if n == 11 or n >= ans:
        return
    
    for dr, dc in D:
        # 아래로 기울였다면
        if dr == 1:
            # 파란공이 더 아래에 있다면 파란공 먼저 이동
            if br > rr:
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
            # 아니라면 빨간공 먼저 이동
            else:
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
        # 위로 기울였다면
        elif dr == -1:
            # 빨간공이 더 위에 있다면 빨간공 먼저 이동
            if br > rr:
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
            # 아니라면 파란공 먼저 이동
            else:
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
        # 오른쪽으로 기울였다면
        elif dc == 1:
            # 파란공이 더 오른쪽에 있다면 파란공 먼저 이동
            if bc > rc:
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
            # 아니라면 빨간공 먼저 이동
            else:
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
        # 왼쪽으로 기울였다면
        elif dc == -1:
            # 빨간공이 더 왼쪽에 있다면 빨간공 먼저 이동
            if bc > rc:
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
            # 아니라면 파란공 먼저 이동
            else:
                in_b, nbr, nbc = move_ball(br, bc, dr, dc)
                in_r, nrr, nrc = move_ball(rr, rc, dr, dc)
        # 빨간공 파란공 모두 들어갔다면
        if in_b and in_r:
            # 원래 위치로 초기화후 다음방향으로 이동
            board[br][bc] = 'B'
            board[rr][rc] = 'R'
            continue
        # 파란공만 들어갔다면
        if in_b:
            # 빨간공의 현재위치를 초기화하고 원래위치로 옮긴 후 파랑공도 초기화하고 다음방향으로 이동
            board[nrr][nrc] = '.'
            board[br][bc] = 'B'
            board[rr][rc] = 'R'
            continue
        # 빨간공만 들어갔다면
        if in_r:
            # ans값 교체
            ans = min(ans, n)
            # 파란공의 현재위치를 초기화하고 원래위치로 옮긴 후 빨간공도 초기화하고 종료
            board[nbr][nbc] = '.'
            board[br][bc] = 'B'
            board[rr][rc] = 'R'
            return
        # 다음 기울임 탐색
        move(n + 1, nbr, nbc, nrr, nrc)
        # 원위치로 복구
        board[nbr][nbc] = board[nrr][nrc] = '.'
        board[br][bc] = 'B'
        board[rr][rc] = 'R'


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = 10 ** 9
for i in range(N):
    # 빨간공 위치와 파란공 위치 기억
    for j in range(M):
        if board[i][j] == 'R':
            pos_r = [i, j]
        elif board[i][j] == 'B':
            pos_b = [i, j]

move(1, pos_b[0], pos_b[1], pos_r[0], pos_r[1])

# 값이 변하지 않았다면 -1 출력
if ans == 10 ** 9:
    print(-1)
# 값이 변했다면 ans출력
else:
    print(ans)