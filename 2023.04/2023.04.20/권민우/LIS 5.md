# [Platinum V] 가장 긴 증가하는 부분 수열 5 - 14003 

[문제 링크](https://www.acmicpc.net/problem/14003) 

### 성능 요약

메모리: 227660 KB, 시간: 2992 ms

### 분류

이분 탐색, 가장 긴 증가하는 부분 수열: O(n log n)

### 문제 설명

<p>수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.</p>

<p>예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {<strong>10</strong>, <strong>20</strong>, 10, <strong>30</strong>, 20, <strong>50</strong>} 이고, 길이는 4이다.</p>

### 입력 

 <p>첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.</p>

<p>둘째 줄에는 수열 A를 이루고 있는 A<sub>i</sub>가 주어진다. (-1,000,000,000 ≤ A<sub>i</sub> ≤ 1,000,000,000)</p>

### 출력 

 <p>첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.</p>

<p>둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.</p>

---

### Solution
```python
import sys
input = sys.stdin.readline

def binary_search(num):
    left = 0
    right = len(lsst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lsst[mid] == num:
            return mid
        elif lsst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return left

N = int(input())
lst = list(map(int, input().split()))
lsst = [lst[0]]
dp = [(0, lst[0])]

for i in range(1, N):
    if lsst[-1] < lst[i]:
        lsst.append(lst[i])
        dp.append((len(lsst)-1, lst[i]))

    else:
        idx = binary_search(lst[i])
        lsst[idx] = lst[i]
        dp.append((idx, lst[i]))

best_cnt = len(lsst)
print(best_cnt)

ans = []
for i in range(N-1, -1, -1):
    if dp[i][0] == best_cnt-1:
        ans.append(dp[i][1])
        best_cnt -= 1

print(*ans[::-1])
