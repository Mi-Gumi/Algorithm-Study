from itertools import combinations
from collections import deque
import copy

def one_cnt(tmp_arr): # 적이 남아있는지 확인하는 함수
    for lst in tmp_arr:
        if lst.count(1):
            return True
    return False

def bfs(c):
    que = deque()
    # 궁수의 위치 추가
    que.append((N-1, c))
    while que:
        si, sj = que.popleft()
        distance = abs(N-si) + abs(c-sj)
        if distance <= D: # 거리 확인
            if tmp_arr[si][sj] == 1: # 적을 찾으면
                return (si, sj) # 적의 위치 반환
            for di, dj in ((0, -1), (-1, 0), (0, 1)): # 왼쪽부터 탐색
                ni = si + di
                nj = sj + dj
                if 0 <= ni < N and 0 <= nj < M:
                    que.append((ni, nj))
        else:
            return # 거리 이상이면 종료

N, M, D = map(int, input().split())

arr = deque(list(map(int, input().split())) for _ in range(N))
ans = 0

# 궁수가 위치할 수 있는 조합을 기준으로 bfs 탐색
for combi in combinations(list(range(M)), 3):
    die = 0
    # 2차원 배열을 여러번 사용해야 되기때문에 깊은 복사 진행
    tmp_arr = copy.deepcopy(arr)

    while one_cnt(tmp_arr): # 적 여부 확인
        enermy = set() # 적의 위치 중복 방지

        for c in combi:
            position = bfs(c)
            if position:
                enermy.add(position) # 적의 위치 추가

        for x, y in enermy: # 죽인 적을 0으로 변경
            tmp_arr[x][y] = 0

        # 죽인 적의 수 추가 및 적의 위치 이동
        die += len(enermy)
        tmp_arr.pop()
        tmp_arr.appendleft([0] * M)
    ans = max(ans, die)
print(ans)




