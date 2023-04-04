def cut_paper(arr, x, y, n): # 분할 정복
    global zero, one, minu
    zero_cnt = one_cnt = minu_cnt = 0 # 카운트 변수
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] == 0: # 0인 경우 카운트
                zero_cnt += 1
            elif arr[i][j] == 1: # 1인 경우 카운트
                one_cnt += 1
            else: # -1인 경우 카운트
                minu_cnt += 1
    # 각각의 카운트가 조건에 만족
    if zero_cnt == n**2:
        zero += 1
    elif one_cnt == n**2:
        one += 1
    elif minu_cnt == n**2:
        minu += 1
    else: # 9등분을 진행
        cut_paper(arr, x, y, n//3)
        cut_paper(arr, x, y + n // 3, n // 3)
        cut_paper(arr, x, y + 2 * (n // 3), n // 3)
        cut_paper(arr, x + n // 3, y, n // 3)
        cut_paper(arr, x + n // 3, y + n // 3, n // 3)
        cut_paper(arr, x + n // 3, y + 2*(n // 3), n // 3)
        cut_paper(arr, x + 2*(n // 3), y, n // 3)
        cut_paper(arr, x + 2*(n // 3), y + n // 3, n // 3)
        cut_paper(arr, x + 2*(n // 3), y + 2 * (n // 3), n // 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

zero = one = minu = 0

cut_paper(arr, 0, 0, N)
print(minu)
print(zero)
print(one)