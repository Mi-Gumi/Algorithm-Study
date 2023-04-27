# 탐색 방향: 상, 하, 좌, 우
direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# CCTV별 이동 가능한 방향
cctv_direction = [
    [],
    [[0], [1], [2], [3]], # 1번 CCTV
    [[0, 1], [2, 3]], # 2번 CCTV
    [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
    [[0, 1, 2, 3]] # 5번 CCTV
]

N, M = map(int,input().split())
matrix_row = [list(map(int,input().split())) for _ in range(N)]
bound = 0

def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

matrix = [arr[:] for arr in matrix_row]
cams = []
cnt_cams = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 :
            bound += 1
        elif matrix[i][j] < 6:
            cams.append((i,j))
            cnt_cams += 1

ans = 0
answer = M*N+1
def bt(now, end, matrix, tg):
    global ans, answer
    
    if now == end:
        # ans = max(tg,ans)
        answer = min(answer,count_zero(matrix))
        return 

    cam = cams[now]
    model = matrix[cam[0]][cam[1]]
    x,y = cam
    cnt = 0
    
    matrix_save = None

    for direction in cctv_direction[model]:
        matrix_load = [arr[:] for arr in matrix]
        target = 0
        for directions in direction:
            nx = x
            ny = y

            while True:
                nx += direction_list[directions][0]
                ny += direction_list[directions][1]
                if nx < 0 or ny < 0 or nx >= N or ny >= M : break
                if matrix_load[nx][ny] == 6: break
                if 1<= matrix_load[nx][ny] <=5 : continue
                if matrix_load[nx][ny] == 9 : continue                
                matrix_load[nx][ny] = 9
                target += 1

        if target >= cnt:
            matrix_save = matrix_load
            cnt = target
            bt(now+1,cnt_cams, matrix_save, tg + cnt)
        else:
            bt(now+1,cnt_cams, matrix_load, tg + cnt)

bt(0, cnt_cams, matrix,0)
# print(ans)
# print(bound - ans)
print(answer)