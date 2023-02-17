import sys
input = sys.stdin.readline

N, K = map(int, input().split())

don = []
for _ in range(N):
    n = int(input())
    don.append(n)

don.sort(reverse=True)

cnt = 0
for i in range(len(don)):
    if i == 0:
        if K >= don[i]:
            cnt += K // don[i]
            K = K % don[i]
    else:
        cnt += K // don[i]
        K = K % don[i]

print(cnt)