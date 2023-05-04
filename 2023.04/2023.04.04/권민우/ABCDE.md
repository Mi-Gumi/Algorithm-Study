# [Gold V] ABCDE - 13023 

[문제 링크](https://www.acmicpc.net/problem/13023) 

### 성능 요약

메모리: 116596 KB, 시간: 652 ms

### 분류

그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹

### 문제 설명

<p>BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.</p>

<p>오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.</p>

<ul>
	<li>A는 B와 친구다.</li>
	<li>B는 C와 친구다.</li>
	<li>C는 D와 친구다.</li>
	<li>D는 E와 친구다.</li>
</ul>

<p>위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.</p>

<p>둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.</p>

### 출력 

 <p>문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.</p>

---

### Solution
```python
import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    # cnt 4까지면 모든 논제가 참. 친구 이어짐, ans를 1로 바꾸고 리턴
    if cnt == 4:
        ans = 1
        return
    
    # idx번째 리스트에 들어있는 친구들 부르기
    for i in human_lst[idx]:
        # 친구 확인 안된 애가 있으면
        if not visited[i]:
            # 인지시키고
            visited[i] = 1
            # 탐구하기
            dfs(i, cnt + 1)
            # 사실여부 확인되면 리턴
            if ans == 1:
                return
            visited[i] = 0

N, M = map(int, input().split())
human_lst = [[] for _ in range(N)]
# 방문여부 확인을 위함
visited = [0] * (N+1)
ans = 0

for i in range(M):
    a, b = map(int, input().split())

    human_lst[a].append(b)
    human_lst[b].append(a)

# 모든 요소에 A 역할 주기
for i in range(N):
    visited[i] = 1
    dfs(i, 0)
    # 답이 나오면 그냥 끝내기
    if ans == 1:
        break
    visited[i] = 0

print(ans)
