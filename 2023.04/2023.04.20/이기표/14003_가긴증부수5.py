N = int(input())
lst = list(map(int, input().split()))

lis = [-1000000001]
check = [0] * (N+1)
def b_search(num):
    s = 0
    e = len(lis) - 1
    while s <= e:
        m = (s + e) // 2
        if lis[m] == num:
            return m
        # 이분 탐색
        elif lis[m] < num:
            s = m + 1
        else:
            e = m - 1
    # # 현재값보다 크거나같고 작은 수중에서 가장 작은 왼쪽 인덱스에 위치
    return s

for i in range(len(lst)):
    if lis[-1] < lst[i]:
        lis.append(lst[i])
        # 부븐 수열의 위치를 체크
        check[i] = len(lis) - 1
    else:
        # 마찬가지로 부분 수열의 위치를 체크
        check[i] = b_search(lst[i])
        lis[check[i]] = lst[i]
L = len(lis) - 1
print(L) # 수열의 길이
ans = []
# 뒤에서부터 체크한 위치와 일치하면 출력
for i in range(N, -1, -1):
    if check[i] == L:
        ans.append(lst[i])
        L -= 1
print(*ans[::-1])


