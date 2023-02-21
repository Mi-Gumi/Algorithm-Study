# [Gold IV] N-Queen - 9663 

[문제 링크](https://www.acmicpc.net/problem/9663) 

### 성능 요약

메모리: 204932 KB, 시간: 29440 ms

### 분류

백트래킹(backtracking), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.</p>

<p>N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. (1 ≤ N < 15)</p>

### 출력 

 <p>첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.</p>
---
### Solution
```python
# 유망성 체크
def ispromising(row):
    for i in range(row):
        # row 이전 까지의 queen들과의 자리 비교
        # abs(board[row]- board[i])는 x 좌표, == abs(row-i):는 y좌표라고 생각하면 편함.
        if board[row] == board[i] or abs(board[row]- board[i]) == abs(row-i):
            return False
    return True

def nqueen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    else:
        for i in range(N):
            board[row] = i
            # 1개의 행에 1개의 퀸만 가능하기 때문에 바로 다음 행의 nqueen을 찾는다.
            if ispromising(row):
                nqueen(row+1)

N = int(input())
board = [0] * N
cnt = 0

nqueen(0)
print(cnt)
```
