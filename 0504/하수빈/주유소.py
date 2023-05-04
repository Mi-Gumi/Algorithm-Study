import sys
input = sys.stdin.readline

N = int(input())
km = list(map(int, input().split()))
pee = list(map(int, input().split()))
ans = 0
now = 0

# 끝에 도달할 때 까지
while now != N - 1:
    for i in range(now + 1, N):
        # 현재 요금 * 이동한 거리 추가
        ans += pee[now] * km[i - 1]
        # 이동한 곳의 요금이 현재 요금보다 낮다면 현재위치 교체
        if pee[now] > pee[i]:
            now = i
            break
        # 마지막에 도달 했다면
        if i == N - 1:
            # now를 마지막으로 교체
            now = N - 1

print(ans)