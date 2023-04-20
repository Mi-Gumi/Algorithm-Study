import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
lis = [0]

for num in A:
    # 만약 num이 현재 최장 증가 수열의 마지막 부분보다 크다면
    if num > lis[-1]:
        # 최장 증가 수열에 추가
        lis.append(num)
    # num이 현재 최장 증가 수열의 마지막 부분보다 작다면
    else:
        # 이 num이 들어갈 위치를 이분 탐색
        s, e = 0, len(lis) - 1
        while s < e:
            m = (s + e) // 2
            if lis[m] >= num:
                e = m
            else:
                s = m + 1
        lis[e] = num

# 최장 증가 수열에서 처음 0을 뺀 길이 출력
print(len(lis) - 1)
