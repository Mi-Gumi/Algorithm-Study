import sys
from collections import deque
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
zero_li = deque()
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_li.append((i, j))

def check_num(si, sj, num):
    if num in arr[si]: # 열 방향 탐색
        return False
    elif num in [arr[i][sj] for i in range(9)]: # 행 방향 탐색
        return False
    else:
        ci = si//3 * 3
        cj = sj//3 * 3
        for i in range(ci, ci+3):
            for j in range(cj, cj+3):
                if arr[i][j] == num:
                    return False
    return True # 무사 통과

def search(idx):
    if idx == len(zero_li):
        for lst in arr:
            print(' '.join(map(str, lst)))
        sys.exit(0)

    i, j = zero_li[idx]
    for n in range(1, 10):
        if check_num(i, j, n):
            arr[i][j] = n
            search(idx+1)
            arr[i][j] = 0

search(0)



