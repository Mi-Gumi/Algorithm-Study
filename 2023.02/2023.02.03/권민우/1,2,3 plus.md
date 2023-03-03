# [Silver III] 1, 2, 3 더하기 - 9095 

[문제 링크](https://www.acmicpc.net/problem/9095) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

다이나믹 프로그래밍(dp)

### 문제 설명

<p>정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.</p>

<ul>
	<li>1+1+1+1</li>
	<li>1+1+2</li>
	<li>1+2+1</li>
	<li>2+1+1</li>
	<li>2+2</li>
	<li>1+3</li>
	<li>3+1</li>
</ul>

<p>정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.</p>

### 출력 

 <p>각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.</p>

---
### Solution
```python
import sys
input = sys.stdin.readline

T = int(input())
num_lst = [0] * 11

num_lst[0] = 1
num_lst[1] = 2 
num_lst[2] = 4 

 # 1이 되는 경우의 수는 + 3
 # 2가 되는 경우의 수는 + 2
 # 3이 되는 경우의 수는 + 1 하면 다음 수가 될 수 있는 경우의 수

for _ in range(T):
    n = int(input())
    if n > 3:
        for j in range(3,n):
            num_lst[j] = num_lst[j-3] + num_lst[j-2] + num_lst[j-1]

    print(num_lst[n-1])
