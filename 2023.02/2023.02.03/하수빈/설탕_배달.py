N = int(input())

# 계산 횟수를 줄이기 위해 N에서 5씩 빼는 리스트 생성
minus_5_list = [N]
while N > 5:
    N = N - 5
    minus_5_list.append(N)

# 가장 작은 값부터 검사후 바로 break 하기위해 정렬
minus_5_list.sort()

# 검사 결과를 알려주기 위한 변수
not_find = True


for i in range(len(minus_5_list)):
    # N이 5의 배수라면
    if not N % 5:
        # minus_5_list의 길이가 N // 5 이므로 출력
        print(len(minus_5_list))
        not_find = False
        break
    # minus_5_list의 요소가 3의 배수라면
    if not minus_5_list[i] % 3:
        # ((N // 5) - 1 - i) + (요소 // 3) 출력 후 break
        print((len(minus_5_list) - 1 - i) + (minus_5_list[i] // 3))
        not_find = False
        break

# 찾지 못했다면 -1 출력
if not_find:
    print(-1)
