from itertools import permutations

num = input()

# 주어진 숫자로 만들 수 있는 숫자의 순열 각 요소에 join을 사용해 이어진 문자열로 만들고
# 중복된 숫자를 없앤 후 오름차순으로 정렬
# set 형태라 sort는 불가능해 sorted 사용
able_nums = sorted(set(map(lambda x: ''.join(x), permutations(num, len(num)))))

# 주어진 숫자가 가장 큰 숫자라면 0 출력
if num == able_nums[-1]:
    print(0)

# 오름차순으로 정렬했으니 주어진 숫자 다음이 큰 수 중 가장 작은 수
else:
    answer_index = able_nums.index(num) + 1
    print(f'{able_nums[answer_index]}')

