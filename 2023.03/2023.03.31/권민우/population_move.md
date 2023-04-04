# [Gold V] 인구 이동 - 16234 

[문제 링크](https://www.acmicpc.net/problem/16234) 

### 성능 요약

메모리: 31556 KB, 시간: 4020 ms

### 분류

구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

### 문제 설명

<p>N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.</p>

<p>오늘부터 인구 이동이 시작되는 날이다.</p>

<p>인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.</p>

<ul>
	<li>국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.</li>
	<li>위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.</li>
	<li>국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.</li>
	<li>연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.</li>
	<li>연합을 해체하고, 모든 국경선을 닫는다.</li>
</ul>

<p>각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)</p>

<p>둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)</p>

<p>인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.</p>

### 출력 

 <p>인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.</p>

---

### Solution
```python
import sys
# 제곱으로 해야합니다.. ㅎㅎ
sys.setrecursionlimit(10**4)

def dfs(x, y):
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            # L 이상 R 이하
            if not visited[nx][ny] and L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                visited[nx][ny] = 1
                country.append((nx, ny))
                dfs(nx,ny)

d = [(1,0),(0,1),(-1,0),(0,-1)]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

date = 0
# 차이가 범위 안이면 계속 돌려야하니까
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            country = []
            # 경계 허물기
            if not visited[i][j]:
                visited[i][j] = 1
                country.append((i, j))  
                dfs(i,j)
            
            # 연합되어 있다면
            if len(country) > 1:
                # while이 꺼지지 않게
                flag = True
                total = 0
                for r, c in country:
                    total += arr[r][c]
                avg = total // len(country)
                for r, c in country:
                    arr[r][c] = avg
    
    if not flag:
        print(date)
        break

    date += 1
