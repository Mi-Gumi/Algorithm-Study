a, b = map(int,input().split())
n, m = map(int,input().split())

arr = [[0]*(a+1) for _ in range(b+1)]
d_dict = {
    'E': 0, 
    'N': 1, 
    'W': 2, 
    'S': 3, 
}
d = {
    0:(0,1),
    1:(1,0),
    2:(0,-1),
    3:(-1,0),
}
pos = dict()

for i in range(1,n+1) :
    x, y, direction1 = input().split()
    x, y = int(x), int(y)
    pos[i] = (y, x)
    arr[y][x] = [i, d_dict[direction1]]


done = False
ans = 'OK'
for _ in range(m) :
    if done :
        break
    robot, cmd, count = input().split()
    robot = int(robot)
    count = int(count)
    # print(si, sj)
    # print(arr)
    si, sj = pos[robot]
    tmp, direction = arr[si][sj]

    if cmd == 'L' :
        direction = (direction + count) % 4
        arr[si][sj][1] =  direction
        continue
    elif cmd == 'R' :
        direction = (direction - count) % 4
        arr[si][sj][1] =  direction
        continue
    elif cmd == 'F' :
        di, dj = d[direction]
        # 이동하면서 충돌 체크
        for k in range(1,count + 1) :
            ni, nj = si + di*k, sj + dj*k
            if 0< ni <= b and 0 < nj <= a :
                # 로봇 체크
                if arr[ni][nj] != 0 :
                    ans = f'Robot {robot} crashes into robot {arr[ni][nj][0]}'
                    done = True
                    break
            else :
                # 벽 충돌
                ans = f'Robot {robot} crashes into the wall'
                done = True
                break
        else :
            # 이동하고 위치 갱신
            pos[robot] = ni,nj
            arr[si][sj], arr[ni][nj] = arr[ni][nj], arr[si][sj]
print(ans)
