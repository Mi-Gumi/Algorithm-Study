'''
1. 빨간공과 파란공 좌표 찾기
2. BFS를 활용해 상 하 좌 우를 모두 탐색후에 정답처리
3. 파란공이 단독으로 들어간 경우와 빨간공과 같이 들어간 경우 모두 실패 케이스기 때문에
파란공을 먼저 이동시켜 홀인 여부를 확인
4. 빨간공을 이동시켜 빨간공만 홀인되었으면 탐색을 멈추고 정답 도출
5. 이동후의 두 공의 좌표가 같은 경우 조건에 따라 좌표 조절
'''
from collections import deque
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ri, rj = 0, 0
bi, bj = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R': # 빨간공 좌표
            ri, rj = i, j
        if arr[i][j] == 'B': # 파란공 좌표
            bi, bj = i, j
# 방문체크 할 리스트
visited = [[ri, rj, bi, bj]]
def bfs():
    que = deque()
    que.append((ri, rj, 0, bi, bj))
    ans = -1 # 정답
    while que:
        sri, srj, cnt, sbi, sbj = que.popleft()

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nri, nrj = sri, srj
            nbi, nbj = sbi, sbj
            flag_blue = 0
            blue, red = 0, 0
            # 파란공 이동
            while 1:
                if arr[nbi+di][nbj+dj] != '#' and arr[nbi+di][nbj+dj] != 'O':
                    nbi += di
                    nbj += dj
                    blue += 1
                else:
                    # 파란공인 홀인이면 현재 케이스를 무시하고 다음으로 continue
                    if arr[nbi+di][nbj+dj] == 'O':
                        flag_blue = 1
                    break

            if flag_blue == 1:
                continue
            # 빨간공 이동
            while 1:
                if arr[nri+di][nrj+dj] != '#' and arr[nri+di][nrj+dj] != 'O':
                    nri += di
                    nrj += dj
                    red += 1
                else:
                    # 빨간공 홀인이면 탐색을 종료하고 정답 반환
                    if arr[nri+di][nrj+dj] == 'O':
                        ans = cnt + 1
                        return ans
                    break
            # 이동 후 동일 좌표에 위치한 경우, 이동 거리순으로 비교 -> 더 많이 이동한 공을 현재 위치 이전으로 조절
            if (nri, nrj) == (nbi, nbj):
                if blue > red:
                    nbi -= di
                    nbj -= dj
                else:
                    nri -= di
                    nrj -= dj
            if [nri, nrj, nbi, nbj] not in visited:
                # 10회를 초과할 경우는 큐에 추가하지 않음
                if cnt+1 < 10:
                    visited.append([nri, nrj, nbi, nbj])
                    que.append((nri, nrj, cnt+1, nbi, nbj))
    # 10회를 초과한 경우
    return ans

print(bfs())
