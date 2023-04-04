# [Gold V] 빗물 - 14719 

[문제 링크](https://www.acmicpc.net/problem/14719) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14719/1.png" style="height:79px; width:146px"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14719/2.png" style="height:79px; width:143px"></p>

<p>비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?</p>

### 입력 

 <p>첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)</p>

<p>두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.</p>

<p>따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.</p>

### 출력 

 <p>2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.</p>

<p>빗물이 전혀 고이지 않을 경우 0을 출력하여라.</p>

---

### Solution
```python
import sys

input = sys.stdin.readline

H, W = map(int, input().split())
lst = list(map(int, input().split()))
# 빗물의 총량
water = 0
# 가장 높은 벽
higher = [0, 0]
length = len(lst)

# 그냥 max 치면 되는데 왜 이렇게 한지 모르겠음
for i in range(length):
    if lst[i] > higher[0]:
        higher = (lst[i], i)

# 앞에서 부터 빗물 모아주기
high = lst[0]
for i in range(1, higher[1]):
    if high > lst[i]:
        water += high - lst[i]
    
    # 높은 벽이 나타나면 갱신
    elif high < lst[i]:
        high = lst[i]

# 뒤에서 부터 빗물 모아주기
high = lst[-1]
for i in range(length - 2, higher[1], -1):

    if high > lst[i]:
        water += high - lst[i]

    elif high < lst[i]:
        high = lst[i]

print(water)
