N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]



# 1번 CCTV는 한 쪽 방향만 감시할 수 있다.
# 2번과 3번은 두 방향을 감시할 수 있는데, 
# 2번은 감시하는 방향이 서로 반대방향이어야 하고,
# 3번은 직각 방향이어야 한다.
# 4번은 세 방향,
# 5번은 네 방향을 감시할 수 있다.

# CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
# 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다.
# CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며,
# 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

# 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

cctv = []
for x in range(N):
    for y in range(M):
        if 1 <= arr[x][y] <= 5:
            cctv.append([x, y])

def search(x, y):
    if arr[x][y] == 1:
        for f in range(4):
            origin = []
            for spread in range(1, N+1):
                nx = x + dx[f] * spread
                ny = y + dy[f] * spread
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 6:
                        break
                    else:
                        arr[nx][ny] = -1
                        origin.append((nx,ny))
                # pprint(arr)
            cnt = 0
            for x in range(N):
                for y in range(M):
                    if arr[x][y] != -1:
                        cnt += 1
            pprint(arr)
            print(cnt)
            for o in origin:
                arr[o[0]][o[1]] = 0

for a in range(len(cctv)):
    search(cctv[a][0], cctv[a][1])

cnt = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] != -1:
            cnt += 1
