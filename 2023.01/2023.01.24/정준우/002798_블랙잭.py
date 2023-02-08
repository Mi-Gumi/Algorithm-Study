amount_card, blackjack = map(int, input().split())
cards = list(map(int, input().split()))

# 세 카드 합 담을 변수 초기화
max_result = 0

# 카드 세개 전부 돌아보며
for i in cards:
    for j in cards:
        for k in cards:
            # 카드 중복이면 다시
            if i == j or j == k or k == i:
                continue
            sum = i + k + j
            # 최대값과 함께 블랙잭 규칙도 고려
            if sum > max_result and sum <= blackjack:
                max_result = sum

print(max_result)