from itertools import permutations

n = input()
m = sorted(list(n))
# 정렬된 수의 리스트로 순열을 만들면 값이 작은 순열부터 나옴
p = map(lambda x : int(''.join(x)),permutations(m, len(n)))

n = int(n)
# 큰 값이 존재하지 않을 경우
ans = 0
for num in p :
    if n < num:
        ans = num
        break
print(ans)