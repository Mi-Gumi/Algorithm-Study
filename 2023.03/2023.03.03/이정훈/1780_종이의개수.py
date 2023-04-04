import sys

input = sys.stdin.readline


def cut(arr, n):
    color = arr[0][0]     # 모두 같은 색인지 알아보기 위해 첫번째 색상을 기준으로 잡음
    cnt = 1              #  color 가 같은 종이 cnt
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:   # 첫번째는 패스
                continue
            if arr[i][j] == color:  # 같은 색 cnt
                cnt += 1
    if cnt == n ** 2:               # n*n 개면 모두 같은 색
        paper_cnt[color + 1] += 1
        return
    nn = n // 3             # 다음 종이의 한변 길이
    arr_up = arr[:nn]       # 상단부 1/3
    arr_mid = arr[nn:2 * nn]# 중단부 1/3
    arr_down = arr[2 * nn:] # 하단부 1/3

    for cut_arr in (arr_up, arr_mid, arr_down):  # 1/3 로 나눈 종이를 다시 세로로 나누어서 cut 호출
        cut(list(map(lambda x: x[:nn], cut_arr)), nn)
        cut(list(map(lambda x: x[nn:2 * nn], cut_arr)), nn)
        cut(list(map(lambda x: x[2 * nn:], cut_arr)), nn)
    return


N = int(input())

paper = [list(map(int, input().strip().split())) for _ in range(N)]
paper_cnt = [0, 0, 0]
# 재귀 함수호출
cut(paper, N)
print(*paper_cnt, sep='\n')
