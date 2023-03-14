import sys
from itertools import permutations

susik_li = ['+', '-', '*', '/']  # + - * //

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
susik = list(map(int, input().split()))

real_susik = []

for i in range(len(susik)): # input 데이터를 진짜 수식으로 변경
    if susik[i] == 0: # 수식이 없을시에는 반영 X
        continue
    else:
        for j in range(susik[i]): #수식의 개수만큼 추가
            real_susik.append(susik_li[i])

real_susik = set(permutations(real_susik))  # 순열 생성

max_sum = -10000000000
min_sum = 10000000000
for su in real_susik:
    _sum = arr[0]
    for j in range(N-1): # eval 함수를 사용하여 문자열 속에서도 편리하게 연산
        _sum = int(eval(str(_sum) + su[j] + str(arr[j+1])))
    if max_sum < _sum: # 최대값 비교
        max_sum = _sum

    if min_sum > _sum: # 최소값 비교
        min_sum = _sum

print(max_sum)
print(min_sum)
