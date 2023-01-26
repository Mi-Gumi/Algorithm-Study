N = int(input())

member = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member.append([age, name])

# sort()에서 key를 통해 일부 요소만 기준으로 잡고 정렬 가능
# key가 여러 개일 때는 튜플 형식으로 지정 (key = lambda x: (x1, x2))
# 내림차순으로 하고 싶다면, - 이용 (key = lambda x: -x[0])
member.sort(key = lambda x: x[0])

for i in range(N):
    print(*member[i])