def find_mise(): # 미세먼지 위치 찾기
    mise_li = []
    clean = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0: # 미세먼지
                mise_li.append((i, j))
            if arr[i][j] == -1: # 청소기
                clean.append((i,j))
    return mise_li, clean

def many_mise(mise_li): # 미세먼지 확장
    for i, j in mise_li:
        mid = arr[i][j] // 5
        cnt = 0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)): # 네 방향 탐색
            ni = i + di
            nj = j + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                tmp_arr[ni][nj] += mid
                cnt += 1
        arr[i][j] = arr[i][j] - (mid*cnt)

    for i in range(R): # 동시값 합치기
        for j in range(C):
            arr[i][j] += tmp_arr[i][j]

def clean_mise(i, j, dr):
    before =  dir = 0
    si, sj = i, j
    i += dr[0][0]
    j += dr[0][1]
    while i != si or j != sj:
        after = arr[i][j] # 다음값
        arr[i][j] = before # 이전값
        before = after # 위치 변경
        i += dr[dir][0]
        j += dr[dir][1]
        if not (0 <= i < R and 0 <= j < C): # 범위를 벗어나고
            if dir == 3: # 마지막 방향으면 종료
                return
            i = i - dr[dir][0] + dr[dir+1][0]
            j = j - dr[dir][1] + dr[dir+1][1]
            dir += 1

def sum_mise(): # 최종 먼지 개수 구하기
    sum_v = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1 or arr[i][j] == 0:
                continue
            sum_v += arr[i][j]
    return sum_v

R, C, T = map(int, input().split()) # 행 열 횟수
arr = [list(map(int, input().split())) for _ in range(R)]

for _ in range(T):
    mise_li, clean = find_mise()
    first, second = clean
    tmp_arr = [[0] * C for _ in range(R)]
    many_mise(mise_li)
    first_dr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    second_dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    clean_mise(first[0], first[1], first_dr)
    clean_mise(second[0], second[1], second_dr)
ans = sum_mise()
print(ans)



