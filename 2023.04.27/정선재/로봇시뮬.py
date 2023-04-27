import sys

A, B = map(int, input().split())
n, m = map(int, input().split())
robot = []
direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
for i in range(n):
    x, y, p = map(str, input().split())
    robot.append([int(x)-1, int(y)-1, direction[p]])
active = []
for i in range(m):
    num, act, times = map(str, input().split())
    active.append([num,act,times])
flag = 1
for num,act,times in active:
    if flag == 0:
        break
    for k in range(int(times)):
        if flag == 0:
            break
        num = int(num)
        if act == 'L':
            robot[num-1][2] = (robot[num-1][2] - 1) % 4
        elif act == 'R':
            robot[num-1][2] = (robot[num-1][2] + 1) % 4

        elif act == 'F':
            robot[num-1][1] = robot[num-1][1] + di[robot[num-1][2]]
            robot[num-1][0] = robot[num-1][0] + dj[robot[num-1][2]]

            if robot[num-1][1] < 0 or robot[num-1][1] >= B or robot[num-1][0] < 0 or robot[num-1][0] >= A:
                print(f'Robot {num} crashes into the wall')
                flag = 0
                break
            for o in range(n):
                if o != (num-1):
                    if robot[o][0] == robot[num-1][0] and robot[o][1] == robot[num-1][1]:
                        print(f'Robot {num} crashes into robot {o+1}')
                        flag = 0
                        break
if flag == 1:
    print('OK')
