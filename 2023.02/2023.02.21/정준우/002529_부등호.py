from itertools import permutations

def try_this(nums):
    for permutation in permutations(nums, len(nums)):

        # 모든 부등호가 성립하는지 판단하는 변수
        able = True

        # 숫자들의 순열이 부등호를 만족하는지 판단
        for i in range(num_of_inequality_sign):
            if inequality_signs[i] == '>':
                if permutation[i] < permutation[i+1]:
                    able = False
                    break

            elif inequality_signs[i] == '<':
                if permutation[i] > permutation[i+1]:
                    able = False
                    break

        # 모두 만족한다면 출력하고 반복 중단
        if able:
            print(''.join(map(str, permutation)))
            break


num_of_inequality_sign = int(input())

inequality_signs = list(map(str, input().split()))

# 오름차순 정렬된 숫자 리스트로 순열을 만들면 제일 먼저 나오는 가능한 경우가 제일 작은 경우
# 내림차순 정렬된 숫자 리스트로 순열을 만들면 제일 먼저 나오는 가능한 경우가 가장 큰 경우
nums_for_max = [num for num in range(9, 8 - num_of_inequality_sign, - 1)]
nums_for_min = [num for num in range(num_of_inequality_sign + 1)]

try_this(nums_for_max)
try_this(nums_for_min)

