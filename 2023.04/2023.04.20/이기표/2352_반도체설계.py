N = int(input())

lst = list(map(int, input().split()))
lis = [lst[0]]

def b_search(num):
    s = 0
    e = len(lis) - 1 # 인덱스로 들어가기에 -1

    while s <= e:
        m = (s + e) // 2
        # 같은 값을 찾으면 종료
        if lis[m] == num:
            return m
        # 이분 탐색
        if lis[m] < num:
            s = m + 1
        else:
            e = m - 1
    # 더 작은 값으로 갱신
    return s

for i in range(len(lst)):
    if lis[-1] < lst[i]:
        lis.append(lst[i])
    else:
        idx = b_search(lst[i])
        lis[idx] = lst[i]

print(len(lis))