import sys
input = sys.stdin.readline

# 열과 행 체크
def check_rc(r, c, n):
    for i in range(9):
        if sudoku[i][c] == n or sudoku[r][i] == n:
            return 0
    return 1

# 사각형 체크
def check_s(r, c, n):
    nr, nc = r // 3 * 3, c // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nr + i][nc + j] == n:
                return 0
    return 1


def check(idx):
    # 0을 전부 채웠다면 출력
    if idx == len(list_0):
        for l in sudoku:
            print(*l)
        sys.exit()

    r, c = list_0[idx][0], list_0[idx][1]
    for i in range(1, 10):
        # 1부터 9까지 넣을 수 있는 수가 있다면
        if check_rc(r, c, i) and check_s(r, c, i):
            # 넣어보고 다시 check
            sudoku[r][c] = i
            check(idx + 1)
            sudoku[r][c] = 0
        
list_0 = []
sudoku = []
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if not tmp[j]:
            list_0.append([i, j])
    sudoku.append(tmp)

check(0)
