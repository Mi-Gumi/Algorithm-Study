from itertools import permutations

k = int(input())

boo = input().split()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 모든 수의 순열
pm = list(permutations(numbers, k + 1))
len_pm = len(pm)
# 값이 작은 순열부터
for j in range(len_pm):
    p = pm[j]
    for i in range(k):
        if boo[i] == '<':
            if p[i] < p[i + 1]:
                continue
            else:  # 우측이 더 작으면 break
                break
        else:
            if p[i] > p[i + 1]:
                continue
            else:  # 좌측이 더 작으면 break
                break
    else:  # break 되지 않으면 가능한 가장 작은 순열을 구했으니 break
        _min = p
        break
# 큰수부터
for j in range(len_pm - 1, -1, -1):
    p = pm[j]
    for i in range(k):
        if boo[i] == '<':
            if p[i] < p[i + 1]:
                continue
            else:
                break
        else:
            if p[i] > p[i + 1]:
                continue
            else:
                break
    else:
        _max = p
        break

print(*_max, sep='')
print(*_min, sep='')
