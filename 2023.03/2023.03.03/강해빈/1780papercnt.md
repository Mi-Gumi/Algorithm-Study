# [Silver II] 종이의 개수 - 1780 

[문제 링크](https://www.acmicpc.net/problem/1780) 

### 성능 요약

메모리: 69484 KB, 시간: 4716 ms

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
```python
m_cnt, z_cnt, p_cnt = 0, 0, 0

def check(x, y, N): # 종이가 모두 같은 수로 되어 있는지 확인
    first = paper[x][y] # 첫 값이랑 비교

    for i in range(x, x + N): # x부터 x+N까지 순회
        for j in range(y, y + N):
            if paper[i][j] != first: # 같지 않으면
                return False # 거짓 반환
    return True # 다 같으면 참 반환

def scissors(x, y, N): # 같은 크기의 종이 9개로 자르고, 확인 과정 반복
    global m_cnt, z_cnt, p_cnt
    if check(x, y, N): # 모두 같은 수로 되어있으면 개수 카운트
        if paper[x][y] == -1:
            m_cnt += 1
        if paper[x][y] == 0:
            z_cnt += 1
        if paper[x][y] == 1:
            p_cnt += 1
        return # 함수 끝내줌
    # 아니면 같은 크기의 9개로 자르기
    new_N = N // 3
    scissors(x, y, new_N)
    scissors(x, y + new_N, new_N)
    scissors(x, y + new_N * 2, new_N)
    scissors(x + new_N, y, new_N)
    scissors(x + new_N, y + new_N, new_N)
    scissors(x + new_N, y + new_N * 2, new_N)
    scissors(x + new_N * 2, y, new_N)
    scissors(x + new_N * 2, y + new_N, new_N)
    scissors(x + new_N * 2, y + new_N * 2, new_N)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
scissors(0, 0, N)
print(m_cnt)
print(z_cnt)
print(p_cnt)
```

```python
# 시도
def scissors(N, paper):
    global m_cnt, z_cnt, p_cnt
    for a in range(0, N, N // 3):
        for b in range(0, N, N // 3):
            same = []
            for c in range(a, a + N // 3):
                for d in range(b, b + N // 3):
                    same.append(paper[c][d])
            if check(same):
                if same[0] == -1:
                    m_cnt += 1
                if same[0] == 0:
                    z_cnt += 1
                if same[0] == 1:
                    p_cnt += 1
            else:
                N = N // 3
                scissors(N, same)

    return m_cnt, z_cnt, p_cnt
```
