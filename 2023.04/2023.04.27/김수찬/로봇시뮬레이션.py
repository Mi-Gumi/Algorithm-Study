A, B = map(int,input().split())
N, M = map(int,input().split())
matrix = [[ 0 for _ in range(B)] for _ in range(A)]

robo_dir = dict()
            #북     # 동    #남  # 서  
dir_xy = ((0, 1),(-1, 0),(0, -1),(1, 0))

dir = {
    'N' : 0,
    'S' : 2,
    'E' : 1,
    'W' : 3,
}
for i in range(1,N+1):
    x, y, d = input().split()
    x = int(x)-1
    y = int(y)-1
    matrix[x][y] = i
    robo_dir[i] = [dir[d],(x,y)]

def order():
    for j in range(M):
        X, o, cnt = input().split()
        X = int(X)
        cnt = int(cnt)

        if o == 'L':
            robo_dir[X][0] = (robo_dir[X][0]-1*cnt) % 4
        elif o == 'R':
            robo_dir[X][0] = (robo_dir[X][0]+cnt) % 4
        else:
            dx,dy = dir_xy[robo_dir[X][0]]
            for _ in range(1,cnt+1):
                x,y = robo_dir[X][1]
                nx = x + dx
                ny = y + dy
                matrix[x][y] = 0
                if nx < 0 or ny < 0 or nx >= A or nx >= B: 
                    print(f'Robot {X} crashes into the wall')
                    return
                if matrix[nx][ny] != 0 :
                    print(f'Robot {X} crashes into robot {matrix[nx][ny]}')
                    return
                matrix[nx][ny] = X
                robo_dir[X][1] = (nx,ny)
    print('OK')
    return

order()