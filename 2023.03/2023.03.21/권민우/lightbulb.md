# [Gold V] 전구와 스위치 - 2138 

[문제 링크](https://www.acmicpc.net/problem/2138) 

### 성능 요약

메모리: 33640 KB, 시간: 7432 ms

### 분류

그리디 알고리즘

### 문제 설명

<p>N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.</p>

<p>N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.</p>

### 출력 

 <p>첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.</p>

---

### Solution
```python
import sys
import copy
input = sys.stdin.readline

# 스위치 누르면 바꾸기
def switch(arr, idx):
    if arr[idx] == 0:
        arr[idx] = 1
    else:
        arr[idx] = 0

    if arr[idx - 1] == 0:
        arr[idx - 1] = 1
    else:
        arr[idx - 1] = 0
    
    # 마지막 전구면 여기까지만
    if idx == N - 1:
        return
    
    if arr[idx + 1] == 0:
        arr[idx + 1] = 1
    else:
        arr[idx + 1] = 0

# 2가지 경우 나눠서, 첫 스위치 켰을때, 껐을때
def partition(onoff, cnt):
    if cnt == 1:
        if onoff[0] == 0:
            onoff[0] = 1
        else:
            onoff[0] = 0

        if onoff[1] == 0:
            onoff[1] = 1
        else:
            onoff[1] = 0
    
    for i in range(1, N):
        # 왼쪽 전구 기준으로, 여긴 지나가면 못 고침
        if onoff[i-1] != after_lst[i-1]:
            switch(onoff, i)
            cnt += 1

        if onoff == after_lst:
            return cnt

    if onoff != after_lst:
        return -1

N = int(input())

befo_lst = list(map(int, input().strip()))
after_lst = list(map(int, input().strip()))
cnt = 0

# 두 가지 경우를 나눠서 답을 구해서 비교해보는게 중요
ans1 = partition(copy.deepcopy(befo_lst), 0)
ans2 = partition(copy.deepcopy(befo_lst), 1)

if ans1 >= 0 and ans2 >= 0:
    print(min(ans1, ans2))

elif ans1 >= 0 and ans2 < 0:
    print(ans1)

elif ans1 < 0 and ans2 >= 0:
    print(ans2)

else:
    print(-1)
