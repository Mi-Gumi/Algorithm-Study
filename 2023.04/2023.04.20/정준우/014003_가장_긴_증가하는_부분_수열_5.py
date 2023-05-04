from sys import stdin
from bisect import bisect_left


num_of_numbers = int(stdin.readline())

sequence = list(map(int, stdin.readline().split()))

nlogn_LIS = []
with_index = []

for number in sequence:

    # 들어가있는 어느 숫자들보다 현재 숫자가 크면 그냥 뒤에 넣어주기
    if not nlogn_LIS or nlogn_LIS[-1] < number:
        nlogn_LIS.append(number)
        with_index.append((len(nlogn_LIS) - 1, number))

    # 더 작은 숫자가 들어왔다면, bisect를 통해 들어갈 수 있는 위치에 갱신
    # 숫자가 더 작으면 더 긴 LIS를 생성할 수도 있음
    else:
        nlogn_LIS[bisect_left(nlogn_LIS, number)] = number
        with_index.append((bisect_left(nlogn_LIS, number), number))

LIS = []

LIS_last_index = len(nlogn_LIS) - 1

# 인덱스가 같을 경우 가장 늦게 들어간 숫자가 알맞은 LIS
# 그래서 뒤에서부터 탐색
for index in range(len(with_index) - 1, -1, -1):

    if with_index[index][0] == LIS_last_index:
        LIS.append(with_index[index][1])
        LIS_last_index -= 1

print(len(LIS))
# 뒤에서부터 들어갔으니 뒤집어줘야 제대로 된 LIS
print(*reversed(LIS))
