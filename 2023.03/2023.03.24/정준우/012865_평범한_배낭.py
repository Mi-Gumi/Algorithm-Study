# knapsack 알고리즘
# dp[i][j] = max(dp[i-1][j], dp[i][j - stuff_weight] + stuff_value)

import sys


num_of_stuff, me_fill = map(int, sys.stdin.readline().split())

stuff_info = []

for _ in range(num_of_stuff):
    stuff, value = map(int, sys.stdin.readline().split())
    stuff_info.append((stuff, value))

knapsack_table = [[0] * (me_fill + 1) for _ in range(num_of_stuff + 1)]

for stuff_weight in range(1, num_of_stuff + 1):
    for limit_weight in range(1, me_fill + 1):

        # 무게 제한 때문에 아직 새 물건을 넣어볼 수 없다면 이전 값 그대로 가져오기
        if limit_weight < stuff_info[stuff_weight - 1][0]:
            knapsack_table[stuff_weight][limit_weight] = knapsack_table[stuff_weight - 1][limit_weight]

        # 새 물건을 넣어서 한계까지 무게를 채웠을 때와 넣지 않은 이전 값을 비교해 더 높은 가치 선택
        else:
            knapsack_table[stuff_weight][limit_weight] = \
            max(knapsack_table[stuff_weight - 1][limit_weight], knapsack_table[stuff_weight - 1][limit_weight - (stuff_info[stuff_weight - 1][0])] + stuff_info[stuff_weight - 1][1])

# 모든 경우를 살펴본 후인 우측 하단 값 출력
print(knapsack_table[-1][-1])
