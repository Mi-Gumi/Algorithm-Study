M, N = map(int, input().split(' '))

B_start = []    # B로 시작하는 체스판
W_start = []    # W로 시작하는 체스판

row1 = []  # B로시작하는 행
row2 = []  # W로 시작하는 행

for j in range(8):
    if j % 2:
        row1.append('W')
        row2.append('B')
    else:
        row1.append('B')
        row2.append('W')

for i in range(8):
    if i % 2:
        B_start.append(row2)
        W_start.append(row1)
    else:
        B_start.append(row1)
        W_start.append(row2)

chess_arr = [list(input()) for _ in range(M)]
min_cnt = 64    # 모두 틀리면 8x8

for i in range(M - 7):
    for j in range(N - 7):
        cnt1 = cnt2 = 0
        for k in range(8):
            for m in range(8): # 슬라이딩 체크
                if chess_arr[k + i][m + j] != B_start[k][m]:
                    cnt1 += 1

                if chess_arr[k + i][m + j] != W_start[k][m]:
                    cnt2 += 1
        if min_cnt > min(cnt1, cnt2):
            min_cnt = min(cnt1, cnt2)

print(min_cnt)
