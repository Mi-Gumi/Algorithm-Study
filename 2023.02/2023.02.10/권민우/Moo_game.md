# [Gold V] Moo 게임 - 5904 

[문제 링크](https://www.acmicpc.net/problem/5904) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>Moo는 술자리에서 즐겁게 할 수 있는 게임이다. 이 게임은 Moo수열을 각 사람이 하나씩 순서대로 외치면 되는 게임이다.</p>

<p>Moo 수열은 길이가 무한대이며, 다음과 같이 생겼다. </p>

<pre>m o o m o o o m o o m o o o o m o o m o o o m o o m o o o o o </pre>

<p>Moo 수열은 다음과 같은 방법으로 재귀적으로 만들 수 있다. 먼저, S(0)을 길이가 3인 수열 "m o o"이라고 하자. 1보다 크거나 같은 모든 k에 대해서, S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)을 합쳐서 만들 수 있다.</p>

<pre>S(0) = "m o o"
S(1) = "m o o m o o o m o o"
S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"</pre>

<p>위와 같은 식으로 만들면, 길이가 무한대인 문자열을 만들 수 있으며, 그 수열을 Moo 수열이라고 한다.</p>

<p>N이 주어졌을 때, Moo 수열의 N번째 글자를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N (1 ≤ N ≤ 10<sup>9</sup>)이 주어진다.</p>

### 출력 

 <p>N번째 글자를 출력한다.</p>

---
### Solution
```python
N = int(input())

# moo
moo = 'moo'
moo_lst = []
# dp[0] = 3글자
moo_lst.append(3)
for i in range(1, N+1):
    # N만큼 dp[i] 만들어 주기
    # dp[0] 생성, append
    moo_lst.append(0)
    moo_lst[i] = moo_lst[i-1] * 2 + i + 3
    # N만큼만 뽑으면 되기 때문에 moo 수열의 길이가 N 이상이면 끊어주기
    if moo_lst[i] >= N:
        break

# idx 위치 조정
n = N - 1

while True:
    # moo_lst[0] 이라는 의미
    if i == 0:
        print(moo[n])
        break
    # N이 moo_lst[i]수열의 가운데 부분보다 크면, 수열만큼 빼주고 뒷부분으로 계산
    if n >= moo_lst[i-1] + i + 3:
        n -= (moo_lst[i-1] + i + 3)
        i -= 1
    # N이 가운데 부분에 있다면, 시작하는 순간이 아니면 'o'이기 때문에 같은 경우에만 'm'
    elif n >= moo_lst[i-1]:
        if n == moo_lst[i-1]:
            print('m')
        else:
            print('o')
        break
    # N이 가운데 수열보다 앞 부분에 있다면, 현재 수열에서 볼 이유가 없으므로 수열 한단계 낮추기
    else:
        i -= 1
