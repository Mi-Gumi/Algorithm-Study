import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

# 체스판은 두 종류 뿐이므로 샘플 준비
sample1 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
sample2 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
# 가장 많이 바꾼 횟수는 64회 이므로 최댓값으로 설정
min_count = 64

# 배열 범위 밖으로 나가지 않도록 -7
for i in range(N - 7):
    for j in range(M - 7):
        # sample1, sample2와 비교하여 갯수를 담을 변수 선언
        count_1 = 0
        count_2 = 0

        # 기존 보드를 8x8크기로 분해
        new_board = []
        for k in range(8):
            new_board.append(board[i + k][j:j + 8])

        # 새로 만든 보드와 sample1, sample2 비교 및 바꿔야 하는 갯수 탐색
        for a in range(8):
            for b in range(8):
                if new_board[a][b] != sample1[a][b]:
                    count_1 += 1
                if new_board[a][b] != sample2[a][b]:
                    count_2 += 1
        
        # 기존 최솟값과 count_1, count_2 비교
        min_count = min(min_count, count_1, count_2)

print(min_count)