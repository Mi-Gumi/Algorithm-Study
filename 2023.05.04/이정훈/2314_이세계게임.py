from collections import deque
# import sys
# 배열을 문자열로 '1011011010111111'
def arr2bit(arr) :
    bit = ''
    for i in range(4):
        for j in range(4) :
            bit += arr[i][j]
    return bit

# 문자열을 4*4 배열로
def bit2arr(bit) :
    arr = []
    for i in range(4):
        arr.append(list(bit[i*4:(i+1)*4]))
    return arr

inputs = []
while len(inputs) < 8 :
    tmp = input()
    if not tmp :
        continue
    inputs.append(list(tmp.strip()))

current_board = inputs[:4]
target_board = inputs[4:]

trans = {
    'L' : '0',
    'P' : '1'
}
for i in range(4) :
    for j in range(4) :
        current_board[i][j] = trans[current_board[i][j]]
        target_board[i][j] = trans[target_board[i][j]]

targetbit = arr2bit(target_board)  #목표값
startbit = arr2bit(current_board)  #시작값

Q = deque()
Q.append(startbit)

# 방문처리 dictionary로
visited = dict()
visited[startbit] = 0  # count로 활용
while Q :
    bit = Q.popleft()
    board = bit2arr(bit)
    # check 
    if bit == targetbit :
        ans = visited[bit]
        break
    # 수평교환
    for i in range(4) :
        for j in range(3) :
            if board[i][j] != board[i][j+1]:
                board[i][j] , board[i][j+1] = board[i][j+1] , board[i][j]
                # 문자열로
                newbit = arr2bit(board)
                if not visited.get(newbit) :
                    visited[newbit] = visited[bit] + 1
                    Q.append(newbit)
                board[i][j] , board[i][j+1] = board[i][j+1] , board[i][j]

    # 수직교환
    for i in range(3) :
        for j in range(4) :
            if board[i][j] != board[i+1][j]:
                board[i][j] , board[i+1][j] = board[i+1][j] , board[i][j]
                # 문자열로
                newbit = arr2bit(board)
                if not visited.get(newbit) :
                    visited[newbit] = visited[bit] + 1
                    Q.append(newbit)
                board[i][j] , board[i+1][j] = board[i+1][j] , board[i][j]

# 출력
print(ans)