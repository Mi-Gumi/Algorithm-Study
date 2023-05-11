from sys import stdin


glasses = int(stdin.readline())

wine_info = [0] * (glasses + 1)
dp = [0] * (glasses + 1)

for wine in range(1, glasses + 1):
    wine_info[wine] = int(stdin.readline())

if glasses == 1:
    print(wine_info[1])

elif glasses == 2:
    print(wine_info[1] + wine_info[2])

# 조건에 맞게 마실 수 있는 경우 중 최대값 찾기
else:
    dp[1] = wine_info[1]
    dp[2] = wine_info[1] + wine_info[2]

    for case in range(3, glasses + 1):
        dp[case] = max(dp[case - 1], dp[case - 3] + wine_info[case - 1] + wine_info[case], dp[case - 2] + wine_info[case])

    print(dp[glasses])
