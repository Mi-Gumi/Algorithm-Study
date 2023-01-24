'''
# 오래 걸리는 코드
import sys
num1, num2 = map(int, sys.stdin.readline().split())

# num1, num2 각 약수를 모은 리스트의 교집합 중 마지막 요소가 최대공약수
num1_divisor = []
num2_divisor = []

for div_1 in range(1, num1 + 1):
    if num1 % div_1 == 0:
        num1_divisor.append(div_1)

for div_2 in range(1, num2 + 1):
    if num2 % div_2 == 0:
        num2_divisor.append(div_2)

div_set1, div_set2 = set(num1_divisor), set(num2_divisor)
divisor = set(num1_divisor) & set(num2_divisor)
print(list(divisor)[-1])

multiple = (num1 * num2) // (list(divisor)[-1])
print(multiple)
'''

# 유클리드 호제법
# a와 b의 최대공약수는 b를 (a % b)로 나눈 후,
# a 자리에 b, b 자리에 (a % b)를 넣는것을 반복해, b가 0이 될 때의 a 값
# a와 b의 최소공배수는 a * b를 a와 b의 최대공약수로 나눈 몫

num1, num2 = map(int, input().split())

div_num1, div_num2 = num1, num2

while div_num2 != 0:
    div_num1 = div_num1 % div_num2
    div_num1, div_num2 = div_num2, div_num1

multiple = (num1 * num2) // div_num1

print(div_num1)
print(multiple)

'''
# 그냥 함수
import math

num1, num2 = map(int, input().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))
'''