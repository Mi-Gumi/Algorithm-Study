import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
ans = 0

# 3개를 더하는 모든 경우의 수를 찾는 반복문
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # 3개를 더한 값이 M보다 작고 ans 보다 크다면 ans를 3개를 더한 값으로 교체
            if num[i] + num[j] + num[k] <= M and num[i] + num[j] + num[k] > ans:
                ans = num[i] + num[j] + num[k]

print(ans)