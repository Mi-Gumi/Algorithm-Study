import sys


def check(N, idx):
    global count

    # 마지막 열 까지 모든 퀸을 놓았다면
    if idx == N:
        # count + 1
        count += 1
        return

    # 첫번째 열 부터 마지막 열 까지
    for i in range(N):
        
        # 같은 행에 퀸이 놓여져 있다면 확인 x
        if visited[i]:
            continue
        
        # idx번째 행 i번째 열에 퀸 표시
        board[idx] = i
        for j in range(idx):
            # idx - j 와 abs(board[idx] - board[j]) 가 같다면 대각선 상에 위치해 있음으로 break
            if idx - j == abs(board[idx] - board[j]):
                break
            # 퀸을 놓을 수 있다면
        else:
            # 방문 체크
            visited[i] = 1
            # 다음 열 체크
            check(N, idx + 1)
            # 방문 해제
            visited[i] = 0
    return


N = int(sys.stdin.readline())
board = [0] * N
visited = [0] * N
count = 0

check(N, 0)

print(count)