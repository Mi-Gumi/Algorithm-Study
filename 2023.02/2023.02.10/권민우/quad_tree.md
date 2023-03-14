# [Silver I] 쿼드트리 - 1992 

[문제 링크](https://www.acmicpc.net/problem/1992) 

### 성능 요약

메모리: 31256 KB, 시간: 48 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.</p>

<p>주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다</p>

<p style="text-align: center;"><img alt="" height="186" src="https://www.acmicpc.net/JudgeOnline/upload/201007/qq.png" width="408"></p>

<p>위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "<code>(0(0011)(0(0111)01)1)</code>"로 표현된다.  N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.</p>

### 출력 

 <p>영상을 압축한 결과를 출력한다.</p>

---
### Solution
```python
import sys
input = sys.stdin.readline

# row, col을 받아서 같은지 체크
def dotcheck(row, col, size):
    dot = board[row][col]

    # 다르다면 False를 반환
    for j in range(row, row + size):
        for k in range(col, col + size):
            if dot != board[j][k]:
                return False
    # 별 일 없음 = 점이 같음, 그러면 True 반환
    return True

# 영상을을 수거하거나 자르기
def partition(row, col, size):
    # 점이 같다면 점 종류에 따라 종이를 += 1
    if dotcheck(row, col, size):
        if board[row][col] == '0':
            print('0',end='')
        else:
            print('1',end='')
        return

    # 같지 않으면반갈
    newsize = size // 2
    print('(', end='')
    partition(row, col, newsize) # (0,0,4) 좌상
    partition(row, col + newsize, newsize) # (0,4,4) 우상
    partition(row + newsize, col, newsize) # (4,0,4) 좌하
    partition(row + newsize, col + newsize, newsize) # (4,4,4) 우하
    print(')',end='')

# main
N = int(input())

board = [input() for i in range(N)]

partition(0,0,N)
