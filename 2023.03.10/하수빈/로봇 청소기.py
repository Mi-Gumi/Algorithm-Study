import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

while True:
    # 청소 안한 구역 발견 플래그
    flag = 0
    # 청소 안했다면 청소하고 ans + 1
    if not room[r][c]:
        visited[r][c] = 1
        ans += 1
    for dr, dc in _dir:
        nr, nc = r + dr, c + dc
        # 방안에서 벽이 아니고 청소안한 구역이 있다면 플래그 처리 후 break
        if 0 <= nr < N and 0 <= nc < M and not room[nr][nc] and not visited[nr][nc]:
            flag = 1
            break
    # 청소 안한 구역이 없다면
    else:
        nr, nc = r - _dir[d][0], c - _dir[d][1]
        # 한 칸 뒤로 간 곳이 방안에 있고 벽이 아니라면 이동
        if 0 <= nr < N and 0 <= nc < M and not room[nr][nc]:
            r, c = nr, nc
        # 방 밖이거나 벽이라면 종료
        else:
            break

    # 청소 안한 구역이 있다면
    if flag:
        # 회전
        # 방향이 0이면 3으로
        if not d:
            d = 3
        # 아니라면 -1
        else:
            d -= 1
        nr, nc = r + _dir[d][0], c + _dir[d][1]
        # 방안이고 벽이아니고 청소 안했다면 이동
        if 0 <= nr < N and 0 <= nc < M and not room[nr][nc] and not visited[nr][nc]:
            r, c = nr, nc

print(ans)
