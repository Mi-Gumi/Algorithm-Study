# [Gold IV] 알파벳 - 1987 

[문제 링크](https://www.acmicpc.net/problem/1987) 

### 성능 요약

메모리: 153152 KB, 시간: 7772 ms

### 분류

그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹

### 문제 설명

<p>세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.</p>

<p>말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.</p>

<p>좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.</p>

### 입력 

 <p>첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.</p>

### 출력 

 <p>첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.</p>

---

### Solution
```python
import sys
from collections import deque

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 실패하면 회귀해서 해야하기 때문에 dfs로
def dfs(r, c, llst):
    global max_
    # 안넣었으면 넣어주기
    if lst[r][c] not in llst:
        llst.add(lst[r][c])
    # 탐색
    for dr, dc in d:
        nr = r + dr
        nc = c + dc
        
        # arr 안이고 안쓴거면
        if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] not in llst:
            # 추가해주기 근데 시작하면서 추가해서 이거 없어도 될듯...?
            llst.add(lst[nr][nc])
            # 가장 큰 값으로
            max_ = max(max_, len(llst))
            dfs(nr, nc, llst)
            # 더 못가면 돌아와서 넣었던거 지우고 다음 내용으로
            llst.remove(lst[nr][nc])

R, C = map(int, input().split())
lst = [list(input().strip()) for _ in range(R)]
max_ = 1
llst = set()
dfs(0, 0, llst)
print(max_)
