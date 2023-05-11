# from itertools import combinations
# from sys import stdin
#
#
# while True:
#
#     number_info = list(map(int, stdin.readline().split()))
#
#     if len(number_info) == 1:
#         break
#
#     num = number_info[0]
#     numbers = number_info[1:]
#
#     for combination in combinations(numbers, 6):
#         print(*combination)
#
#     print()





from sys import stdin


def pick(picked, idx):

    if picked == 6:
        print(*combinations)
        return

    for i in range(idx, num):
        combinations.append(numbers[i])
        pick(picked + 1, i + 1)
        combinations.pop()


while True:
    number_info = list(map(int, stdin.readline().split()))

    if len(number_info) == 1:
        break

    num = number_info[0]
    numbers = number_info[1:]

    combinations = []

    pick(0, 0)

    print()
