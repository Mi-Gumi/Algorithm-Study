def max_pay(n, day, nowpay):
    if day == n:  # 퇴사날
        return nowpay

    pays = [nowpay]  # 받을 수 있는 금액을 담을 리스트

    for i in range(day, day + sangdam[day][0]):  # 현재 날의 소요기간 안의 선택 가지수
        # 오늘 상담을 하거나 안하고 내일것을 하거나...
        if i == n:  # 안덱스 체크
            break
        if i + sangdam[i][0] <= n:  # 퇴사전까지 상담을 끝낼 수 있는 경우
            pays.append(max_pay(n, i + sangdam[i][0], nowpay + sangdam[i][1]))
    return max(pays)  # 이 날 기준 최고 금액 리턴


N = int(input())

sangdam = [list(map(int, input().split())) for _ in range(N)]

ans = max_pay(N, 0, 0)

print(ans)
