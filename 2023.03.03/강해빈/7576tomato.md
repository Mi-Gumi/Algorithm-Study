# [Gold V] 토마토 - 7576 

[문제 링크](https://www.acmicpc.net/problem/7576) 

### 성능 요약

메모리: 178936 KB, 시간: 2004 ms

### 분류

너비 우선 탐색(bfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/de29c64f-dee7-4fe0-afa9-afd6fc4aad3a/-/preview/" style="width: 215px; height: 194px;"></p>

<p>창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.</p>

<p>토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.</p>

### 입력 

 <p>첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.</p>

<p>토마토가 하나 이상 있는 경우만 입력으로 주어진다.</p>

### 출력 

 <p>여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.</p>

---
```python
dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque
def bfs(one): # 익은 토마토(들) (동시에) 탐색
    level = 0 # 날짜
    queue = deque()
    for j in one:
        queue.append([j[0], j[1], level]) # 각각 익은 토마토 탐색 위해 추가
        visited[j[0]][j[1]] = True # 방문 처리

    while queue:
        ripe = queue.popleft() # 탐색 대상
        level = ripe[2] # 날짜 업데이트
        for i in range(4): # 사방 탐색
            nx = ripe[0] + dx[i]
            ny = ripe[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0: # 안 익었으면 익혀
                    box[nx][ny] = 1
                    visited[nx][ny] = True
                    # 그대로 cnt 넣으면 4번 카운트됨
                    queue.append([nx, ny, level + 1]) # 다음 탐색 대상과 날짜 카운트
    return level # 날짜 반환

M, N = map(int, input().split()) # M 가로칸 수, N 세로칸 수 
box = [list(map(int, input().split())) for _ in range(N)] # 토마토 상태
visited = [[False for _ in range(M)] for _ in range(N)] # 방문 처리
flag = True

one = [] # 익은 토마토 리스트
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            one.append([x, y])
            
result = bfs(one) # 최소 날짜 구하기

for xx in range(N):
    for yy in range(M):
        if box[xx][yy] == 0: # 탐색한 후에도 모두 익지 못하는 상황
            flag = False 

if flag == True:
    print(result)
else:
    print(-1)
```
