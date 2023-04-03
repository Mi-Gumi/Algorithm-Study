N, M = map(int, input().split()) # 방 크기 N X M
r, c, d = map(int, input().split()) # 첫 좌표 r,c 방향 d
area = [list(map(int, input().split())) for _ in range(N)]
# 0 청소되지 않은 빈칸  1 벽
# 0 북      1 동     2 남     3 서
cnt = 0
flag = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

bd = [[1,0], [0,-1], [-1,0], [0,1]] # 후진
fd = [[-1,0], [0,1], [1,0], [0,-1]] # 전진

while flag:
    # 작동 1.
    if area[r][c] == 0: # 현재 칸이 아직 청소되지 않은 경우
        area[r][c] = 2 # 청소 처리
        cnt += 1

    # 작동 2, 3 판별
    clean_cnt = 0
    for i in range(4): # r,c 칸의 주변 4칸 중
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if area[nx][ny] == 0: # 청소되지 않은 빈 칸이 있는 경우
                clean_cnt += 1

    # 작동 2.
    if clean_cnt == 0:
        if area[r+bd[d][0]][c+bd[d][1]] != 1: # 한 칸 후진할 수 있다면 후진
            r += bd[d][0]
            c += bd[d][1]
            continue # # 1번으로 돌아간다
        else:
            break # 후진할 수 없다면 작동을 멈춘다
    
    # 작동 3.
    if clean_cnt > 0:
        d = (d + 3) % 4  # 반시계 방향으로 회전
        if area[r+fd[d][0]][c+fd[d][1]] == 0: #  앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            r += fd[d][0]
            c += fd[d][1]
            continue # 1번으로 돌아간다
        
print(cnt) # 작동을 멈출 때까지 청소하는 칸의 개수
