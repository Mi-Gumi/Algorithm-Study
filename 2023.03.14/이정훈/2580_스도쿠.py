def solve_sudoku(board):

    # 스도쿠 보드 상의 빈칸을 찾음
    row, col = find_empty_cell(board)
    # 모든 빈칸이 채워졌다면 리턴
    if row is None:
        return board
    
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            
            board[row][col] = num

            if solve_sudoku(board):
                return board
            # 스도쿠 보드가 해답이 아닌 경우 다시 빈칸으로 만들고 다른 수를 대입해봄
            board[row][col] = 0
            
    # 스도쿠 보드를 해결할 수 없는 경우
    return None

def find_empty_cell(board):
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    # 빈칸이 없는 경우
    return None, None

def is_valid_move(board, row, col, num):
    
    # 주어진 숫자(num)가 스도쿠 보드 상의 해당 칸(row, col)에 유효한 수인지 확인하는 함수
    
    # 해당 숫자가 행과 열에 이미 존재하는지 확인
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # 해당 숫자가 속한 3x3 서브그리드에 이미 존재하는지 확인
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row+i][subgrid_col+j] == num:
                return False
    return True

sudoku = [list(map(int,input().split())) for _ in range(9)]

ans = solve_sudoku(sudoku)
for i in range(9) :
    print(*ans[i])