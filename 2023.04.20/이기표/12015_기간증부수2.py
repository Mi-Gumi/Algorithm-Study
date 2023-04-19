N = int(input())
lst = list(map(int, input().split()))

tmp = [lst[0]]

def b_search(num):
    start = 0
    end = len(tmp)-1
    # 이미 오름차순으로 정렬되어있기때문에 이분탐색 진행
    while start <= end:
        mid = (start+end)//2
        # 해당값과 일치하면 종료
        if tmp[mid] == num:
            return mid
        # 이분 탐색 진행
        elif tmp[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    # 현재값보다 크거나같고 작은 수중에서 가장 작은 왼쪽 인덱스에 위치
    return start

for i in range(1, len(lst)):
    if tmp[-1] < lst[i]:
        tmp.append(lst[i])
    else:
        idx = b_search(lst[i])
        tmp[idx] = lst[i]

print(len(tmp))

