n = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]


def binarySearch(e):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1

    return start


for i in range(n):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
    else:
        idx = binarySearch(arr[i])
        LIS[idx] = arr[i]

print(len(LIS))
print(*LIS)



