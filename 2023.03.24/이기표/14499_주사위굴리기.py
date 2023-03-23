N, M, X, Y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))
dice = [0] * 6 # 주사위

# 주사위 회전
def move(n):
    if n==1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif n==2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif n==3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif n==4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

dr = [[0, 1], [0, -1], [-1, 0], [1, 0]]
for c in lst:
    # 동 서 북 남 범위를 벗어난 경우 무시
    if X+dr[c-1][0] < 0 or Y + dr[c-1][1] < 0 or Y + dr[c-1][1] >= M or X+dr[c-1][0] >= N:
        continue
    # 델타 이동
    X += dr[c-1][0]
    Y += dr[c-1][1]
    # 주사위 회전
    move(c)
    # 0이 아닐때 칸에 해당하는 값 -> 주사위로 복사
    if arr[X][Y]:
        dice[5] = arr[X][Y]
        arr[X][Y] = 0
    # 0일때 주사위 값 -> 칸으로 복사
    else:
        arr[X][Y] = dice[5]

    print(dice[0])


