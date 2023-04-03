N, M = map(int, input().split())
si, sj, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 북 서 남 동
if d == 1: # 실제 2차원 배열 내에서의 뱡향 고려
    d = 3
elif d == 3:
    d = 1


def trans_d():  # 시계 반대방향으로 90도
    global d
    if d == 0:
        d = 1
    elif d == 1:
        d = 2
    elif d == 2:
        d = 3
    elif d == 3:
        d = 0

cnt = 0
while 1:
    if arr[si][sj] == 0: # 청소 진행
        cnt += 1
        arr[si][sj] = 9 # 청소 체크

    flag = 1
    for k in range(4): # 4방향 탐색
        trans_d() # 시계 반대방향으로 90 회전
        ni = si + dir[d][0] # 전진
        nj = sj + dir[d][1]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            flag = 0 # 청소 할 곳이 있는 경우
            si, sj = ni, nj
            break
    else:
        flag = 1

    if flag: # 4방향 탐색 후 청소할 곳이 없는 경우
        ni = si - dir[d][0] # 후진
        nj = sj - dir[d][1]
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == 1: # 벽을 만난 경우 종료
                break
            else:
                si, sj = ni, nj
        else: # 범위를 벗어나도 종료
            break

print(cnt)

