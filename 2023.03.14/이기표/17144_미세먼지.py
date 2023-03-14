def find_mise(): # 미세먼지 위치 찾기
    mise_li = []
    clean = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                mise_li.append((i, j))
            if arr[i][j] == -1:
                clean.append((i,j))
    return mise_li, clean

def many_mise(mise_li):
    for i, j in mise_li:
        mid = arr[i][j] // 5
        cnt = 0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                tmp_arr[ni][nj] += mid
                cnt += 1
        arr[i][j] = arr[i][j] - (mid*cnt)

    for i in range(R):
        for j in range(C):
            arr[i][j] += tmp_arr[i][j]

def clean_mise_1(first, first_dr):
    si, sj = first[0] - 1, first[1]
    dr = 0
    while 1:
        si += first_dr[dr][0]
        sj += first_dr[dr][1]
        if 0 <= si <= first[0] and 0 <= sj < C:
            if arr[si][sj]:
                if dr == 0:
                    if (si + 1, sj) == first:
                        arr[si][sj] = 0
                    else:
                        arr[si + 1][sj] = arr[si][sj]
                        arr[si][sj] = 0
                elif dr == 1:
                    arr[si][sj - 1] = arr[si][sj]
                    arr[si][sj] = 0
                elif dr == 2:
                    arr[si - 1][sj] = arr[si][sj]
                    arr[si][sj] = 0
                elif dr == 3:
                    if arr[si][sj] == -1:
                        return
                    else:
                        arr[si][sj + 1] = arr[si][sj]
                        arr[si][sj] = 0
        else:
            si -= first_dr[dr][0]
            sj -= first_dr[dr][1]
            dr = (dr + 1) % 4

def clean_mise_2(second, second_dr):
    si, sj = second[0] + 1, second[1]
    dr = 0
    while 1:
        si += second_dr[dr][0]
        sj += second_dr[dr][1]
        if second[0] <= si < R and 0 <= sj < C:
            if arr[si][sj]:
                if dr == 0:
                    if (si - 1, sj) == second:
                        arr[si][sj] = 0
                    else:
                        arr[si - 1][sj] = arr[si][sj]
                        arr[si][sj] = 0
                elif dr == 1:
                    arr[si][sj - 1] = arr[si][sj]
                    arr[si][sj] = 0
                elif dr == 2:
                    arr[si + 1][sj] = arr[si][sj]
                    arr[si][sj] = 0
                elif dr == 3:
                    if arr[si][sj] == -1:
                        return
                    else:
                        arr[si][sj + 1] = arr[si][sj]
                        arr[si][sj] = 0
        else:
            si -= second_dr[dr][0]
            sj -= second_dr[dr][1]
            dr = (dr + 1) % 4

def sum_mise():
    sum_v = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1 or arr[i][j] == 0:
                continue
            sum_v += arr[i][j]
    return sum_v

R, C, T = map(int, input().split()) # 행 열 횟수
arr = [list(map(int, input().split())) for _ in range(R)]

for i in range(T):
    mise_li, clean = find_mise()
    first, second = clean
    tmp_arr = [[0] * C for _ in range(R)]
    many_mise(mise_li)
    first_dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    second_dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    clean_mise_1(first, first_dr)
    clean_mise_2(second, second_dr)
    print(arr)
ans = sum_mise()
print(ans)


