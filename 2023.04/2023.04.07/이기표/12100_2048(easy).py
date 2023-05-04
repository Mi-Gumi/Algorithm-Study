import copy
def move(check, board):
    if check == 1:
        for j in range(N):
            cur = 0 # 현재 인덱스
            for i in range(N):
                if board[i][j]: # 0이 아닌 경우
                    # 다음 위치로 옮길 값 저장
                    tmp = board[i][j]
                    # 현재 위치 0 할당
                    board[i][j] = 0
                    
                    if board[cur][j] == 0: # 현재 인덱스가 0이면 저장값 할당
                        board[cur][j] = tmp
                    elif board[cur][j] == tmp: # 저장값과 동일하면 합치기
                        board[cur][j] *= 2
                        cur += 1 # 합친 후 인덱스 증가
                    else: # 저장값과 다른 경우
                        cur += 1 # 인덱스를 증가시킨 후 이동
                        board[cur][j] = tmp

    elif check == 2:
        for j in range(N):
            cur = N-1
            for i in range(N - 1, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[cur][j] == 0:
                        board[cur][j] = tmp
                    elif board[cur][j] == tmp:
                        board[cur][j] *= 2
                        cur -= 1
                    else:
                        cur -= 1
                        board[cur][j] = tmp
    elif check == 3:
        for i in range(N):
            cur = 0
            for j in range(N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][cur] == 0:
                        board[i][cur] = tmp
                    elif board[i][cur] == tmp:
                        board[i][cur] *= 2
                        cur += 1
                    else:
                        cur += 1
                        board[i][cur] = tmp
    elif check == 4:
        for i in range(N):
            cur = N-1
            for j in range(N - 1, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][cur] == 0:
                        board[i][cur] = tmp
                    elif board[i][cur] == tmp:
                        board[i][cur] *= 2
                        cur -= 1
                    else:
                        cur -= 1
                        board[i][cur] = tmp
    return board

def dfs(n, board):
    global ans
    if n == 5: # 5번 진행한 경우의 최대값 도출
        for lst in board:
            ans = max(ans, max(lst))
        return
    # 1 상 2 하 3 좌 4 우
    for i in range(1, 5):
        # 깊은 복사를 통해 배열 중복 방지
        in_board = copy.deepcopy(board)
        dfs(n + 1, move(i, in_board))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, arr)
print(ans)