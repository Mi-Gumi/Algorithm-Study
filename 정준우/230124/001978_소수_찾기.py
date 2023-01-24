N = int(input())
nums = map(int, input().split())
# 소수 개수 셀 변수 초기화
prime_num = 0

for num in nums:
    # 소수일때 0을 유지할 변수 초기화
    is_prime_num = 0
    # 1은 무조건 성립이라 빼기 위한 조건
    if num > 1:
        for i in range(2, num):
            # 1과 자기 자신 빼고 나누어 떨어지는지 판단
            if num % i == 0:
                is_prime_num += 1
           
        if is_prime_num == 0:
            prime_num += 1

print(prime_num)
