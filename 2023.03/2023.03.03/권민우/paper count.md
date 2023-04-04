# [Silver II] 종이의 개수 - 1780 

[문제 링크](https://www.acmicpc.net/problem/1780) 

### 성능 요약

메모리: 69520 KB, 시간: 4496 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.</p>

<ol>
	<li>만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.</li>
	<li>(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.</li>
</ol>

<p>이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N(1 ≤ N ≤ 3<sup>7</sup>, N은 3<sup>k</sup> 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.</p>

### 출력 

 <p>첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.</p>

---
### Solution
```python
import sys
input = sys.stdin.readline

def check(x,y,size):
    paper = arr[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper != arr[i][j]:
                return False
    
    return True

def partition(x, y, size):
    global z0, o1, m1
    if check(x, y, size):
        if arr[x][y] == 0:
            z0 += 1
        elif arr[x][y] == 1:
            o1 += 1
        else:
            m1 += 1
        
        return
    
    new_size = size // 3
    partition(x, y, new_size)
    partition(x, y + new_size, new_size)
    partition(x, y + (2 * new_size), new_size)
    partition(x + new_size, y, new_size)
    partition(x + new_size, y + new_size, new_size)
    partition(x + new_size, y + (2 * new_size), new_size)
    partition(x + (2* new_size), y, new_size)
    partition(x + (2* new_size), y + new_size, new_size)
    partition(x + (2* new_size), y + (2 * new_size), new_size)

    return

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
z0 = 0
o1 = 0
m1 = 0

partition(0,0,N)
print(f'{m1}\n{z0}\n{o1}')
