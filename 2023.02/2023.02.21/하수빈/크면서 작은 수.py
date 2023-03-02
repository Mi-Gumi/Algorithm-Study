import sys


def recur(N, i):
    global min_num

    # 순열이 완성 됬다면
    if i == N:
        # 순열이 원본가 같지 않다면
        if num != origin:
            # min_num 교체
            min_num = num.copy()
        return

    # min_num의 앞자리 보다 순열의 앞자리가 크거나 원본의 앞자리보다 순열의 앞자리가 작다면 종료
    if int(''.join(min_num[:i + 1])) < int(''.join(num[:i + 1])) or int(''.join(origin[:i + 1])) > int(''.join(num[:i + 1])):
        return

    # 순열 생성
    for j in range(i, N):
        num[i], num[j] = num[j], num[i]
        recur(N, i + 1)
        num[i], num[j] = num[j], num[i]


num = list(sys.stdin.readline()[:-1])
# 숫자 원본
origin = num.copy()
N = len(num)
min_num = ['9'] * N
# 최솟값 원본
origin_min = min_num.copy()

recur(N, 0)

# 최솟값이 변하지 않았다면
if min_num == origin_min:
    # 0출력
    print(0)
# 최솟값이 변했다면
else:
    # 변한 값 출력
    print(''.join(min_num))