import sys
input = sys.stdin.readline

def move(k):
    global r, c
    flag = 0
    # 주사위 굴리기 및 가능 여부 확인 조건문
    if k == 1 and c < M - 1:
        c += 1
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        flag = 1
    elif k == 2 and c > 0:
        c -= 1
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        flag = 1
    elif k == 3 and r > 0:
        r -= 1
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        flag = 1
    elif k == 4 and r < N - 1:
        r += 1
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        flag = 1

    # 주사위를 굴릴 수 있다면
    if flag:
        if _map[r][c]:
            # 지도에 숫자가 있다면 숫자 변경하고 지도를 0으로 설정
            new_dice[5][0] = _map[r][c]
            _map[r][c] = 0
        else:
            # 지도에 숫자가 없다면 주사위 숫자 복사
            _map[r][c] = new_dice[5][0]
        print(new_dice[0][0])
        # 바뀐 주사위 반환
        return new_dice
    else:
        # 주사위를 굴릴 수 없다면 기존 주사위 반환
        return dice

N, M, r, c, K = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

dice = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]
#1          4       2       1       6       5       3
#2          3       2       6       1       5       4
#3          5       1       3       4       6       2
#4          2       6       3       4       1       5

for k in cmd:
    dice = move(k)