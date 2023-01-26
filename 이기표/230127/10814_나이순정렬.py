T = int(input())
ans = []
for t in range(T):
    age, name = input().split()
    age = int(age)
    ans.append([age, name]) # 나이 이름 리스트 형태로 추가

ans.sort(key = lambda x: x[0]) # 나이순으로 정렬 진행
for a in ans:
    print(a[0], a[1]) # 나이 이름