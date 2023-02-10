def moo_game(N, degree, s_len):
    if degree == 0:
        if N == 1:
            return 'm'
        else: return 'o'

    s_len = (s_len - degree - 3) // 2 # 분할
    degree -= 1

    if N <= s_len:
        return moo_game(N, degree, s_len)
    elif N - s_len == 1:
        return 'm'
    elif N > (s_len + 1) + degree + 3: # 중간값보다 뒤에 있을 경우
        return moo_game(N - (s_len+1) - degree - 3, degree, s_len)    
    else: return 'o'


N = int(input())

degree = 0
s_len = 3
while s_len < N: # 길이 구하기
    degree += 1
    s_len = 2 * s_len + (degree+3)

print(moo_game(N, degree, s_len))