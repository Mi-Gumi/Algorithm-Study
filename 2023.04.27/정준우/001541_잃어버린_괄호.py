from sys import stdin

# 연속된 덧셈끼리 괄호로 묶어 먼저 계산 후에 뺄셈을 수행하면 최소값
divided_by_minus = stdin.readline().split('-')

answer = 0

# - 가 처음으로 나오기 전까지의 덧셈은 모두 해줘야 함
for num in divided_by_minus[0].split('+'):
    answer += int(num)

for partial in divided_by_minus[1:]:
    for num in partial.split('+'):
        answer -= int(num)

print(answer)
