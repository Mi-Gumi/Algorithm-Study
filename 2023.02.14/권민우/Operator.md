# [Silver I] 연산자 끼워넣기 - 14888 

[문제 링크](https://www.acmicpc.net/problem/14888) 

### 성능 요약

메모리: 31388 KB, 시간: 64 ms

### 분류

백트래킹(backtracking), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>N개의 수로 이루어진 수열 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.</p>

<p>우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.</p>

<p>예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.</p>

<ul>
	<li>1+2+3-4×5÷6</li>
	<li>1÷2+3+4-5×6</li>
	<li>1+2÷3×4-5+6</li>
	<li>1÷2×3-4+5+6</li>
</ul>

<p>식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.</p>

<ul>
	<li>1+2+3-4×5÷6 = 1</li>
	<li>1÷2+3+4-5×6 = 12</li>
	<li>1+2÷3×4-5+6 = 5</li>
	<li>1÷2×3-4+5+6 = 7</li>
</ul>

<p>N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. </p>

### 출력 

 <p>첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.</p>

---
### Solution
```python
import sys
input = sys.stdin.readline

N = int(input())

num_lst = list(map(int, input().split()))
# 연산자 개수 받기
plus, minus, multi, div = map(int, input().split())
# 무한의 값으로 1e9를 사용
max_, min_ = -1e9, 1e9

# 사용한 숫자, 연산한 값, 연산자 개수
def dfs(depth, total, plus, minus, multi, div):
    global max_, min_

    # N개를 모두 사용했으면 마지막에 나온 total과, max, min을 비교해서 넣기
    if depth == N:
        max_ = max(total, max_)
        min_ = min(total, min_)
        return
    
    # 처음 해당 지점에 왔을 때, (1, 1, 2, 1, 1, 1)
    if plus:
        dfs(depth + 1, total + num_lst[depth], plus-1, minus, multi, div)
    # 처음 해당 지점에 왔을 때, (1, 1, 2, 1, 1, 1)
    if minus:
        dfs(depth + 1, total - num_lst[depth], plus, minus-1, multi, div)
    # 처음 해당 지점에 왔을 때, (1, 1, 2, 1, 1, 1)
    if multi:
        dfs(depth + 1, total * num_lst[depth], plus, minus, multi-1, div)
    # 처음 해당 지점에 왔을 때, (1, 1, 2, 1, 1, 1)
    if div:
        dfs(depth + 1, int(total / num_lst[depth]), plus, minus, multi, div-1)
    # 즉, 하나를 소모한 뒤 4개의 연산자로 이루어 질 수 있는 모든 경우의 수를 확인함.

dfs(1, num_lst[0], plus, minus, multi, div)
print(max_)
print(min_)
