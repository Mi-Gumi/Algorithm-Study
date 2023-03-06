def bfs(s, g):
    queue = [s]
    visited[s] = 1  # 출발층 방문체크
    while queue:
        v = queue.pop(0)
        if v == g:      # 도착
            return True
        for d in dd:    # 위 아래
            nfloor = v + d  # 층수 체크 and 방문 체크
            if 1 <= nfloor <= F and visited[nfloor] == 0:
                queue.append(nfloor)
                visited[nfloor] = visited[v] + 1  # 버튼 누른 횟수
    return False        # 갈 수 있는 경우를 모두 방문 했음에도 도착 못 함


F, S, G, U, D = map(int, input().split())
# 최대층수, 출발지, 도착지, 위로, 아래로

visited = [0] * (F + 1)  # 방문 체크 : 같은 층을 두번 가는 건 무쓸모
dd = (U, -D)

isGood = bfs(S, G)  # BFS 가능 여부를 반환값으로
if isGood:
    print(visited[G] - 1)
else:
    print('use the stairs')
