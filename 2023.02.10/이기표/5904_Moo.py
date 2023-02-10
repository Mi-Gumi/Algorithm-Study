def moo_game(N, degree, s_len):
    if degree == 0: # 0차수 일 경우 해당하는 값들 바로 반환
        if N == 1:
            return 'm'
        else: return 'o'

    s_len = (s_len - degree - 3) // 2 # 분할 진행
    degree -= 1

    if N <= s_len:
        return moo_game(N, degree, s_len)
    elif N - s_len == 1: # 문자열이랑 1차이 나면 바로 m 반환
        return 'm'
    elif N > (s_len + 1) + degree + 3: # 중간값보다 뒤에 있을 경우
        return moo_game(N - (s_len+1) - degree - 3, degree, s_len) # 중간 앞에 문자열로 이동
    else: return 'o' # 그 외의 경우는 전부 o 반환


N = int(input())

degree = 0 # 차수
s_len = 3 # 문자열 길이
while s_len < N: # 공식에 따라 input값 보다 큰 길이 구하기
    degree += 1
    s_len = 2 * s_len + (degree+3) # 이전 길이 s_len + 차수+3은 중간값 개수

print(moo_game(N, degree, s_len))