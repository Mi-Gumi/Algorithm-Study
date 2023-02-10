def cutpaper(n: int, paper: list, color) -> int:
    color_cnt = 0
    for i in range(n):
        color_cnt += paper[i].count(color)

    if color_cnt == n * n:
        return 1

    m = n // 2
    if m == 1:
        return color_cnt
    p1 = paper[:m]
    p2 = paper[:m]
    p3 = paper[m:]
    p4 = paper[m:]

    for i in range(m):
        p1[i] = p1[i][:m]
        p2[i] = p2[i][m:]
        p3[i] = p3[i][:m]
        p4[i] = p4[i][m:]

    return cutpaper(m, p1, color) + cutpaper(m, p2, color) + cutpaper(m, p3, color) + cutpaper(m, p4, color)


N = int(input())

paper_arr = [list(map(int, input().split())) for _ in range(N)]

white = cutpaper(N, paper_arr, 0)
blue = cutpaper(N, paper_arr, 1)
print(white)
print(blue)
