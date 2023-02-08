def moo(N):
    # 처음 moo문열의 길이
    ans = 3
    i = 0
    tmp = 0

    # moo문자열의 길이가 N보다 커질 때 까지
    while ans < N:
        # 차수 + 1
        i += 1
        # 가운데 문자열열의 길이는 차수 + 3
        mid = i + 3
        # tmp에 전 차수 문자열의 길이 저장
        tmp = ans
        # 현재 차수의 길이는 전 차수의 길이 * 2에 가운데 문자열의 길이를 더한 길이
        ans = 2 * ans + mid

    # 만약 N이 현재 문자열의 가운데 문자열 부분에 있다면
    if N <= tmp + i + 3:
        
        # N이 전 차수 바로 다음에 있다면
        if N == tmp + 1:
            # m 반환
            return 'm'
            # 아니라면
        else:
            # o 반환
            return 'o'
    # N이 현재 문자열의 끝 문자열 부분에 있다면
    else:
        # N을 N - tmp - i - 3으로 만들어서 재귀
        return moo(N - tmp - i - 3)


N = int(input())

print(moo(N))