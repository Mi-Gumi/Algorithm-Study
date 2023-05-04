import sys
input = sys.stdin.readline


def check():
    new_fire_list = []
    divide_list = []
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(fire_list)):
        r, c = fire_list[i]
        for m, s, d in board[r][c]:
            dr, dc = _dir[d]
            # 이동한 위치
            nr, nc = (r + s * dr) % N, (c + s * dc) % N
            # 이동한 위치의 새 보드에 파이어볼 추가
            new_board[nr][nc].append([m, s, d])
            # 이동한 위치에 파이어볼이 하나 있다면 새로운 파이어볼 위치에 추가
            if len(new_board[nr][nc]) == 1:
                new_fire_list.append([nr, nc])
            # 이동한 위치에 파이어볼이 두개 있다면 나눠야할 파이어볼 위치에 추가
            elif len(new_board[nr][nc]) == 2:
                divide_list.append([nr, nc])

    for i in range(len(divide_list)):
        r, c = divide_list[i]
        s_m = s_s = 0
        flag = 0
        # 첫번째 파이어볼 방향이 홀수인지 짝수인지 기억
        odd = new_board[r][c][0][2] % 2
        for fire in new_board[r][c]:
            s_m += fire[0]
            s_s += fire[1]
            # 현재 파이어볼의 방향이 첫번째 파이어볼 방향의 홀수, 짝수와 다르다면 표시
            if not flag and fire[2] % 2 != odd:
                flag = 1
        
        # 나눴을 때 파이어볼의 질량이 0이 된다면 삭제
        if not s_m // 5:
            new_board[r][c] = []
        elif flag:
            # 대각선 방향으로 설정
            new_board[r][c] = [[s_m // 5, s_s // len(new_board[r][c]), 1], [s_m // 5, s_s // len(new_board[r][c]), 3], [s_m // 5, s_s // len(new_board[r][c]), 5], [s_m // 5, s_s // len(new_board[r][c]), 7]]
        else:
            # 십자 방향으로 설정
            new_board[r][c] = [[s_m // 5, s_s // len(new_board[r][c]), 0], [s_m // 5, s_s // len(new_board[r][c]), 2], [s_m // 5, s_s // len(new_board[r][c]), 4], [s_m // 5, s_s // len(new_board[r][c]), 6]]
    
    return new_board, new_fire_list


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fire_list = []
_dir = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # 파이어볼 위치에 질량 속도 방향 저장
    board[r - 1][c - 1].append([m, s, d])
    # 파이어볼 위치 기억
    fire_list.append([r - 1, c - 1])

for _ in range(K):
    # 보드와 파이어볼 이동한 후로 교체
    board, fire_list = check()

ans = 0
# 남은 질량 계산
for r, c in fire_list:
    for fire in board[r][c]:
        ans += fire[0]

print(ans)
