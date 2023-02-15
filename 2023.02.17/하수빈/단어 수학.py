import sys
input = sys.stdin.readline

N = int(input())

value = {}
words = []

# \n 제외한 문자열 배열 생성
for _ in range(N):
    tmp = input()[:-1]
    words.append(tmp)

# 알파벳 별 가중치 설정
for w in words:
    for i in range(len(w)):
        # 알파벳이 딕셔너리 안에 없다면
        if not value.get(w[i]):
            # 알파벳 가충치는 알파벳 자릿수로 설정
            value[w[i]] = 10 ** (len(w) - i - 1)
        # 알파벳이 딕셔너리 안에 있다면
        else:
            # 알파벳 가충치 + 알파벳 자릿수
            value[w[i]] += 10 ** (len(w) - i - 1)

# 가충치 정렬
value_list = sorted(list(value.values()))
ans = 0
i = 9

# 가중치가 빌 때까지
while value_list:
    # 가중치가 높은 알파벳부터 9~1을 곱해 ans에 연산
    ans += i * value_list[-1]
    # 가중치 배열에서 제거
    value_list.pop()
    i -= 1

print(ans)