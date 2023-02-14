from itertools import permutations

N = int(input())

numbers = input().split()
operator = list(map(int, input().split()))
_max = -1000000000
_min = 1000000000

op = ['+', '-', '*', '//']
op_list = []
for i in range(4):
    op_list.extend([op[i] for _ in range(operator[i])])  # 개수 만큼 리스트에 추가

op.clear()
op = permutations(op_list, N - 1)   # 순열 구하기
op = list(set(op))                  # 중복 제거

M = len(op)     # 순열의 개수

for i in range(M):
    formula = numbers[0]        #계산식, str형식이고 처음엔 첫 숫자가 들어감
    for j in range(1, N):
        if int(formula) < 0 and op[i][j - 1] == '//' and int(numbers[j]) > 0: #음수를 양수로 나눌 때
            formula = str(-1 * int(formula))
            formula += op[i][j - 1]
            formula += numbers[j]
            formula = str(-1 * eval(formula))
        else:
            formula += op[i][j - 1]     # 연산자 추가
            formula += numbers[j]       # 연산자 뒤에 숫자 붙이기
            formula = str(eval(formula))    #eval 함수로 계산하고 다시 str
    rst = int(formula)
    if rst > _max:
        _max = rst
    if rst < _min:
        _min = rst

print(_max)
print(_min)
