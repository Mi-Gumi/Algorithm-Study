day_of_happiness = int(input())

# 상담에 필요한 시간과 그 상담을 완료했을 때의 임금 리스트
time_needed = []
wage = []
profit = [0 for _ in range(day_of_happiness + 1)]

for _ in range(day_of_happiness):
    time, money = map(int, input().split())

    time_needed.append(time)
    wage.append(money)

# 뒷날부터 첫날까지 거꾸로 탐색
for i in range(day_of_happiness - 1, -1, -1):
    # 상담을 마치려면 퇴사일을 넘어갈 때는 다음날의 이익을 갖고 온다
    if time_needed[i] + i > day_of_happiness:
        profit[i] = profit[i + 1]

    # 상담을 마쳐도 퇴사일을 넘어가지 않는다면, 두 가지 경우로 나눠진다
    # 1) 상담을 안 할 경우, 다음 날의 이익인 profit[i + 1]
    # 2) 상담을 할 경우, 그 상담의 보수와 그 상담이 끝났을 날에 거꾸로 쌓여 이익을 더한다
    # 3) 둘 중 큰 값을 고른다
    else:
        profit[i] = max(profit[i + 1], profit[time_needed[i] + i] + wage[i])

# 첫날까지 탐색했을 때의 이익 출력
print(profit[0])