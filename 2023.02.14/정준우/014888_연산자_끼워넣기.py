from itertools import permutations


# 각 연산자가 수행할 작업을 정의
# 문제에서 제시한 음수를 양수로 나눌 때의 나눗셈 방법 추가
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num1 < 0:
            return -((-num1) // num2)
        else:
            return num1 // num2


num_of_nums = int(input())
nums = list(map(int, input().split()))

num_of_operator = list(map(int, input().split()))

# 각 연산자의 수만큼 해당 연산자를 리스트에 추가
operator = []
operator += list('+' * num_of_operator[0]) + list('-' * num_of_operator[1]) + list('*' * num_of_operator[2]) + list('/' * num_of_operator[3])

max_result = -1e9
min_result = 1e9

# 연산자의 개수는 (숫자의 개수 - 1)
# 연산자를 모아놓은 리스트를 연산자의 개수 길이의 순열로 만들고, 중복 제거
operators = set(permutations(operator, num_of_nums - 1))

# 각 연산자의 조합 하나씩 연산
for oper in operators:
    # 계산 끝나고 계산한 결과 초기화
    calculated = 0
    for j in range(len(oper)):
        # 첫 숫자는 쌓여온 계산 결과가 없으니 앞 숫자, 뒷 숫자, 연산자로 함수 실행
        if j == 0:
            calculated = calculate(nums[j], nums[j+1], oper[j])
        # 첫 숫자가 아니면 쌓여온 계산 결과와, 뒷 숫자, 연산자로 함수 실행
        else:
            calculated = calculate(calculated, nums[j+1], oper[j])

    # 계산값 나올 때마다 최대값, 최소값 비교해서 수정
    if max_result < calculated:
        max_result = calculated
    if min_result > calculated:
        min_result = calculated

print(max_result)
print(min_result)