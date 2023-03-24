# 세로, 가로, 주사위 좌표, 명령 개수
N, M, x, y, K = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split())) # 명령 동 1 서 2 북 3 남 4


dice = [0,0,0,0,0,0,0] # 0 번인덱스는 안쓰는거
# dice = [안씀, 윗면, 북쪽, 동쪽, 서쪽, 남쪽, 아래]
#          _    1    2    3    4    5    6

def role_dice(before, direction):
    # dice = [윗면, 북쪽, 동쪽, 서쪽, 남쪽, 아래]
    _, a, b, c, d, e, f = before
    if direction == 1 : # 동쪽 :
        after = [_, d, b, a, f, e, c]
    elif direction == 2 : # 서쪽:
        after = [_, c, b, f, a, e, d]
    elif direction == 3 : # 북쪽:
        after = [_, e, a, c, d, f, b]
    elif direction == 4 : # 남쪽:
        after = [_, b, f, c, d, a, e]
    return after


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for direction in cmd: # K 안에 있는 direction 가져오기
    # 맵을 벗어나지 않는 direction일경우에만 동작을 수행
    if 0 <= (x + dx[direction]) < N and 0 <= (y + dy[direction]) < M:
        x += dx[direction]
        y += dy[direction]
        
        dice = role_dice(dice, direction)

        if num[x][y] == 0: # 땅이 0 일 경우
            num[x][y] = dice[-1] # 땅이 주사위 바닥을 복사주사위 바닥으로 복사
        else: # 땅이 0 이 아닐경우
            dice[-1] = num[x][y] # 주사위 바닥이 땅으로 복사
            num[x][y] = 0 # 이후 땅이 0으로 변경

        print(dice[1])

