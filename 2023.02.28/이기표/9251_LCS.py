str1 = list(input()) # 기준 수열
str2 = list(input()) # 탐색 수열
dp = [[0] * (len(str1)+1) for _ in range(len(str2))] # 2차원 배열의 dp사용
# 최장 공통 부분 수열의 길이를 누적
for i in range(len(str2)): # 탐색 수열 기준으로
    for j in range(len(str1)):
        if str2[i] == str1[j]: # 수열이 일치할 경우
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 값의 + 1
        else: # 수열이 다를 경우
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 바로 전 값을 맵핑
print(dp[-1][len(str1)-1]) # 마지막 값이 최고 길이기 때문에 출력


