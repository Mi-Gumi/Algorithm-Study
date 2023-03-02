# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = [int(input()) for _ in range(N)]
    

# max_val = 0
# for i in range(len(arr)):
#     sum_val = 0
#     for j in range(len(arr)):
#         if arr[i] <= arr[j]:
#             sum_val += arr[i]
#     if sum_val > max_val:
#         max_val = sum_val

# print(max_val)

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

a = sorted(arr, reverse = True)

max_val = 0
for i in range(len(a)):
    if a[i]+(a[i]*i) > max_val:
        max_val = a[i]+(a[i]*i)


print(max_val)