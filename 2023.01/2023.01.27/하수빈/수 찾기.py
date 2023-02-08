import sys
input = sys.stdin.readline

# 비교 대상 배열을 set로 바꿔 중복된 수를 제거
# 중복된 수가 줄어듬으로 처리속도 향상
N = int(input())
num_N = list(map(int, input().split()))
num_N = set(num_N)

M = int(input())
num_M = list(map(int, input().split()))

# M의 요소가 num_N안에 있다면 1출력 없다면 0출력
for num in num_M:
    if num in num_N:
        print(1)
    else:
        print(0)