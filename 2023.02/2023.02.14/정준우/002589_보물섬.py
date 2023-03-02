# 난 deque가 너무 좋아
from collections import deque
# 난 sys도 너무 좋아
import sys

# 최단거리 탐색 = 노드 간 최단 거리를 측정하는 BFS
def useless_hook(x, y):
    deq = deque()
    # 시작점 추가
    deq.append((x, y))

    # 함수 밖에서 쓸 farthest 변수 global 선언
    global farthest

    # deq 빌 때까지
    while deq:
        # 시작점부터 탐색 시작하며 큐에서 제거
        x, y = deq.popleft()

        # 시작점의 상하좌우 둘러보기
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 범위 넘어서면 다른 점으로
            if new_x < 0 or new_x >= row or new_y < 0 or new_y >= col:
                continue

            # 가려는 곳이 바다면 다른 점으로
            if island[x][y] == 'W':
                continue

            # 가려는 곳이 땅이고, 아직 지나가지 않은 길이라면,
            if island[new_x][new_y] == 'L' and distance[new_x][new_y] == -1:
                # 새로운 점은 지금까지 이동한 거리에 +1
                distance[new_x][new_y] = distance[x][y] + 1
                # 새로 이동한 점부터 다시 탐색을 시작하기 위해 큐에 해당 위치 추가
                deq.append((new_x, new_y))

                # 새로 나온 거리가 가장 긴 거리라면 변수 수정
                if farthest < distance[new_x][new_y]:
                    farthest = distance[new_x][new_y]



row, col = map(int, sys.stdin.readline().split())

island = [list(sys.stdin.readline()) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

farthest = 0

for i in range(row):
    for j in range(col):
        # 새롭게 탐색을 시작해야 할 점을 찾으면,
        if island[i][j] == 'L':
            # 거리 측정을 위한 배열 초기화
            distance = [[-1] * col for _ in range(row)]
            # 시작점은 거리 0으로 수정
            distance[i][j] = 0
            useless_hook(i, j)

print(farthest)