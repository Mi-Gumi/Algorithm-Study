from sys import stdin
from itertools import combinations


def find_cheap_and_nutritious():

    min_cost = 1e9

    best_choice = None

    # 1개 ~ 전체 재료를 선택할 때까지의 모든 경우에서
    for num_of_picked_ingredients in range(1, num_of_ingredients + 1):
        # 재료의 조합을 구한 후
        for combination in combinations(range(1, num_of_ingredients + 1), num_of_picked_ingredients):

            # 조합된 재료들의 영양소와 가격을 더해서 영양소 조건을 만족한다면 최소 가격인지 판단
            protein = fat = carbs = vitamin = cost = 0

            for ingredient in combination:

                # 배열은 인덱스 0부터 시작하므로 조합에서 나온 재료 번호에 -1 해서 사용
                protein += ingredients_info[ingredient - 1][0]
                fat += ingredients_info[ingredient - 1][1]
                carbs += ingredients_info[ingredient - 1][2]
                vitamin += ingredients_info[ingredient - 1][3]
                cost += ingredients_info[ingredient - 1][4]

            if protein >= protein_required and fat >= fat_required and carbs >= carbs_required and vitamin >= vitamin_required:
                if min_cost > cost:
                    min_cost = cost
                    best_choice = combination

                # 가격이 같다면 조건에 따라 사전 순으로 정렬 후 제일 앞 요소 선택
                elif min_cost == cost:
                    best_choice = sorted((best_choice, combination))[0]

    if min_cost == 1e9:
        print(-1)

    else:
        print(min_cost)
        print(*best_choice)


num_of_ingredients = int(stdin.readline())

protein_required, fat_required, carbs_required, vitamin_required = map(int, stdin.readline().split())

ingredients_info = [list(map(int, stdin.readline().split())) for _ in range(num_of_ingredients)]

find_cheap_and_nutritious()
