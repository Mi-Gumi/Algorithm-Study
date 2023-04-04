N = int(input())

# 홀수개의 타일은 무조건 0 이기 때문에 이는 skip 하고 진행
dp = [0] + [0 for _ in range(N//2 + 4)] # 반만 체크 + 넉넉하게 +4 해주기
dp[0] = 1 # X0 <- X4 이상일 경우에 중간에 있는 사각형에 대한 경우
dp[1] = 3 # X2

if N %2 != 0:
    print(0)
else:
    n = N//2

    for i in range(2,n+1): # 점화식으로 통해 얻은 값
        # 초기의 3개 * 이전의 값 + 바꿀수 있는 사각형
        dp[i] += dp[i-1]* 3 + 2
        for j in range(2,i):
            dp[i] += dp[i-j]*2 # 갯수를 활용해서 얻을 수 있는 X a 의 가짓수 *2 위, 아래
    print(dp[n])