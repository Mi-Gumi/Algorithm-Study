# [Gold III] 캐슬 디펜스 - 17135 

[문제 링크](https://www.acmicpc.net/problem/17135) 

### 성능 요약

메모리: 122020 KB, 시간: 464 ms

### 분류

구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

### 문제 설명

<p>캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.</p>

<p>성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. </p>

<p>게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.</p>

<p>격자판의 두 위치 (r<sub>1</sub>, c<sub>1</sub>), (r<sub>2</sub>, c<sub>2</sub>)의 거리는 |r<sub>1</sub>-r<sub>2</sub>| + |c<sub>1</sub>-c<sub>2</sub>|이다.</p>

### 입력 

 <p>첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.</p>

### 출력 

 <p>첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.</p>

---

### Solution
```python
import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

def bfs(loca,distance):
    attack = deque()
    attack.append([N, loca , distance])
    visited = [[0 for _ in range(M)] for _ in range(N+1)]
    visited[N][loca] = 1
    possible = []

    while attack:
        r, c, distance = attack.popleft()

        if tmp_arr[r][c] == 1 and distance <= D:
            possible.append([distance, c, r])
            continue
        
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and distance <= D:
                    attack.append([nr,nc,distance+1])
                    visited[nr][nc] = 1
    
    return sorted(possible)

def next_round():
    for i in range(N-1, 0, -1):
        for j in range(M):
            tmp_arr[i][j] = tmp_arr[i-1][j]

    for i in range(M):
        tmp_arr[0][i] = 0

def is_empty(tmp_arr):
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 1:
                return False
    return True

d = [(0, -1), (-1, 0), (0, 1)]

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] + [[-1] * M]
best_point = 0

archer = [i for i in range(M)]

for i in combinations(archer, 3):
    tmp_arr = copy.deepcopy(arr)
    point = 0

    while not is_empty(tmp_arr):
        attack_possible = []
        for j in range(3):
            search_monster = bfs(i[j], 0)

            if search_monster:
                search_monster = search_monster[0]
                attack_possible.append((search_monster[2], search_monster[1]))

        attack_possible = list(set(attack_possible))

        for j in attack_possible:
            tmp_arr[j[0]][j[1]] = 0
            point += 1
        
        next_round()
    
    best_point = max(best_point, point)

print(best_point)
