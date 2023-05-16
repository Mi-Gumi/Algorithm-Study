import sys
input = sys.stdin.readline


# 모래 이동 함수
def move(r, c, now_d):
    global ans
    dr, dc = d[now_d]
    tmp = board[r][c]
    if dr:
        if 0 <= r + (2 * dr) < N:
            board[r + (2 * dr)][c] += tmp // 20
        else:
            ans += tmp // 20
        board[r][c] -= tmp // 20
        if 0 <= r + dr < N and 0 <= c + 1 < N:
            board[r + dr][c + 1] += tmp // 10
        else:
            ans += tmp // 10
        board[r][c] -= tmp // 10
        if 0 <= r + dr < N and 0 <= c - 1 < N:
            board[r + dr][c - 1] += tmp // 10
        else:
            ans += tmp // 10
        board[r][c] -= tmp // 10
        if 0 <= c + 1 < N:
            board[r][c + 1] += tmp * 7 // 100
        else:
            ans += tmp * 7 // 100
        board[r][c] -= tmp * 7 // 100
        if 0 <= c - 1 < N:
            board[r][c - 1] += tmp * 7 // 100
        else:
            ans += tmp * 7 // 100
        board[r][c] -= tmp * 7 // 100
        if 0 <= c + 2 < N:
            board[r][c + 2] += tmp // 50
        else:
            ans += tmp // 50
        board[r][c] -= tmp // 50
        if 0 <= c - 2 < N:
            board[r][c - 2] += tmp // 50
        else:
            ans += tmp // 50
        board[r][c] -= tmp // 50
        if 0 <= r - dr < N and 0 <= c + 1 < N:
            board[r - dr][c + 1] += tmp // 100
        else:
            ans += tmp // 100
        board[r][c] -= tmp // 100
        if 0 <= r - dr < N and 0 <= c - 1 < N:
            board[r - dr][c - 1] += tmp // 100
        else:
            ans += tmp // 100
        board[r][c] -= tmp // 100
        if 0 <= r + dr < N:
            board[r + dr][c] += board[r][c]
        else:
            ans += board[r][c]
        board[r][c] = 0
    else:
        if 0 <= c + (2 * dc) < N:
            board[r][c + (2 * dc)] += tmp // 20
        else:
            ans += tmp // 20
        board[r][c] -= tmp // 20
        if 0 <= r + 1 < N and 0 <= c + dc < N:
            board[r + 1][c + dc] += tmp // 10
        else:
            ans += tmp // 10
        board[r][c] -= tmp // 10
        if 0 <= r - 1 < N and 0 <= c + dc < N:
            board[r - 1][c + dc] += tmp // 10
        else:
            ans += tmp // 10
        board[r][c] -= tmp // 10
        if 0 <= r + 1 < N:
            board[r + 1][c] += tmp * 7 // 100
        else:
            ans += tmp * 7 // 100
        board[r][c] -= tmp * 7 // 100
        if 0 <= r - 1 < N:
            board[r - 1][c] += tmp * 7 // 100
        else:
            ans += tmp * 7 // 100
        board[r][c] -= tmp * 7 // 100
        if 0 <= r + 2 < N:
            board[r + 2][c] += tmp // 50
        else:
            ans += tmp // 50
        board[r][c] -= tmp // 50
        if 0 <= r - 2 < N:
            board[r - 2][c] += tmp // 50
        else:
            ans += tmp // 50
        board[r][c] -= tmp // 50
        if 0 <= r + 1 < N and 0 <= c - dc < N:
            board[r + 1][c - dc] += tmp // 100
        else:
            ans += tmp // 100
        board[r][c] -= tmp // 100
        if 0 <= r - 1 < N and 0 <= c - dc < N:
            board[r - 1][c - dc] += tmp // 100
        else:
            ans += tmp // 100
        board[r][c] -= tmp // 100
        if 0 <= c + dc < N:
            board[r][c + dc] += board[r][c]
        else:
            ans += board[r][c]
        board[r][c] = 0


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
d = ((0, -1), (1, 0), (0, 1), (-1, 0))
move_cnt = 1
now_d = 0
cnt = 0
ans = 0
r = c = N // 2

while r != 0 or c != 0:
    for _ in range(move_cnt):
        # 이동 방향으로 이동 횟수 만큼 이동
        r, c = r + d[now_d][0], c + d[now_d][1]
        # 모래 이동
        move(r, c, now_d)
        # 0, 0에 도달했다면 종료
        if not r and not c:
            break
    # 방향 전환
    now_d = (now_d + 1) % 4
    # cnt + 1
    cnt += 1
    # 두 번 이동했다면
    if cnt == 2:
        cnt = 0
        # 이동 횟수 + 1
        move_cnt += 1

print(ans)
