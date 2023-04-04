import sys
from collections import deque
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
zero_li = deque()
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0: # 0의 위치를 리스트화
            zero_li.append((i, j))

def check_num(si, sj, num):
    if num in arr[si]: # 열 방향 탐색
        return False
    elif num in [arr[i][sj] for i in range(9)]: # 행 방향 탐색
        return False
    else:
        ci = si//3 * 3
        cj = sj//3 * 3
        for i in range(ci, ci+3): # 사각형 탐색
            for j in range(cj, cj+3):
                if arr[i][j] == num:
                    return False
    return True # 무사 통과

def search(idx):
    if idx == len(zero_li):
        for lst in arr: # 결과 도출
            print(' '.join(map(str, lst)))
        sys.exit(0)

    i, j = zero_li[idx]
    # 0의 위치에 들어갈 수 있는 1부터 9까지의 모든 경우를 시도
    for n in range(1, 10):
        if check_num(i, j, n): # 이미 행 열 사각에 그 값이 존재하는지 확인
            arr[i][j] = n
            search(idx+1) # 재귀탐색
            arr[i][j] = 0

search(0)



