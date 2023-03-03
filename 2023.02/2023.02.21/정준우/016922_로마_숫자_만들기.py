# 주어진 리스트의 요소들로 길이 r 인 중복 조합을 만들어주는 함수
# combinations_with_replacement(iterable, r)
from itertools import combinations_with_replacement

num_of_usable = int(input())

usables = [1, 5, 10, 50]

nums_made = []

# 주어진 수만큼만 이용해서 만들 수 있는 숫자 조합의 리스트
combinations = list(combinations_with_replacement(usables, num_of_usable))


for combination in combinations:
    nums_made += [sum(combination)]

# 중복된 숫자를 제외한 후 만들어진 숫자가 몇 개나 있는지 확인
answer = len(set(nums_made))

print(answer)