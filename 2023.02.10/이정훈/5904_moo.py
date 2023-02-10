def moo(length, m, target):
    nextlen = (length - m) // 2  # 다음 수열( 사실 이전 수열 )

    if target <= nextlen:        # nextlen 보다 작을 경우
        return moo(nextlen, m - 1, target)
    if nextlen <= target <= nextlen + m: # 가운데 moo..의 범위 안에 있으면
        if target - nextlen == 1:  # 첫번째면 'm'
            return 'm'
        else:
            return 'o'
    else:      # 가운데의 무 너머에 있으면 무 전의 수열과 같으므로 target 재계산
        return moo(nextlen, m - 1, target - (nextlen + m))


N = int(input())

num = 3  # 'moo'
M = 3    # 현재 최고 moo 의 길이

while num < N:          # N이 수열의 길이보다 작을 때까지
    M += 1              # 최고 길이 + 1
    num = num * 2 + M   # 다음 수열의 길이 계산

ans = moo(num, M, N)
print(ans)