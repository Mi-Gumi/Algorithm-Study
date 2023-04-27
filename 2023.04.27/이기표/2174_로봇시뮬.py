def check(n, ci, cj):
    if 0 >= ci or 0 >= cj or A < ci or B < cj: # 벽 충돌
        return f'Robot {n+1} crashes into the wall'

    for i in range(len(pos)): # 로봇끼리 충돌
        if i == n:
            continue
        if (ci, cj) == (pos[i][0], pos[i][1]):
            return f'Robot {n+1} crashes into robot {i+1}'

    return 0 # 이상 없음

A, B = map(int, input().split())
N, M = map(int, input().split())
pos = []
for _ in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    pos.append([x, y, d])

rst = 0
R_lst = ['N', 'E', 'S', 'W']
L_lst = ['N', 'W', 'S', 'E']
for _ in range(M):
    flag = 0
    # 로봇번호, 명령 종류, 횟수
    n, t, c = input().split()
    n, c = int(n)-1, int(c)
    if t == 'R': # 오른쪽으로 회전
        dir = 0
        if pos[n][2] == 'N': dir = 0
        elif pos[n][2] == 'E': dir = 1
        elif pos[n][2] == 'S': dir = 2
        elif pos[n][2] == 'W': dir = 3
        pos[n][2] = R_lst[(dir + c) % 4]
    elif t == 'L': # 왼쪽으로 회전
        dir = 0
        if pos[n][2] == 'N':dir = 0
        elif pos[n][2] == 'E':dir = 3
        elif pos[n][2] == 'S':dir = 2
        elif pos[n][2] == 'W':dir = 1
        pos[n][2] = L_lst[(dir + c) % 4]
    else:
        for _ in range(c): # 앞으로 이동
            if pos[n][2] == 'N': pos[n][1] += 1
            elif pos[n][2] == 'E': pos[n][0] += 1
            elif pos[n][2] == 'S': pos[n][1] -= 1
            elif pos[n][2] == 'W': pos[n][0] -= 1
            rst = check(n, pos[n][0], pos[n][1])
            if rst:
                flag = 1
                break
    if flag:
        break

if rst == 0:
    print('OK')
else:
    print(rst)