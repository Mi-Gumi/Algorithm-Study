def cutpaper(n: int, paper: list, color) -> int:  # 형식 명시 , 범용성을 위해 color값을 받음
    color_cnt = 0
    for i in range(n):
        color_cnt += paper[i].count(color)  # color 값을 카운트

    if color_cnt == n * n:  # 정사각형이 전부 다 같은 색이므로 1개 리턴
        return 1

    m = n // 2              # 잘랐을 때의 한변의 길이
    if m == 1:              # 최소 크기일 때
        return color_cnt    # 하나 하나가 한개
    p1 = paper[:m]          # 가로로 자른 종이의 윗부분
    p2 = paper[:m]
    p3 = paper[m:]          # 가로로 자른 종이의 아랫부분
    p4 = paper[m:]

    for i in range(m):
        p1[i] = p1[i][:m]   # 세로로 자른 종이의 왼쪽부분
        p2[i] = p2[i][m:]   # 세로로 자른 종이의 오른쪽부분
        p3[i] = p3[i][:m]
        p4[i] = p4[i][m:]
    # 4부분으로 나누어 재귀함수 호출 후 취합
    return cutpaper(m, p1, color) + cutpaper(m, p2, color) + cutpaper(m, p3, color) + cutpaper(m, p4, color)


N = int(input())
# 색종이 정보를 이중배열로 저장
paper_arr = [list(map(int, input().split())) for _ in range(N)]
# 함수 호출
white = cutpaper(N, paper_arr, 0)
blue = cutpaper(N, paper_arr, 1)
print(white)
print(blue)
