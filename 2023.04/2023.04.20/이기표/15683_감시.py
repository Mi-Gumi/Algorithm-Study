'''
1. 상 하 좌 우로 감시하는 함수 생성
2. 5개 카메라의 각각 조건(ex. 한방향, 양방향....)에 따라 감시 진행
3. 완전탐색을 통해 카메라 수만큼 감시 진행 후 특정 조건을 만족하면 탐색 종료
'''
def move_up(arr, x, y):
    for i in range(x, -1, -1):
        if arr[i][y] == 6:
            break
        else:
            if arr[i][y] == 0:
                arr[i][y] = -1
def move_down(arr, x, y):
    for i in range(x, N):
        if arr[i][y] == 6:
            break
        else:
            if arr[i][y] == 0:
                arr[i][y] = -1
def move_left(arr, x, y):
    for j in range(y, -1, -1):
        if arr[x][j] == 6:
            break
        else:
            if arr[x][j] == 0:
                arr[x][j] = -1
def move_right(arr, x, y):
    for j in range(y, M):
        if arr[x][j] == 6:
            break
        else:
            if arr[x][j] == 0:
                arr[x][j] = -1

def cam1(arr, n, d): # 상 하 좌 우
    x = cam_pos[n][0]
    y = cam_pos[n][1]
    if d == 0:
        move_up(arr, x, y)
    elif d == 1:
        move_down(arr, x, y)
    elif d == 2:
        move_left(arr, x, y)
    else:
        move_right(arr, x, y)
    return arr

def cam2(arr, n, d): # 상하 좌우
    x = cam_pos[n][0]
    y = cam_pos[n][1]

    if d%2==0: # 상하
        move_up(arr, x, y)
        move_down(arr, x, y)
    else:      # 좌우
        move_right(arr, x, y)
        move_left(arr, x, y)
    return arr

def cam3(arr, n, d):
    x = cam_pos[n][0]
    y = cam_pos[n][1]

    if d == 0: # 상우
        move_up(arr, x, y)
        move_right(arr, x, y)
    elif d == 1: # 우하
        move_right(arr, x, y)
        move_down(arr, x, y)
    elif d == 2: # 하좌
        move_down(arr, x, y)
        move_left(arr, x, y)
    else: # 좌상
        move_left(arr, x, y)
        move_up(arr, x, y)

    return arr

def cam4(arr, n, d):
    x = cam_pos[n][0]
    y = cam_pos[n][1]

    if d == 0: # 좌상우
        move_left(arr, x, y)
        move_up(arr, x, y)
        move_right(arr, x, y)
    elif d == 1: #상우하
        move_up(arr, x, y)
        move_right(arr, x, y)
        move_down(arr, x, y)
    elif d == 2: #우하좌
        move_right(arr, x, y)
        move_down(arr, x, y)
        move_left(arr, x, y)
    else: # 하좌상
        move_down(arr, x, y)
        move_left(arr, x, y)
        move_up(arr, x, y)

    return arr

def cam5(arr, n, d):
    x = cam_pos[n][0]
    y = cam_pos[n][1]

    move_up(arr, x, y)
    move_down(arr, x, y)
    move_left(arr, x, y)
    move_right(arr, x, y)
    return arr

def cam_cnt(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

def bt(n, arr):
    global ans

    # 사각지대가 없으면 종료
    if ans == 0:
        return

    # 모든 카메라를 사용하면 사각지대 비교 후 종료
    if n == len(cam_pos):
        cnt = cam_cnt(arr)
        ans = min(ans, cnt)
        return
    # 현재의 카메라 위치
    cam_cur = arr[cam_pos[n][0]][cam_pos[n][1]]
    for d in range(4):
        # 깊은 복사 진행
        arr_c = [lst[:] for lst in arr]
        if cam_cur == 1:
            bt(n + 1, cam1(arr_c, n, d))
        elif cam_cur == 2:
            bt(n + 1, cam2(arr_c, n, d))
        elif cam_cur == 3:
            bt(n + 1, cam3(arr_c, n, d))
        elif cam_cur == 4:
            bt(n + 1, cam4(arr_c, n, d))
        else:
            bt(n + 1, cam5(arr_c, n, d))

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cam_pos = []
for i in range(N):
    for j in range(M):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            cam_pos.append((i, j))

ans = 10**9
bt(0, arr)
print(ans)