'''
그리디 탐색으로 +, -인 경우를 각각 생각해 문제를 해결
음수와 음수사이를 전부 split하여 음수 연산을 나중에 해야 가장 최솟값을 도출 할 수 있음
-> 첫번째 수가 음수와 양수인 경우를 고려해야 올바른 결과를 도출 할 수 있음
'''

data = input().split('-')

ans = 0
# 첫번째 수 고려
first_v = list(map(int, data[0].split('+')))
if data[0][0] == '-': # 음수
    ans -= sum(first_v)
else: # 양수
    ans += sum(first_v)
# 그 후의 값을 고려
for num in data[1:]:
    num = list(map(int, num.split('+')))
    ans -= sum(num)

print(ans)







