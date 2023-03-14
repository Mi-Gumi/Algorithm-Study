import sys
input = sys.stdin.readline

T = int(input())

step_li = [0]
max_sum = 0

for t in range(T):   # 계단 리스트 만들기
    step = int(input())
    step_li.append(step)


if len(step_li) <= 2: # 배열의 길이가 2 이하일 경우는 다 누적
    print(sum(step_li))
else:
    dp = [0] * (T + 1) # DP 배열 생성
    dp[1] = step_li[1]
    dp[2] = step_li[1] + step_li[2]

    for i in range(3, T+1): # 점화식 생성
        dp[i] = max(dp[i-2] + step_li[i], dp[i-3] + step_li[i-1] + step_li[i])

    print(dp[T])




# def step_func(i, arr):
#     global max_sum
#
#     if len(arr) < 2: # 길이가 2이하는 다 누적
#         max_sum = sum(arr)
#         return max_sum
#
#     if i-1 == 0:
#         max_sum += arr[i] + arr[i-1]
#         return max_sum
#
#     elif i-2 == 0:
#         if arr[i - 1] > arr[i - 2]:  # 다음 수의 누적합이 클 때
#             max_sum += arr[i] + arr[i - 1]
#             return max_sum
#
#         elif arr[i - 1] < arr[i - 2]:  # 다다음수의 누적합이 클 때
#             max_sum += arr[i] + arr[i - 2]
#             return max_sum
#
#     if arr[i-1] > arr[i-2]: # 다음 수의 누적합이 클 때
#         max_sum += arr[i]
#         return step_func(i-1, arr)
#
#     elif arr[i-1] < arr[i-2]: # 다다음수의 누적합이 클 때
#         max_sum += arr[i]
#         return step_func(i-2, arr)