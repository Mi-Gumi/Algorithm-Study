# [Silver II] 창고 다각형 - 2304 

[문제 링크](https://www.acmicpc.net/problem/2304) 

### 성능 요약

메모리: 31256 KB, 시간: 80 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 스택(stack)

### 문제 설명

<p>N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다. 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.</p>

<ol>
	<li>지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.</li>
	<li>지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.</li>
	<li>지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.</li>
	<li>지붕의 가장자리는 땅에 닿아야 한다.</li>
	<li>비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.</li>
</ol>

<p>그림 1은 창고를 옆에서 본 모습을 그린 것이다. 이 그림에서 굵은 선으로 표시된 부분이 지붕에 해당되고, 지붕과 땅으로 둘러싸인 다각형이 창고를 옆에서 본 모습이다. 이 다각형을 창고 다각형이라고 하자.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/JudgeOnline/upload/201011/cd.png" style="height:331px; width:483px"></p>

<p style="text-align: center;">그림1 . 기둥과 지붕(굵은 선)의 예</p>

<p>창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다. 그림 1에서 창고 다각형의 면적은 98 ㎡이고, 이 경우가 가장 작은 창고 다각형이다.</p>

<p>기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. N은 1 이상 1,000 이하이다. 그 다음 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다. L과 H는 둘 다 1 이상 1,000 이하이다.</p>

### 출력 

 <p>첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력한다.</p>
---
### Solution
```python
N = int(input())

lst = []
for i in range(N):
    L, H = map(int,input().split())
    lst.append([L,H])

# x축을 기준으로 정렬
lst.sort(key=lambda x: x[0])
 
# 가장 높은 기둥의 면적을 구하고 미리 더해주기
value = 0
for i in range(len(lst)) :
    if lst[i][1] > value :
        value = lst[i][1]
        idx = i

# 처음 높이는 첫번째 기둥의 높이 
high = lst[0][1]

# 가장 높은 기둥 전까지 돌면서 면적을 추가해주기 
# value에 면적을 계산해서 더해주고 높이를 다음 기둥으로 갱신
for i in range(idx) :
    if high < lst[i+1][1] :
        value += high * (lst[i+1][0]-lst[i][0])
        high = lst[i+1][1]
    # 높이가 낮다면 이전 높이를 그대로하고 현재 면적을 더하기
    else :
        value += high * (lst[i+1][0] - lst[i][0])

# 뒤에서도 가장 큰 기둥까지 면적을 추가
high = lst[-1][1]

for i in range(N-1, idx, -1) :
    if high < lst[i-1][1] :
        value += high * (lst[i][0]-lst[i-1][0])
        high = lst[i-1][1]
    else :
        value += high * (lst[i][0] - lst[i-1][0])

print(value)
