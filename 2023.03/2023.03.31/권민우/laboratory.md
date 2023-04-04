# [Gold III] 연구소 3 - 17142 

[문제 링크](https://www.acmicpc.net/problem/17142) 

### 성능 요약

메모리: 34244 KB, 시간: 504 ms

### 분류

그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

### 문제 설명

<p>인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.</p>

<p>연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.</p>

<p>예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.</p>

<pre>2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2</pre>

<p>M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.</p>

<pre>* 6 5 4 - - 2
5 6 - 3 - 0 1
4 - - 2 - 1 2
3 - 2 1 2 2 3
2 2 1 0 1 - -
1 - 2 1 2 3 4
0 - 3 2 3 4 *</pre>

<p>시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.</p>

<pre>0 1 2 3 - - 2
1 2 - 3 - 0 1
2 - - 2 - 1 2
3 - 2 1 2 2 3
3 2 1 0 1 - -
4 - 2 1 2 3 4
* - 3 2 3 4 *</pre>

<p>연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.</p>

### 입력 

 <p>첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.</p>

<p>둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.</p>

---

### Solution
```python
import sys
from collections import deque
import copy

input = sys.stdin.readline

# 0이 없으면 전부 퍼진 것
def complete(lst):
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                return False
    return True

def bfs(lst):
    tmp_arr = copy.deepcopy(arr)
    queue = deque(lst)
    visited = [[0] * N for _ in range(N)]

    for i in queue:
        visited[i[0]][i[1]] = 1

    while queue:
        r, c, time = queue.popleft()

        for dr, dc in d:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if tmp_arr[nr][nc] == 0:
                    tmp_arr[nr][nc] = time
                    visited[nr][nc] = 1
                    if time >= best_time:
                        return best_time
                    queue.append((nr, nc, time + 1))
                elif tmp_arr[nr][nc] == -1:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, time + 1))

    max_time = 0
    
    # 안퍼지면 best_time 그대로 반환
    if not complete(tmp_arr):
        return best_time
    
    # 퍼졌다면 퍼진 시간 찾기
    for i in tmp_arr:
        max_time = max(max(i), max_time)
    
    # 퍼진시간 반환
    return max_time

# cnt M개면 바이러스 선정 끝, bfs 돌리기
def virus(idx, cnt):
    global best_time
    if cnt == M:
        time = bfs(use_virus)
        best_time = min(best_time, time)
        return
    
    # 순열, 사용할 바이러스 위치 선정해주기
    for i in range(idx, len_virus):
        if not virus_used[i]:
            virus_used[i] = 1
            use_virus.append(virus_lst[i])
            virus(i+1, cnt + 1)
            virus_used[i] = 0
            use_virus.pop()

# main

N, M = map(int, input().split())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = [list(map(int, input().split())) for _ in range(N)]
virus_lst = []
use_virus = []
best_time = 1e9

# 바이러스 모두 -1로 바꿔주기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            arr[i][j] = -1
            # 바이러스가 퍼지는 시간과, 위치 넣어주기
            virus_lst.append((i, j, 1))
        
        # 벽은 -2로 바꾸기
        elif arr[i][j] == 1:
            arr[i][j] = -2

len_virus = len(virus_lst)
virus_used = [0] * len_virus

virus(0, 0)

# 바뀌지 않았으면 다 
if best_time == 1e9:
    best_time = -1

print(best_time)
