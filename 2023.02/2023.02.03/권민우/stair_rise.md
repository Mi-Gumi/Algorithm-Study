# [Silver III] 계단 오르기 - 2579 

[문제 링크](https://www.acmicpc.net/problem/2579) 

### 성능 요약

메모리: 31256 KB, 시간: 60 ms

### 분류

다이나믹 프로그래밍(dp)

### 문제 설명

<p>계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7177ea45-aa8d-4724-b256-7b84832c9b97/-/preview/" style="width: 300px; height: 160px;"></p>

<p style="text-align: center;"><그림 1></p>

<p>예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f00b6121-1c25-492e-9bc0-d96377c586b0/-/preview/" style="width: 300px; height: 190px;"></p>

<p style="text-align: center;"><그림 2></p>

<p>계단 오르는 데는 다음과 같은 규칙이 있다.</p>

<ol>
	<li>계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.</li>
	<li>연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.</li>
	<li>마지막 도착 계단은 반드시 밟아야 한다.</li>
</ol>

<p>따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.</p>

<p>각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력의 첫째 줄에 계단의 개수가 주어진다.</p>

<p>둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.</p>

### 출력 

 <p>첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.</p>

---
### Solution
```python
import sys
input = sys.stdin.readline

T = int(input())
# 계단의 개수는 300 이하의 자연수
stair_lst = [0] * 301
point_lst = [0] * 301

# 계단 개수 만큼 점수 쌓기
for i in range(T):
    stair_lst[i] = int(input())

# 계단 밟는 것에 따른 점수 분배
# 1번 계단 밟을 점수, stair_lst[0] = 10점
point_lst[0] = stair_lst[0]
# 2번 계단 밟을 때 최고 점수, 1,2계단을 모두 밟는 경우 = 30점
point_lst[1] = stair_lst[0] + stair_lst[1]
# 1번, 2번계단을 밟는 경우와, 1번, 3번 계단을 밟는 경우 중 더 높은 점수
point_lst[2] = max(stair_lst[0] + stair_lst[2], stair_lst[1] + stair_lst[2])

# 계단 밟는 개수만큼, [0],[1],[2]는 이미 지정 했기 때문에 제외
for i in range(3, T):
    # 1개를 밟은 다음 점프 후 2개를 연속으로 밟는 점수와 2개를 밟고 점프 후 밟는 경우 중 최고점.
    # 해당 형태로 가게 되면
    # 0 = 0
    # 1 = 0,1
    # 2 = max - 0,2 or 1,2
    # 3 = max - (0) + 2 + 3 or (0,1) + 3
    # 4 = max - (0,1) + 3 + 4 or [(0,2) or (1,2)] + 4
    # 5 = max - [(0,2) or (1,2)] + 4 + 5 or [(0) + 2 + 3 or (0,1) + 3] + 5
    point_lst[i] = max(point_lst[i-3] + stair_lst[i-1] + stair_lst[i], point_lst[i-2] + stair_lst[i])

print(point_lst[T-1])
