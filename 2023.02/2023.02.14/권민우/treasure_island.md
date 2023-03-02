```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 보드판 만들기
board = [list(input()) for _ in range(N)]

# 계속 초기화 해줘야 할듯
visited = [[False]*M for _ in range(N)]

# L(육지)에서만 시작하기
for i in range(N): 
    for j in range(M):
        if board[i][j] == 'W':
            pass
        
# 상 하 좌 우
row = [1,-1,0,0]
col = [0,0,-1,1]
cnt = 0

못했음 
