# [Gold IV] 연구소 - 14502 

[문제 링크](https://www.acmicpc.net/problem/14502) 

### 성능 요약

메모리: 119388 KB, 시간: 1508 ms

### 분류

구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

### 문제 설명

<p>인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.</p>

<p>연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. </p>

<p>일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.</p>

<p>예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.</p>

<pre>2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0</pre>

<p>이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.</p>

<p>2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.</p>

<pre>2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0</pre>

<p>바이러스가 퍼진 뒤의 모습은 아래와 같아진다.</p>

<pre>2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0</pre>

<p>벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.</p>

<p>연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)</p>

<p>둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.</p>

<p>빈 칸의 개수는 3개 이상이다.</p>

### 출력 

 <p>첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.</p>

---
### Solution
```python
import sys
from collections import deque

sys.stdin.readline
input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 벽 3개가 세워지면 세이프 존을 확인하고 다른 곳에 벽을 세움
def back(cnt):
    global best_safe_area
    if cnt == 3:
        safe_area = bfs()

        if safe_area > best_safe_area:
            best_safe_area = safe_area

        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
                back(cnt)
                arr[i][j] = 0
                cnt -= 1

# 바이러스 확산
def bfs():
    visited = [[0] * M for _ in range(N)]
    for i, j in virus:
        visited[i][j] = 1
    cnt = 0

    tmp_virus = deque([])

    for i in virus:
        tmp_virus.append(i)

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                visited[i][j] = 1

    while tmp_virus:
        r, c = tmp_virus.popleft()

        for dr, dc in d:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 0:
                tmp_virus.append((nr, nc))
                visited[nr][nc] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1

    return cnt

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
best_safe_area = -1e9

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))

back(0)
print(best_safe_area)
