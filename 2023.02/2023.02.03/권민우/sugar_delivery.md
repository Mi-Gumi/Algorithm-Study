# [Silver IV] 설탕 배달 - 2839 

[문제 링크](https://www.acmicpc.net/problem/2839) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

다이나믹 프로그래밍(dp), 그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.</p>

<p>상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.</p>

<p>상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)</p>

### 출력 

 <p>상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.</p>

---
### Solution
```python
N = int(input())
cnt = 0

while True:
    if N < 0:
        cnt = -1
        break

    if N % 5 == 0:
        cnt += (N // 5)
        break

    N -= 3
    cnt += 1

print(cnt)
```
```python
import sys
input = sys.stdin.readline

N = int(input())
# 옮겨야 하는 kg 최대수는 5000, 불가능 할 시에 -1 출력으로, 기본 값 -1
sugar = [-1 for _ in range(5001)]

# 3kg와 5kg, cnt 횟수
sugar[3] = 1
sugar[5] = 1

if N <= 5:
    print(sugar[N])

else:
    # 6kg 부터 Nkg까지
    for i in range(6, N+1):
    
        # 5랑 3으로 모두 떨어지면, 횟수가 더 작은 수에서 + 1
        if sugar[i-3] > 0 and sugar[i-5] > 0:
            sugar[i] = min(sugar[i-3], sugar[i-5]) + 1
            
        # 5로 떨어지면 -5kg 값에서 + 1
        elif i % 5 == 0:
            sugar[i] = sugar[i-5] + 1
            
        # 3으로 떨어지면 -3kg 값에서 + 1
        elif i % 3 == 0:
            sugar[i] = sugar[i-3] + 1
    
    print(sugar[N])
