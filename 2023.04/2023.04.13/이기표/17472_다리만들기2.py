'''
1. 각각의 섬마다 번호를 매핑 and 다리만들기에 필요한 좌표와 값을 저장 - bfs
2. 저장된 좌표를 가지고 4방향 탐색을 통해 다른 섬 번호에 도달하면 다리 리스트에 추가
3. 다익스트라 알고리즘을 활용해 최단 경로 도출 
'''
from collections import deque
import heapq, pprint
def bfs(i, j, tmp): # 섬 찾기
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    arr[i][j] = tmp
    land_li.append((i, j, tmp))
    while que:
        i, j = que.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                arr[ni][nj] = tmp # 섬 번호 매핑
                land_li.append((ni, nj, tmp)) # 섬 위치와 값을 저장
                que.append((ni, nj))

def make_node(): # 다리 만들기
    for i, j, num in land_li:
        # 4방향 탐색으로 다른 섬 번호에 도달한 경우 (출발 섬, 도착 섬, 거리) 저장
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dist = 0  # 최소 거리
            end = 0
            ni, nj = i + di, j + dj
            while 1: # 다리 놓기
                if not(0 <= ni < N and 0 <= nj < M): # 범위내에 없으면 종료
                    break
                # 바다인 경우
                if arr[ni][nj] == 0:
                    ni += di
                    nj += dj
                    dist += 1
                # 섬인 경우
                else:
                    if arr[ni][nj] == num: # 같은 섬에 위치
                        break
                    else: # 다른 섬 이동했으면 종료
                        end = arr[ni][nj]
                        break
            # 거리가 2 미만이면 다리 불가능
            if dist < 2:
                continue
            else:
                if end != 0:
                    dist_li.append((num, end, dist))

def prim(s):
    ans = 0
    cnt = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:  # 간선의 개수 최대는 V-1
        dist, node = heapq.heappop(heap)
        if visited[node]: continue  # 이미 방문한 정점이면 지나감
        visited[node] = 1  # 방문안했으면 방문처리
        ans += dist  # 해당 정점까지의 가중치를 더해줌
        cnt += 1
        if cnt == (tmp+1):
            return ans
        for u, w in graph[node]:  # 해당 정점의 간선정보를 불러옴
            if not visited[u]:
                heapq.heappush(heap, [w, u])  # 힙에 넣어줌
    return ans


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
land_li = []
dist_li = []
tmp = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] == 1:
            tmp += 1
            bfs(i, j, tmp)
make_node()
graph = [[] for _ in range(tmp+1)]
visited = [0] * (tmp+1)
# 그래프 생성
for v1, v2, w in dist_li:
    graph[v1].append((v2, w))
ans = prim(1)
for v in visited[1:]:
    if v == 0:
        print(-1)
        break
else:
    print(ans)