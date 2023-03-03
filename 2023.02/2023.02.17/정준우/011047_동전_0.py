num_of_coin_type, money = map(int, input().split())

# 사용 가능한 동전 종류를 담을 리스트
coin_type = []

for i in range(num_of_coin_type):
    coin_type.append(int(input()))

# 사용한 동전 수를 셀 변수
coin_count = 0

# 금액이 큰 동전부터 고려해야 가장 적은 수의 동전을 쓰게 되므로, 범위 조정
for i in range(num_of_coin_type - 1, -1, -1):
    # 몫만큼 사용한 동전 수에 더해주고, 남은 돈을 다음으로 큰 금액의 동전으로 지불
    coin_count += money // coin_type[i]
    money = money % coin_type[i]

print(coin_count)