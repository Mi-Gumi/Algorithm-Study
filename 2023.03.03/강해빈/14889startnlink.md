# [Silver II] 스타트와 링크 - 14889 

[문제 링크](https://www.acmicpc.net/problem/14889) 

### 성능 요약

메모리: 60792 KB, 시간: 2444 ms

### 분류

백트래킹(backtracking), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.</p>

<p>BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 S<sub>ij</sub>는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 S<sub>ij</sub>의 합이다. S<sub>ij</sub>는 S<sub>ji</sub>와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S<sub>ij</sub>와 S<sub>ji</sub>이다.</p>

<p>N=4이고, S가 아래와 같은 경우를 살펴보자.</p>

<table class="table table-bordered" style="width:20%">
	<thead>
		<tr>
			<th>i\j</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>1</th>
			<td> </td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<th>2</th>
			<td>4</td>
			<td> </td>
			<td>5</td>
			<td>6</td>
		</tr>
		<tr>
			<th>3</th>
			<td>7</td>
			<td>1</td>
			<td> </td>
			<td>2</td>
		</tr>
		<tr>
			<th>4</th>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.</p>

<ul>
	<li>스타트 팀: S<sub>12</sub> + S<sub>21</sub> = 1 + 4 = 5</li>
	<li>링크 팀: S<sub>34</sub> + S<sub>43</sub> = 2 + 5 = 7</li>
</ul>

<p>1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.</p>

<ul>
	<li>스타트 팀: S<sub>13</sub> + S<sub>31</sub> = 2 + 7 = 9</li>
	<li>링크 팀: S<sub>24</sub> + S<sub>42</sub> = 6 + 4 = 10</li>
</ul>

<p>축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.</p>

### 입력 

 <p>첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 S<sub>ij</sub> 이다. S<sub>ii</sub>는 항상 0이고, 나머지 S<sub>ij</sub>는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.</p>

### 출력 

 <p>첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.</p>
---
```python
N = int(input())
S = [[0] + list(map(int, input().split())) for _ in range(N)]
S.insert(0, [0 for _ in range(N+1)])
# pprint(S) # 번호 != 인덱스
# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 2, 3],
#  [0, 4, 0, 5, 6],
#  [0, 7, 1, 0, 2],
#  [0, 3, 4, 5, 0]]
start = []
link = []
num = [i for i in range(1, N + 1)] # 팀원 번호

from itertools import combinations # 중복 없는 순열
team = list(combinations(num, N // 2)) # 팀을 이룰 수 있는 모든 경우의 수
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
#   A       B       C       C       B       A
for i in range(len(team) // 2): # 스타트팀과 링크팀 나누기
    start.append(team[i])
    link.append(team[-(i + 1)])

mn = [] # 능력치 차이
for a in range(len(start)): # 한 쌍인 두 팀의 인덱스값이 같음
    start_power = 0
    link_power = 0    
    compare = 0
    for b in start[a]: # 스타트팀 능력치 # (1, 2)
        for c in start[a]:
            start_power += S[b][c]
            # print('b:', b, 'c:', c, '  ', end=' ')
            # A의 경우) b: 1 c: 1   b: 1 c: 2   b: 2 c: 1   b: 2 c: 2
            # B의 경우) b: 1 c: 1   b: 1 c: 3   b: 3 c: 1   b: 3 c: 3
            # C의 경우) b: 1 c: 1   b: 1 c: 4   b: 4 c: 1   b: 4 c: 4
    for d in link[a]: # 링크팀 능력치 # (3, 4)
        for e in link[a]:
            link_power += S[d][e] 
    compare = abs(start_power - link_power) # 능력치 차이
    mn.append(compare)
print(min(mn)) # 최솟값
```
