N = int(input())

# 숫자를 다룰 stack 리스트와 연산자를 담을 ans 리스트 생성
stack = []
ans = []

# 수열을 만들 수 없을 경우 사용하게 될 변수 지정
able = 'able'

# 다음 push 할 숫자를 의미하는 next_num을 1로 지정
next_num = 1

for i in range(N):
    num = int(input())

    # push 해야 할 숫자가 목표 숫자와 같아지기 전까지
    # stack 리스트에 push, ans 리스트에 'push 했음'을 의미하는 + 추가
    # 다음 숫자를 고려하기 위해 next_num에 1 더해준 후 반복
    while next_num <= num:
        ans.append('+')
        stack.append(next_num)
        next_num += 1


    # stack의 마지막 숫자가 목표한 숫자와 같아지면,
    # pop을 해주며 ans 리스트에 'pop 했음'을 의미하는 - 추가
    if stack[-1] == num:
        ans.append('-')
        stack.pop()
    # 위 조건이 성립되지 않아 수열을 만들 수 없다고 판단되면,
    # able을 'unable' 로 지정하고 반복 중단
    else:
        able = 'unable'
        break

# 조건이 성립되지 않아 able이 unable이 되면 NO 출력
if able == 'unable':
    print('NO')
# 조건이 성립되어 수열이 만들어졌다면, ans 리스트 출력
else:
    for j in ans:
        print(j)