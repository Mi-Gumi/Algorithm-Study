import sys
from collections import deque
import heapq

def find_island(x,y):
    global island_num
    q = deque()
    q.append((x,y))
    while q:
        i,j = q.popleft()
        visited[i][j] = 1
        arr[i][j] = island_num
        island.append([i,j,island_num])
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni,nj))
                
    island_num += 1

def find_bridge():
    for i,j,num in island:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            cnt = 0
            while True:
                if 0 <= ni < n and 0 <= nj < m :
                    if arr[ni][nj] == 0:
                        cnt += 1
                        ni = ni + di[k]
                        nj = nj + dj[k]
                        continue
                    elif arr[ni][nj] != 0 and arr[ni][nj] != num and cnt > 1:
                        bridge.append([cnt, num, arr[ni][nj]])
                        break
                    if cnt < 2:
                        break
                else:
                    break


def prim(s):
    D[s] = 0
    heap = []
    heapq.heappush(heap,(0,s))
    while heap:
        d, s = heapq.heappop(heap)

        if D[s] < d:
            continue

        for nw,nx in adj_mat[s]:
            nd = nw
            if D[nx] > nd:
                heapq.heappush(heap,(nd,nx))
                D[nx] = nd
    return D       

n,m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
island_num = 1
island = deque()
bridge = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            find_island(i,j)

find_bridge()
INF = 10**9
D = [INF] * island_num
adj_mat = [[] for _ in range(island_num)]
for i in range(len(bridge)):
    d,s,e = bridge.popleft()
    adj_mat[s].append((d,e))
D[0] = 0
prim(island_num-1)
if max(D) != INF:
    print(sum(D))
else:
    print(-1)
