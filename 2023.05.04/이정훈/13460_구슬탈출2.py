def move_ball(board, blue, red, direction, cnt) :
    global ans
    # 현재 최소값이상이면 볼 필요 없음
    if ans <= cnt :
        return
    # 복사해서 사용
    arr = [board[i][:] for i in range(n)]
    blue_pos = blue.copy()
    red_pos = red.copy()

    di, dj = d[direction]

    # 앞으로 가면서 다른 구슬을 만났는지 여부
    blue_meet_red = False
    red_meet_blue = False
    
    # 파란 구슬 이동
    while True :
        ni, nj = blue_pos[0] + di, blue_pos[1] + dj
        if arr[ni][nj] == 'O' :
            # 파란 구슬이 들어 갔다면 빨강이 앞에 있든 뒤에 있든 don't care
            return
        elif arr[ni][nj] == '#':
            break
        elif arr[ni][nj] == 'R' :
            # 블루가 이동하면서 레드를 만남. 즉, 파랑이 뒤에 위치
            blue_meet_red = True
        blue_pos[0], blue_pos[1] = ni, nj

    # 빨간 구슬 이동
    while True :
        ni, nj = red_pos[0] + di, red_pos[1] + dj
        if arr[ni][nj] == 'O' :
            if ans > cnt :
                ans = cnt
            return
        elif arr[ni][nj] == '#' :
            break
        elif arr[ni][nj] == 'B' :
            # 레드가 이동하면서 블루를 만남. 즉, 빨강이 뒤에 위치
            red_meet_blue = True
        red_pos[0], red_pos[1] = ni, nj


    # 10번째 시도일 떄 구멍에 들어가지 않았으므로 return
    if cnt == 10 :
        return
    
    # 만난 적이 있으면 같은 위치에 있으므로 뒤에 있던 구슬을 한칸 뒤로
    if blue_meet_red :
        blue_pos = [blue_pos[0]-di,blue_pos[1]-dj]
    elif red_meet_blue :
        red_pos = [red_pos[0]-di,red_pos[1]-dj]

    # 아무 구슬도 움직이지 않았으면 return
    if blue == blue_pos and red == red_pos :
        return
    
    # 구슬 이동
    # 원래 위치를 . 으로, 이동 후 위치를 R, B 로
    arr[blue[0]][blue[1]], arr[red[0]][red[1]] = '.','.'
    arr[blue_pos[0]][blue_pos[1]], arr[red_pos[0]][red_pos[1]] = 'B', 'R'

    # print(dir_name[direction], cnt)
    # for i in range(n) :
    #     print(*arr[i])
    # print()

    for nd in range(4) :
        # 같은 방향은 다시 시도하지 않음
        if nd == direction :
            continue
        move_ball(arr, blue_pos, red_pos, nd, cnt+1)


d = ((0,1),(1,0),(0,-1),(-1,0))


n, m = map(int,input().split())

board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m) :
        if board[i][j] == 'B' :
            blue = [i,j]
        elif board[i][j] == 'R' :
            red = [i,j]
ans = 99
for direc in range(4) :
    move_ball(board, blue, red, direc, 1)

if ans == 99:
    ans = -1
print(ans)