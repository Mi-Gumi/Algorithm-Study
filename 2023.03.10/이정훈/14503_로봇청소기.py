N, M = map(int,input().split())

r, c, look = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]

d = ((-1,0),(0,1),(1,0),(0,-1))

clean = 0
while True :
    if room[r][c] == 0 :
        room[r][c] = 2
        clean += 1
    
    # check 
    dirty = False
    for dr, dc in d :
        rr, cc = r + dr , c + dc
        if 0<= rr < N and 0<= cc < M :
            if room[rr][cc] == 0 :
                 dirty = True
                 break
    if dirty :
        while True : # 청소할 방향까지 회전
            look = (look + 3 ) % 4
            rr, cc = r + d[look][0] , c + d[look][1]
            if 0<= rr < N and 0<= cc < M :
                if room[rr][cc] == 0 :
                    r, c = rr, cc
                    break
        
    else :
        # 후진
        rr, cc = r - d[look][0] , c - d[look][1]
        if 0<= rr < N and 0<= cc < M :
            # 벽이 아니면 ok
            if room[rr][cc] != 1 :
                r, c = rr, cc
                continue
            # 벽이면 not ok
            else :
                break
        else :
            break
print(clean)
    