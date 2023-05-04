# [Gold I] 구간 합 구하기 - 2042 

[문제 링크](https://www.acmicpc.net/problem/2042) 

### 성능 요약

메모리: 215908 KB, 시간: 832 ms

### 분류

세그먼트 트리, 자료 구조

### 문제 설명

<p>어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.</p>

<p>입력으로 주어지는 모든 수는 -2<sup>63</sup>보다 크거나 같고, 2<sup>63</sup>-1보다 작거나 같은 정수이다.</p>

### 출력 

 <p>첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -2<sup>63</sup>보다 크거나 같고, 2<sup>63</sup>-1보다 작거나 같은 정수이다.</p>

---

### Solution
```python
import sys
input = sys.stdin.readline

# 트리 만들기
def tree(start, end, idx):
    # start와 end가 같으면 리프노드
    if start == end:
        segment_tree[idx] = num_lst[start-1]
        return segment_tree[idx]
    
    # 총 start ~ end*2까지 나옴.
    mid = (start+end) // 2
    segment_tree[idx] = tree(start, mid, idx*2) + tree(mid+1, end, idx*2+1)
    return segment_tree[idx]

# 트리에서 값 찾기
def search(start, end, idx, left, right):
    # 찾는 법위가 start ~ end 밖이라면 0 반환
    if start > right or end < left:
        return 0
    
    # 찾는 범위가 트리 내에 있다면 !! 매우 중요
    if start >= left and end <= right:
        return segment_tree[idx]
    
    # 트리에서 범위 값을 맞추기 위해 조정
    mid = (start + end) // 2
    tmp_sum = search(start, mid, idx*2, left, right) + search(mid+1, end, idx*2+1, left, right)
    return tmp_sum

# 트리에서 값 변경하기 (구간 값도 모두 변경해야함)
def update(start, end, idx, update_idx, update_num):
    # update 하려는 범위가 초과될 경우
    if start > update_idx or end < update_idx:
        return
    
    segment_tree[idx] += update_num

    # 같으면 분할 불가
    if start == end:
        return
    
    mid = (start + end) // 2
    update(start, mid, idx*2, update_idx, update_num)
    update(mid+1, end, idx*2+1, update_idx, update_num)


N,M,K = map(int, input().split())

num_lst = []
# 가장 가까우면서 N보다 큰 제곱수의 *2를 해야하지만 보통 N*4로 함.
segment_tree = [0] *(N*4)

for _ in range(N):
    num_lst.append(int(input()))

tree(1, N, 1)

for _ in range(M+K):
    # a가 1이면 변경, 2면 구간합 구하기
    a, b, c = map(int, input().split())
    if a == 1:
        # 바꾸는 값 - 원래 값을 미리 구하여 넣어준다.
        # update시 값 오류를 막기 위함
        tmp = c - num_lst[b-1]
        num_lst[b-1] = c
        update(1, N, 1, b, tmp)
    
    else:
        print(search(1,N,1,b,c))
