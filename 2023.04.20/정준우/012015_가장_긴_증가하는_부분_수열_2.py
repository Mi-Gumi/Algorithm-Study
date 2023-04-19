from sys import stdin
from bisect import bisect_left


num_of_numbers = int(stdin.readline())

sequence = list(map(int, stdin.readline().split()))

LIS = []

for number in sequence:

    # 들어가있는 어느 숫자들보다 현재 숫자가 크면 그냥 뒤에 넣어주기
    if not LIS or LIS[-1] < number:
        LIS.append(number)

    # 더 작은 숫자가 들어왔다면, bisect를 통해 들어갈 수 있는 위치에 갱신
    # 숫자가 더 작으면 더 긴 LIS를 생성할 수도 있음
    else:
        LIS[bisect_left(LIS, number)] = number

print(len(LIS))
