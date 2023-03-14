def insnair(time) :
    if time == T :
        return
    new_room = [[0]*C for _ in range(R)]

    for i in range(R) :
        for j in range(C) :
            dust = room[i][j]
            if dust == 0 or dust == -1 :
                continue
            dust_kid = dust//5
            cnt = 0
            for di, dj in d :
                ni = i + di 
                nj = j + dj
                if i not in safe_zone :
                    if ni in safe_zone :
                        continue
                if 0<= ni < R and 0 <= nj < C :
                    cnt += 1
                    new_room[i][j] += dust_kid
            room[i][j] -= cnt * dust_kid
    for i in range(R) :
        for j in range(C) :
            room[i][j] += new_room[i][j]
    
    # 상단 좌측
    for i in range(1,aircleaner_top) :
        room[i][0] = room[i-1][0]
    # 상단 상단
    for i in range(0,C-1) :
        room[0][i] = room[0][i+1]
    # 상단 우측
    for i in range(0,aircleaner_top) :
        room[i][C-1] = room[i+1][C-1]

    # 하단 좌측
    for i in range(R-2,aircleaner_bot, -1) :
        room[i][0] = room[i+1][0]
    # 하단 하단
    for i in range(C-2,-1,-1) :
        room[R-1][i] = room[R-1][i+1]
    # 하단 우측
    for i in range(aircleaner_bot+2,R) :
        room[i][C-1] = room[i-1][C-1]
    # 중심부
    for i in range(2,C) :
        room[aircleaner_top][i] = room[aircleaner_top][i-1]
        room[aircleaner_bot][i] = room[aircleaner_top][i-1]
    room[aircleaner_top][1] = 0
    room[aircleaner_bot][1] = 0
    insnair(time+1)

R, C, T = map(int,input().split())

room = [(list(map(int,input().split()))) for _ in range(R)]

aircleaner_top = 0
aircleaner_bot = 0
for i in range(R) :
    if room[i][0] == -1 :
        aircleaner_top = i
        aircleaner_bot = i + 1
        break

safe_zone = (aircleaner_top, aircleaner_bot)
d = ((0,1),(1,0),(0,-1),(-1,0))

insnair(0)
ans = 0
for i in range(R) :
    ans += sum(room[i])
    print(*room[i])

ans += 2

print(ans)






