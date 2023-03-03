import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    count = -1
    # 큐가 빌때 까지 반복
    while tomato:
        # 날짜 + 1
        count += 1
        # 큐의 길이만큼 반복
        for _ in range(len(tomato)):
            r, c = tomato.popleft()
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                # 탐색
                if 0 <= nr < M and 0 <= nc < N and not box[nr][nc]:
                    box[nr][nc] = 1
                    tomato.append([nr, nc])

    # 박스 안에 덜익은 토마토가 있다면 count = -1
    for lst in box:
        if 0 in lst:
            count = -1
            break

    return count


N, M = map(int, input().split())
box = []
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
tomato = deque([])
for i in range(M):
    tmp = list(map(int, input().strip().split()))
    for j in range(N):
        # 익은 토마토 위치 큐에 추가
        if tmp[j] == 1:
            tomato.append([i, j])
    box.append((tmp))

ans = bfs()
print(ans)