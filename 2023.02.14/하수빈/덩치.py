import sys
input = sys.stdin.readline

N = int(input())

people = []

for _ in range(N):
    people.append(list(map(int, input().split())))

ans = []

for target in people:
    k = 1
    for other in people:
        # 만약 다른사람의 키와 몸무게가 target의 키와 몸무게 보다 모두 크다면 등수 + 1
        if other[0] > target[0] and other[1] > target[1]:
            k += 1
    # 등수 추가
    ans.append(k)

print(*ans)
