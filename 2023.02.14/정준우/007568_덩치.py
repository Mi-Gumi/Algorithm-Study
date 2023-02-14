num_of_students = int(input())

# 학생들의 몸무게, 키를 담을 리스트
students_info = []
# 순위를 담을 리스트
result = []

for _ in range(num_of_students):
    weight, height = map(int, input().split())
    students_info.append([weight, height])

# 기본 등수를 1등으로 두고, 본인보다 키와 몸무게 모두 큰 사람이 있을 때만 등수에 +1
for i in students_info:
    rank = 1
    for j in students_info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    # 결과 리스트에 등수 추가
    result.append(rank)

print(*result)