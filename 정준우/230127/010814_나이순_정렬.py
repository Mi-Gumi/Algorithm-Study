'''
# lambda 사용하지 않고 시도 - runtine error (TypeError)
N = int(input())

member = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member.append([age, name])

def sorting(x):
    return x[0]

member.sort(key = sorting(member))

for i in range(N):
    print(member[i])
'''

# lambda 사용하지 않고 시도 - runtine error (TypeError)
N = int(input())

member = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member.append([age, name])

# sort()에서 key를 통해 일부 요소만 기준으로 잡고 정렬 가능
# 공식문서에서는 key는 함수의 형태라고 했으나,
# lambda x 형태가 아니면 제대로 작동되지 않음

# def 로 정의하는 함수는 아니고, 내장 함수는 되는 것으로 보임 (Ex. key = len)
# key가 여러 개일 때는 튜플 형식으로 지정 (key = lambda x: (x1, x2))
# 내림차순으로 하고 싶다면, - 이용 (key = lambda x: -x[0])
member.sort(key = lambda x: x[0])

for i in range(N):
    print(*member[i])