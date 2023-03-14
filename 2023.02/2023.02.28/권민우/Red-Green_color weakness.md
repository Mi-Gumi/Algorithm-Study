# [Gold V] 적록색약 - 10026 

[문제 링크](https://www.acmicpc.net/problem/10026) 

### 성능 요약

메모리: 34208 KB, 시간: 80 ms

### 분류

너비 우선 탐색(bfs), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.</p>

<p>크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)</p>

<p>예를 들어, 그림이 아래와 같은 경우에</p>

<pre>RRRBB
GGBBB
BBBRR
BBRRR
RRRRR</pre>

<p>적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)</p>

<p>그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)</p>

<p>둘째 줄부터 N개 줄에는 그림이 주어진다.</p>

### 출력 

 <p>적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.</p>

---
### Solution
```python
import sys
input = sys.stdin.readline
from collections import deque

# 그냥 이번엔 bfs 쓰고 싶어서 썼음, 근데 일반적으로는 bfs가 더 좋다고 하니 좋을듯
def blindness_test(x, y, color, v):
    v[x][y] = 1
    queue = deque([(x, y)])
    
    # 처음돌릴 때 방문하고 방문 값이 초록이면 빨강으로 바꿔주기.
    if painting[x][y] == 'G':
        painting[x][y] = 'R'

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cr, cc = queue.popleft()

        for dr, dc in d:
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and painting[nr][nc] == color:
                queue.append((nr, nc))
                v[nr][nc] = 1
                
                # 재귀가 아니기 때문에 여기에도 넣어줘야함
                if painting[nr][nc] == 'G':
                    painting[nr][nc] = 'R'
    # 구역을 찾는 것이기 때문에 탐색이 끝날때 1값을 반환
    return 1


N = int(input())
painting = [list(input().strip()) for _ in range(N)]
# 두번 돌릴 거기 때문에 방문 자료도 2개
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

# 색약 아닌 사람이 보는 구역의 수
area1 = 0
# 색약인 사람이 보는 구역의 수
area2 = 0

# 색약 아닌 사람의 탐색, 하고 나면 G는 모두 R이 되어있을 것
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            area1 += blindness_test(i, j, painting[i][j], visited1)

# 색약인 사람의 탐색, 빨강과, 파랑 밖에 없음
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            area2 += blindness_test(i, j, painting[i][j], visited2)

print(area1, area2)
