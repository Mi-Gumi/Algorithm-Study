import sys


def why_do_this():
    if col_size % 2 == 1:
        return 0

    cha_gok_cha_gok = [0] * 31

    cha_gok_cha_gok[0] = 1
    cha_gok_cha_gok[2] = 3

    for i in range(4, col_size + 1):
        cha_gok_cha_gok[i] = cha_gok_cha_gok[i - 2] * 3
        for j in range(4, col_size + 1, 2):
            cha_gok_cha_gok[i] += cha_gok_cha_gok[i - j] * 2

    return cha_gok_cha_gok[col_size]


col_size = int(sys.stdin.readline())

print(why_do_this())
