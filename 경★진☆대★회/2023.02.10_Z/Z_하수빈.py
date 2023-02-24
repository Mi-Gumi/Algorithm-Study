import sys
input = sys.stdin.readline


def find(N, r, c):
    global ans
    if N == 1:
        if r == 0:
            if c == 1:
                ans += 1
        else:
            if c == 0:
                ans += 2
            else:
                ans += 3
    else:
        half = 2 ** N // 2
        if r < half:
            if c < half:
                find(N - 1, r, c)
            else:
                find(N - 1, r, c - half)
                ans += half ** 2
        else:
            if c < half:
                find(N - 1, r - half, c)
                ans += 2 * (half ** 2)
            else:
                find(N - 1, r - half, c - half)
                ans += (3 * (half ** 2))


# def fill(N, x, y):
#     global current
#     if N == 1:
#         dx = [0, 0, 1, 1]
#         dy = [0, 1, 0, 1]
#         for i in range(4):
#             ans[x + dx[i]][y + dy[i]] = current
#             current += 1
#     else:
#         fill(N - 1, x, y)
#         fill(N - 1, x, y + ((2 ** N) // 2))
#         fill(N - 1, x + ((2 ** N) // 2), y)
#         fill(N - 1, x + ((2 ** N) // 2), y + ((2 ** N) // 2))


N, r, c = map(int, input().split())
# current = 0
# ans = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]
# fill(N, 0, 0)
# print(ans[r][c])

ans = 0
find(N, r, c)
print(ans)