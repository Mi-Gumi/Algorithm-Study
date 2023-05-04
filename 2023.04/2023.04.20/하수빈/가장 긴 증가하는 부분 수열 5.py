import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

lis = [-(10 ** 9)]
#            들어간 값    들어간 위치
lis_total = [(-(10 ** 9), 0)]

for num in A:
    # 만약 num이 현재 최장 증가 수열의 마지막 부분보다 크다면
    if num > lis[-1]:
        # 들어간 위치와 num 최장 증가 수열에 추가
        lis_total.append((num, len(lis)))
        lis.append(num)
    # num이 현재 최장 증가 수열의 마지막 부분보다 작다면
    else:
        # 이분 탐색으로 들어갈 위치 탐색
        s, e = 0, len(lis) - 1
        while s < e:
            mid = (s + e) // 2
            if lis[mid] >= num:
                e = mid
            else:
                s = mid + 1
        # 최장 증가 수열 교체
        lis[e] = num
        # 들어간 위치와 num 최장 증가 수열에 추가
        lis_total.append((num, e))

# 끝 에서 부터 최장 증가 수열에 사용된 num 역 탐색
now = len(lis) - 1
ans = []
for i in range(N, 0, -1):
    if lis_total[i][1] == now:
        ans.append(lis_total[i][0])
        now -= 1
    if not now:
        break

# ans 뒤집은 후 출력
ans.reverse()
print(len(ans))
print(*ans)
