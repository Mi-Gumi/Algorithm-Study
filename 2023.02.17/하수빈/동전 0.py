import sys
input = sys.stdin.readline

N, K = map(int, input().split())
values = []
count = 0
for _ in range(N):
    values.append(int(input()))

# 잔액이 0이 될때 까지
while K != 0:
    for i in range(len(values)):
        # 동전의 가치가 잔액보다 크다면
        if values[i] > K:
            # 동전의 갯수 + 잔액 // 바로 전 동전의 가치
            count += K // values[i - 1]
            # 잔액은 잔액을 바로 전 동전의 가치로 나눈 나머지로 설정
            K = K % values[i - 1]
        # 마지막 동전이라면
        elif i == len(values) - 1:
            # 동전의 갯수 + 잔액 // 동전의 가치
            count += K // values[i]
            # 잔액은 잔액을 동전의 가치로 나눈 나머지로 설정
            K = K % values[i]

print(count)