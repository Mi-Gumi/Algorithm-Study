from collections import deque

def bfs(): # 빙산의 개수 확인
    visited = [[0]*M for _ in range(N)]
    tmp = 0
    for i, j in ice:
        if visited[i][j] == 0:
            # 녹인 후의 빙산의 개수 체크
            tmp += 1
            que = deque()
            que.append((i,j))
            visited[i][j] = tmp

            while que:
                si, sj = que.popleft()
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni = si + di
                    nj = sj + dj
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj]:
                        que.append((ni, nj))
                        visited[ni][nj] = tmp

    for lst in visited:
        for v in lst:
            # 빙산이 개수가 2 이상인 경우 종료
            if v >= 2:
                return False
    return True

def ice_check(): # 조건에 만족하는 빙산 찾기
    pos = []
    for i in range(N):
        for j in range(M):
            cnt = 0
            if arr[i][j]:
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        cnt += 1
                # 빙산의 위치와 4방향에 일치하는 카운트값도 저장
                pos.append((i, j, cnt))
    return pos

def ice_melt():
    # 받은 빙산의 위치를 통해 한 번에 녹임
    ice = []
    for i, j, cnt in pos:
        # 0이하일 경우는 무조건 0
        if cnt > arr[i][j]:
            arr[i][j] = 0
        else:
            arr[i][j] -= cnt
        if arr[i][j]:
            ice.append((i,j))
    return ice


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
pos = []
while 1:
    pos = ice_check()
    ice = ice_melt()
    ans += 1
    rst = bfs()
    # 빙산의 개수를 만족하거나 빙산이 더 이상 업는 경우 종료
    if rst == False or len(pos)==0:
        break
if len(pos) == 0:
    print(0)
else:
    print(ans)




