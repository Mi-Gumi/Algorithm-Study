# 9896을 표현할 때,
# 9 * (1010) + 8 * (100) + 6 * 1 으로 표현할 수 있음을 이용

num_of_words = int(input())

words = [input() for _ in range(num_of_words)]

# 알파벳과 해당 알파벳이 들어가는 자리를 알려주는 딕셔너리
word_dict = {}

# 작은 수의 위치에 들어갈 알파벳부터 10^n 을 배정
for word in words:
    for exponent, alphabet in enumerate(word[::-1]):
        # 딕셔너리에 해당 알파벳이 없으면 추가
        if alphabet not in word_dict:
            # pow(base, exp) -> base의 exp 거듭제곱 반환 함수
            # (10 ** exponent)도 가능
            word_dict[alphabet] = pow(10, exponent)
        # 딕셔너리에 해당 알파벳이 있을 때,
        # 1) 자리수가 다르면 1000 + 10 으로 1010 의 결과를 얻음으로 천의 자리와 십의 자리 둘 다 있다는 것 표시
        # 2) 자리수가 같으면 1000 + 1000 으로 2000의 결과를 얻음으로 이후 과정 중 2배의 값을 받게 된다 -> 3000이면 3배
        else:
            word_dict[alphabet] += pow(10, exponent)

# 큰 자리수부터 다루기 위해 내림차순으로 정렬
word_dict = sorted(word_dict.items(), reverse = True, key = lambda x: x[1])

answer = 0

# 딕셔너리의 각 value에 저장된 자리수 관련 숫자에 차례로 곱할 숫자 리스트
numbers = [number for number in range(10)]

# 딕셔너리에 구해놓은 자리수를 의미하는 숫자에 9부터 차례로 곱해서 더하기
for info in word_dict:
    answer += info[1] * numbers.pop()

print(answer)