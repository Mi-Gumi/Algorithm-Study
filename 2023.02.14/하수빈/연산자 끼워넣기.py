# import sys
# import itertools
# input = sys.stdin.readline

# N = int(input())

# num = list(map(int, input().split()))
# tmp = list(map(int, input().split()))
# _list = ['+', '-', '*', '/']
# operator = []

# 각 연산자의 갯수만큼 담겨 있는 배열 생성
# for i in range(4):
#     for j in range(tmp[i]):
#         operator.append(_list[i])

# operator 요소들로 순열을 생성하여 다시 operator에 저장
# operator = list(itertools.permutations(operator, len(operator)))
# max_num = -100000000
# min_num = 100000000

# 모든 순열 요소들에 대해 계산
# for o in operater:
#     calc = num[0]
#     for i in range(len(num) - 1):
#         if o[i] == '+':
#             calc += num[i + 1]
#         elif o[i] == '-':
#             calc -= num[i + 1]
#         elif o[i] == '*':
#             calc *= num[i + 1]
#         elif o[i] == '/':
#             if calc >= 0:
#                 calc = calc // num[i + 1]
#             else:
#                 calc = -(-calc // num[i + 1])

#     if calc > max_num:
#         max_num = calc
#     if calc < min_num:
#         min_num = calc

# print(max_num) 
# print(min_num)

import sys
input = sys.stdin.readline

def calc(i, current):
    global max_num, min_num, N, num, operator
    # 마지막 숫자까지 모두 계산하면
    if N == i:
        # 최댓값, 최솟값 교체
        max_num = max(max_num, current)
        min_num = min(min_num, current)
    # 마지막 숫자가 아니라면
    else:
        # add 실행 한 후 다시 calc 실행
        if operator[0]:
            operator[0] -= 1
            calc(i + 1, current + num[i])
            operator[0] += 1
        # sub 실행 한 후 다시 calc 실행
        if operator[1]:
            operator[1] -= 1
            calc(i + 1, current - num[i])
            operator[1] += 1
        # mul 실행 한 후 다시 calc 실행
        if operator[2]:
            operator[2] -= 1
            calc(i + 1, current * num[i])
            operator[2] += 1
        # div 실행 한 후 다시 calc 실행
        if operator[3]:
            operator[3] -= 1
            if current < 0:
                tmp = -(-current // num[i])
            else:
                tmp = current // num[i]
            calc(i + 1, tmp)
            operator[3] += 1

N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -100000000
min_num = 100000000

calc(1, num[0])

print(max_num)
print(min_num)