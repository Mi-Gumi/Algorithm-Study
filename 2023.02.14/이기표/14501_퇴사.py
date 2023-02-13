import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 , 0]]
for i in range(N):
    arr.append(list(map(int, input().split())))

dp = [0] * (N+1) # 수익 저장
for i in range(1, N+1): #arr[i][0] 기간 arr[i][1] 이익 / i+arr[i][0]-1 중복되는 인덱스 확인
    if i+arr[i][0]-1 < N+1: # 끝까지 도달 안했으면 / dp에 들어갈 인덱스 and 누적 기간
        dp[i+arr[i][0]-1] = max(dp[i+arr[i][0]-1], arr[i][1]+dp[i-1]) # 인덱스 조절
    dp[i] = max(dp[i], dp[i-1])
    print(dp)
print(dp[-1]) # 마지막으로 누적된 최고값 도출



