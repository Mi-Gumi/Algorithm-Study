T = int(input())

arr = list(map(int, input().split()))

ans = []
total = 0
for i in range(len(arr)):
    cnt = []
    for j in range(1, 1001): # 1부터 1000까지 다 나눠주기
        if arr[i] % j == 0:
            cnt.append(j) # 소수 추가

    ans.append(cnt)

for a in ans:
    if len(a) == 2:
        total += 1

print(total)
