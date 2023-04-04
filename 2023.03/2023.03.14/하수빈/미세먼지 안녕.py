import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
flag = 0
room = []
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 방 정보를 입력 받으면서 공기청정기 위치 기억
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j]:
            if tmp[j] == -1:
                if flag:
                    cleaner_down = i
                else:
                    cleaner_up = i
                    flag = 1
    room.append(tmp)

# 확산
# move_list에 먼지 이동 합을 계산
for _ in range(T):
    move_list = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                tmp = 0
                for dr, dc in d:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        move_list[nr][nc] += room[i][j] // 5
                        tmp += room[i][j] // 5
                room[i][j] -= tmp

    # room에 move_list 합산
    for i in range(R):
        for j in range(C):
            room[i][j] += move_list[i][j]

    # 윗 공기 순환
    # 이동방향
    dir = 0
    # 임시 변수
    tmp = 0
    r, c, = cleaner_up, 1
    d2 = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    while True:
        nr, nc = r + d2[dir][0], c + d2[dir][1]
        # 공기청정기 위치에 도달했다면 break
        if r == cleaner_up and c == 0:
            break
        # 방의 끝에 도달했다면 방향 전환
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            dir += 1
            continue
        # 임시변수와 현재위치 교환
        tmp, room[r][c] = room[r][c], tmp
        # 현재위치 변경
        r, c = nr, nc

    # 아래 공기 순환
    dir = 0
    tmp = 0
    r, c, = cleaner_down, 1
    d2 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while True:
        nr, nc = r + d2[dir][0], c + d2[dir][1]
        # 공기청정기 위치에 도달했다면 break
        if r == cleaner_down and c == 0:
            break
        # 방의 끝에 도달했다면 방향 전환
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            dir += 1
            continue
        # 임시변수와 현재위치 교환
        tmp, room[r][c] = room[r][c], tmp
        # 현재위치 변경
        r, c = nr, nc

ans = 0
for l in room:
    for du in l:
        ans += du

print(ans + 2)