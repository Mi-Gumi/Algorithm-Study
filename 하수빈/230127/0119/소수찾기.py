N = input()
num = list(map(int, input().split()))
# 갯수를 담을 변수
count = 0

for n in num:
    # 1은 소수가 아님으로 1이 아닐경우만 생각
    if n != 1:
        # n을 2부터 n-1까지로 나눴을때 나머지가 0인 경우가 있다면 소수가 아님으로 break
        for i in range(2, n):
            if n % i == 0:
                break
        # for문을 통과했다면 count + 1
        else:
            count += 1

print(count)